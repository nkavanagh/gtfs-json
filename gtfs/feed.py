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
            self.path = path.rstrip('.zip') + '/'
            archive.extractall(path)
        else:
            self.path = path + '/'

    def load_routes(self):
        self.routes = pd.read_csv(self.path + 'routes.txt',
                                  index_col='route_id',
                                  usecols=['route_id',
                                           'route_long_name',
                                           'route_type'],
                                  dtype={'route_id': str,
                                         'route_long_name': str,
                                         'route_type': int})

    def load_stops(self):
        self.stops = pd.read_csv(self.path + 'stops.txt',
                                 index_col='stop_id',
                                 usecols=['stop_id',
                                          'stop_name',
                                          'stop_lat',
                                          'stop_lon']
                                 )

    def load_calendar(self):
        self.stops = pd.read_csv(self.path + 'calendar.txt',
                                 index_col='service_id',
                                 usecols=['service_id',
                                          'monday',
                                          'tuesday',
                                          'wednesday',
                                          'thursday',
                                          'friday',
                                          'saturday',
                                          'sunday',
                                          'start_date',
                                          'end_date']
                                 )

    def load_calendar_dates(self):
        self.stops = pd.read_csv(self.path + 'calendar_dates.txt',
                                 index_col='service_id',
                                 usecols=['service_id',
                                          'date',
                                          'exception_date']
                                 )

    def load_trips(self):
        self.trips = pd.read_csv(self.path + 'trips.txt',
                                 index_col='trip_id',
                                 usecols=['route_id',
                                          'service_id',
                                          'trip_id',
                                          'trip_headsign',
                                          'direction_id']
                                 )

    def get_routes(self, route_type):
        if self.routes is None:
            self.load_routes()

        routes = []

        for route_id, row in self.routes.iterrows():
            route = {'id': route_id,
                     'name': row.route_long_name,
                     'type': row.route_type}

            if (route_type == row.route_type):
                routes.append(route)

        return routes

    def get_trips(self, route_id):
        if self.trips is None:
            self.load_trips()

        trips = []

        pass
