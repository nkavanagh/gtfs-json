"""
GTFS feed parsing

Created by Niall Kavanagh <niall@kst.com> on 6/23/2014
"""

import zipfile
import pandas as pd


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
