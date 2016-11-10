from robobrowser import RoboBrowser
import re
from harvest import get_index, get_total_pages
import csv
import os


def list_indexes(write_csv=True):
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
    indexes = list_indexes(write_csv=False)
    for index in indexes[start:]:
        get_index(index)


def get_pages():
    indexes = list_indexes(write_csv=False)
    for index in indexes:
        title, url = index
        pages = get_total_pages(url)
        print '{}: {}'.format(title, pages)




