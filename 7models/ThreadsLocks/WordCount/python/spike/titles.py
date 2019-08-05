#!/usr/bin/env python3

import sys

import xml.etree.ElementTree as ET


LEN_TAG = len('{http://www.mediawiki.org/xml/export-0.10/}')


def titles(file_name):
    count = 0
    for _, elem in ET.iterparse(file_name):
        tag = elem.tag[LEN_TAG:]
        if tag == 'title':
            count += 1
            print(count, elem.text.strip())
        elem.clear()

titles(sys.argv[1])
