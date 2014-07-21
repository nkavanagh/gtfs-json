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

    parser.add_argument('--output',
                        help='output to file instead of stdout')

    args = parser.parse_args()

    if not os.path.exists(args.filename):
        print('File not found: {0}'.format(args.filename),
              file=sys.stderr)
        sys.exit(2)

    output_file = sys.stdout
    if args.output is not None:
        output_file = open(args.output, 'w')

    # feed
    feed = gtfs.Feed(args.filename)

    routes = feed.get_routes(args.type)

    # output json
    output = json.dumps(routes, indent=4)
    print('{0}'.format(output),
          file=output_file)

    sys.exit(0)

if __name__ == '__main__':
    main()
