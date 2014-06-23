#!/usr/bin/env python
# encoding: utf-8
"""
routes.py

Lists routes available from a GTFS feed
"""

import pandas as pd
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

        self.routes = pd.read_csv(path + 'routes.txt',
                                  index_col='route_id',
                                  usecols=['route_id',
                                           'route_long_name',
                                           'route_type'],
                                  dtype={'route_id': str,
                                         'route_long_name': str,
                                         'route_type': int})


def main():
    mbta = Feed('tests/MBTA_GTFS.zip')

    for route_id, row in mbta.routes.iterrows():
        print route_id

    sys.exit(0)

if __name__ == '__main__':
    main()
