#!/usr/bin/env python
# encoding: utf-8
"""
routes.py

Lists routes available from a GTFS feed
"""

import pandas
import zipfile
import sys


class Feed(object):
    """
    Represents a GTFS data feed
    """
    def __init__(self, path):
        if zipfile.is_zipfile(path):
            archive = zipfile.ZipFile(path)
            path = path.rstrip('.zip') + '/'
            archive.extractall(path)

        self.routes = pandas.read_csv(path + 'routes.txt',
                                      dtype={'route_id': str,
                                             'route_short_name': str})


def main():
    mbta = Feed('tests/MBTA_GTFS.zip')

    for route in mbta.routes:
        print route

    sys.exit(0)

if __name__ == '__main__':
    main()
