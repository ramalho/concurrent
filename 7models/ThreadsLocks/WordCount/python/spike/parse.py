#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET

FILE_NAME = 'ptwiki-20190801-pages-articles-multistream.xml'

NS_TAG = '{http://www.mediawiki.org/xml/export-0.10/}'


def titles(file_name):
    count = 0
    for _, elem in ET.iterparse(file_name):
        tag = elem.tag.replace(NS_TAG, '')
        if tag == 'title':
            count += 1
            print(count, elem.text)


titles(sys.argv[1])
