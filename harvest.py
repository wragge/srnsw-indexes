from robobrowser import RoboBrowser
from robobrowser.forms.fields import Input
import re
import csv
import os
import time

def check_page(browser):
    last_page = None
    last_link = browser.find('a', href="javascript:__doPostBack('GridView1','Page$Last')")
    if not last_link:
        nav_links = browser.find_all('a', href=re.compile("javascript:__doPostBack\('GridView1','Page\$"))
        last_link = nav_links[-1]
        last_page = int(re.search(r'Page\$(\d+)', last_link['href']).group(1))
    return last_page


def get_values(row, tag):
    values = []
    for cell in row.find_all(tag):
        values.append(cell.string.replace(u'\xa0', '').encode('utf-8'))
    return values


def slugify(title):
    return re.sub(r'\W+', '-', title.lower())


def process_page(browser, page, last_page, results, table_title):
    print page
    table = browser.find(id='GridView1')
    rows = table.find_all('tr', recursive=False)
    for index, row in enumerate(rows[:-1]):
        if index == 0:
            if page == 1:
                results.append(get_values(row, 'th'))
        else:
            results.append(get_values(row, 'td'))
    page += 1
    if not last_page:
        last_page = check_page(browser)
    if not last_page or page <= last_page:
        nav_form = browser.get_form(id='form1')
        new_field1 = Input('<input name="__EVENTARGUMENT" value="Page${}" />'.format(page))
        nav_form.add_field(new_field1)
        new_field2 = Input('<input name="__EVENTTARGET" value="GridView1" />')
        nav_form.add_field(new_field2)
        browser.submit_form(nav_form)
        time.sleep(0.2)
        process_page(browser, page, last_page, results, table_title)
    else:
        with open(os.path.join('data', '{}.csv'.format(slugify(table_title))), 'wb') as csv_file:
            csv_writer = csv.writer(csv_file)
            for result in results:
                csv_writer.writerow(result)


def get_index(index):
    browser = RoboBrowser(history=True)
    browser.open(index[1])
    process_page(browser, 1, None, [], index[0])


