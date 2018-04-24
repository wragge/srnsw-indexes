#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser
import re
from harvest import get_index, slugify
import csv
import os
import pandas as pd


def list_indexes(write_csv=True):
    categories = []
    indexes = []
    urls = []
    browser = RoboBrowser()
    browser.open('https://www.records.nsw.gov.au/archives/collections-and-research/guides-and-indexes/indexes-a-z')
    links = browser.find_all('a', href=re.compile('/archives/collections-and-research/guides-and-indexes/[a-z\-]+/indexes'))
    for link in links:
        if link['href'] not in categories:
            categories.append(link['href'])
    for category in categories:
        url = 'https://www.records.nsw.gov.au' + category
        browser.open(url)
        for index in browser.find_all('a', class_='form-submit'):
            try:
                index_id = re.search('\?id=(\d+)', index['href']).group(1)
            except AttributeError:
                print('Nope')
            else:
                if index_id not in indexes:
                    indexes.append(index_id)
    for index in indexes:
        browser.open('https://www.records.nsw.gov.au/search_form?id=' + index)
        title = browser.find('h1').string
        form = browser.get_form(id='records-online-index-search-form')
        form[form.keys()[0]].value = '%'
        browser.submit_form(form)
        urls.append([title.encode('utf-8'), browser.url])
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
        browser.open(url)
        last_link = browser.find('a', title='Go to last page')
        last_page = re.search('page=(\d+)', last_link['href']).group(1)
        last_url = url.replace('?', '?page={}&'.format(last_page))
        browser.open(last_url)
        table = browser.find('tbody')
        rows = table.find_all('tr', recursive=False)
        last_rows = len(rows)
        total_rows = (int(last_page) * 20) + last_rows
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
        link = 'https://github.com/wragge/srnsw-indexes/raw/master/data/{}.csv'.format(slugify(title))
        print '| {} | {} | [CSV file]({}) | [Web site]({}) |'.format(title, harvested, link, url)
    print '{} indexes with {} rows'.format(len(indexes), total)


def clean_index(index):
    '''
    Remove empty columns.
    '''
    print(index)
    no_empty = lambda x: not (x.startswith('Unnamed: ') or x == 'Add to request')
    df = pd.read_csv(index, usecols=no_empty)
    df.to_csv(index.replace('.csv', '-cleaned.csv'), index=False)

def clean_all():
    indexes = list_indexes(write_csv=False)
    for index in indexes:
        index_path = os.path.join('data', '{}.csv'.format(slugify(index[0])))
        clean_index(index_path)
