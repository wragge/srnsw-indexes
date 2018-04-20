#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser
import re
import csv
import os
import time


def get_values(row, tag):
    '''
    Extracts values from an index row.
    '''
    values = []
    for cell in row.find_all(tag):
        try:
            value = cell.string.replace(u'\xa0', '').encode('utf-8')
        except AttributeError:
            value = cell.string
        values.append(value)
    return values


def slugify(title):
    '''
    Turn index titles into a safe filename.
    '''
    return re.sub(r'\W+', '-', title.lower())


def get_index(index, start_page=0):
    title, url = index
    page = start_page
    browser = RoboBrowser(history=False)
    browser.open(url)
    last_link = browser.find('a', title='Go to last page')
    last_page = int(re.search('page=(\d+)', last_link['href']).group(1))
    print('{} pages'.format(last_page))
    with open(os.path.join('data', '{}.csv'.format(slugify(title))), 'wb') as csv_file:
        csv_writer = csv.writer(csv_file)
        while page <= last_page:
            print('page {}'.format(page))
            if page == 0:
                header = browser.find('thead')
                for row in header.find_all('tr', recursive=False):
                    csv_writer.writerow(get_values(row, 'th'))
            table = browser.find('tbody')
            for row in table.find_all('tr', recursive=False):
                csv_writer.writerow(get_values(row, 'td'))
            page += 1
            if page <= last_page:
                time.sleep(0.2)
                if 'page=' not in url:
                    print('NOT')
                    url = url.replace('?', '?page={}&'.format(page))
                else:
                    url = re.sub('page=\d+', 'page={}'.format(page), url)
                print url
                browser.open(url)
