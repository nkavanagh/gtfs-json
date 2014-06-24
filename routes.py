#!/usr/bin/env python
# encoding: utf-8
"""
routes.py

Lists routes available from a GTFS feed
"""

from __future__ import print_function
import sys
import argparse
import os
import json
from gtfs import feed as gtfs


def main():
    # command line args
    parser = argparse.ArgumentParser(description='Generates a JSON \
                                     representation of routes from a \
                                     GTFS feed')

    parser.add_argument('filename', help='GTFS ZIP file or path to \
                       unzipped GTFS data')

    parser.add_argument('--type', type=int,
                        help='only show routes of a particular type')

    args = parser.parse_args()

    if not os.path.isfile(args.filename):
        print('File not found: {0}'.format(args.filename),
              file=sys.stderr)
        sys.exit(2)

    # feed
    feed = gtfs.Feed(args.filename)

    routes = []

    for route_id, row in feed.routes.iterrows():
        route = {'id': route_id,
                 'name': row.route_long_name,
                 'type': row.route_type}

        if (args.type == row.route_type):
            routes.append(route)

    # output json
    output = json.dumps(routes, indent=4)
    print('{0}'.format(output))

    sys.exit(0)

if __name__ == '__main__':
    main()
