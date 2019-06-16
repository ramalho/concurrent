#!/usr/bin/env python3

import calendar
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = 'https://en.wikipedia.org/wiki/Wikipedia:Picture_of_the_day/'
HTML_DIR = 'html'


def get_month(year, month):
    name = f'{calendar.month_name[month]}_{year}'
    url = BASE_URL + name
    print(url)
    resp = urlopen(url)
    assert resp.status == 200
    body = resp.read()
    with open(f'{HTML_DIR}/{year}-{month:02d}.html', 'wb') as fp:
        fp.write(body)
    return (year, month)


def main():
    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = (executor.submit(get_month, year, month)
                   for year in range(2005, 2019) for month in range(1, 13))

        for future in as_completed(futures):
            try:
                year_month = future.result()
            except Exception as exc:
                print(f'{year_month} generated an exception: {exc}')
            else:
                print(year_month)


if __name__ == '__main__':
    main()
