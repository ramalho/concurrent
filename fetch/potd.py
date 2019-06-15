#!/usr/bin/env python3

import calendar
import http.client
from urllib.parse import urlparse

BASE_URL = 'https://en.wikipedia.org/wiki/Wikipedia:Picture_of_the_day/'
HTML_DIR = 'html'

month_names = (calendar.month_name[n] for n in range(1, 13))

years = range(2005, 2019)

months = [f'{m}_{y}' for m in month_names for y in years]


def get_month(cnx, path, year, month):
    name = f'{calendar.month_name[month]}_{year}'
    print(path + name)
    cnx.request('GET', path + name)
    resp = cnx.getresponse()
    assert resp.status == 200
    body = resp.read()
    with open(f'{HTML_DIR}/{year}-{month:02d}.html', 'wb') as fp:
        fp.write(body)

def main():
    url = urlparse(BASE_URL)
    cnx = http.client.HTTPSConnection(url.netloc)

    for year in range(2005, 2019):
        for month in range(1, 13):
            get_month(cnx, url.path, year, month)

if __name__ == '__main__':
    main()
