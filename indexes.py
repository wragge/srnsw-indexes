#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser
from robobrowser.forms.fields import Input
import re
from harvest import get_index, get_total_pages, slugify
import csv
import os


def list_indexes(write_csv=True):
    '''
    Starts at https://www.records.nsw.gov.au/archives/collections-and-research/guides-and-indexes/indexes-a-z
    and then moves down the hierarchy to find all the indexes.
    It then constructs a blank search query that will actually return the index results.
    Returns a list of [index title, query url] lists.
    '''
    categories = []
    indexes = []
    urls = []
    browser = RoboBrowser(history=True)
    browser.open('https://www.records.nsw.gov.au/archives/collections-and-research/guides-and-indexes/indexes-a-z')
    links = browser.find_all('a', href=re.compile('/archives/collections-and-research/guides-and-indexes/[a-z\-]+/indexes'))
    for link in links:
        if link['href'] not in categories:
            categories.append(link['href'])
    for category in categories:
        url = 'https://www.records.nsw.gov.au' + category
        browser.open(url)
        for index in browser.find_all('a', class_='index'):
            if index['href'] not in indexes and 'indexes' in index['href']:
                indexes.append(index['href'])
    for index in indexes:
        browser.open(index)
        text_field = browser.find('input', type='textbox')
        query = text_field['name']
        if ' ' in query:
            query = '[{}]'.format(query)
        table = browser.find('input', {'name': 'table'})['value']
        index_id = browser.find('input', {'name': 'id'})['value']
        url = 'http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table={}&id={}&frm=1&query={}:%'.format(table.encode('utf-8'), index_id, query)
        urls.append([table.encode('utf-8'), url])
    if write_csv:
        with open(os.path.join('data', 'indexes.csv'), 'wb') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for url in urls:
                writer.writerow(url)
    return urls


def get_all_indexes(start=0):
    '''
    Harvest ALL THE INDEXES.
    This will probably fail at some point because there's lots to harvest.
    If so then restart using the start parameter to pick up where it left off.
    The start number will be the row number indexes.csv minus 1.
    '''
    indexes = list_indexes(write_csv=False)
    for index in indexes[start:]:
        get_index(index)


def get_pages():
    '''
    Displays the number of pages per index.
    '''
    indexes = list_indexes(write_csv=False)
    for index in indexes:
        title, url = index
        pages = get_total_pages(url)
        print '{}: {}'.format(title, pages)


def check_rows():
    '''
    Compares the number of rows in each index online with the total number harvested.
    Basically a way of checking if the harvest completed properly.
    You could also run this periodically to see if any data has been added to the indexes.
    '''
    indexes = list_indexes(write_csv=False)
    results = []
    browser = RoboBrowser()
    for index in indexes:
        title, url = index
        browser.open(url.replace('’', '%u2019'))
        nav_form = browser.get_form(id='form1')
        new_field1 = Input('<input name="__EVENTARGUMENT" value="Page$Last" />')
        nav_form.add_field(new_field1)
        new_field2 = Input('<input name="__EVENTTARGET" value="GridView1" />')
        nav_form.add_field(new_field2)
        browser.submit_form(nav_form)
        nav_links = browser.find_all('a', href=re.compile("javascript:__doPostBack\('GridView1','Page\$"))
        nav_links[-1].parent.parent.next_sibling
        last_page = nav_links[-1].parent.parent.next_sibling.string
        table = browser.find(id='GridView1')
        rows = table.find_all('tr', recursive=False)
        last_rows = len(rows) - 2
        total_rows = ((int(last_page) - 1) * 20) + last_rows
        try:
            with open(os.path.join('data', '{}.csv'.format(slugify(title))), 'rb') as csv_file:
                reader = csv.reader(csv_file)
                csv_rows = list(reader)
                csv_count = len(csv_rows) - 1
        except IOError:
            print '{} -- not found'.format(title)
        else:
            results.append([title, url, total_rows, csv_count])
            if total_rows != csv_count:
                print '{}: {} of {}'.format(title, csv_count, total_rows)
    return results


def print_details():
    indexes = sorted(check_rows())
    total = 0
    print '| Name | Number of rows | Download data | View at SRNSW |'
    print '|------|----------------|---------------|---------------|'
    for index in indexes:
        title, url, rows, harvested = index
        total += harvested
        link = 'data/{}.csv'.format(slugify(title))
        print '| {} | {} | [CSV file]({}) | [Web site]({}) |'.format(title, harvested, link, url)
    print '{} indexes with {} rows'.format(len(indexes), total)


