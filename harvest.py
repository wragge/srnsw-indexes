#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser
from robobrowser.forms.fields import Input
import re
import csv
import os
import time


def get_total_pages(url):
    '''
    Goes to the last page of results to find the total number of pages in an index.
    '''
    browser = RoboBrowser(history=True)
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
    return int(last_page)


def get_values(row, tag):
    '''
    Extracts values from an index row.
    '''
    values = []
    for cell in row.find_all(tag):
        values.append(cell.string.replace(u'\xa0', '').encode('utf-8'))
    return values


def slugify(title):
    '''
    Turn index titles into a safe filename.
    '''
    return re.sub(r'\W+', '-', title.lower())


def get_index(index, start_page=1):
    '''
    Harvest an index.
    Expects a list containing [index title, query url] such as created by indexes.list_indexes()
    '''
    title, url = index
    url = url.replace('’', '%u2019')
    print title
    last_page = get_total_pages(url)
    print last_page
    page = start_page
    browser = RoboBrowser()
    browser.open(url)
    with open(os.path.join('data', '{}.csv'.format(slugify(title))), 'ab') as csv_file:
        csv_writer = csv.writer(csv_file)
        while page <= last_page:
            print page
            table = browser.find(id='GridView1')
            rows = table.find_all('tr', recursive=False)
            for index, row in enumerate(rows[:-1]):
                if index == 0:
                    if page == 1:
                        csv_writer.writerow(get_values(row, 'th'))
                else:
                    csv_writer.writerow(get_values(row, 'td'))
            page += 1
            time.sleep(0.2)
            nav_form = browser.get_form(id='form1')
            new_field1 = Input('<input name="__EVENTARGUMENT" value="Page${}" />'.format(page))
            nav_form.add_field(new_field1)
            new_field2 = Input('<input name="__EVENTTARGET" value="GridView1" />')
            nav_form.add_field(new_field2)
            browser.submit_form(nav_form)



