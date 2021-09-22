#!/usr/bin/env python3
import argparse
import feedparser

parser = argparse.ArgumentParser(description='Filter an RSS or ATOM feed by title or description.')
parser.add_argument('feed_uri', type=str, nargs=1)
parser.add_argument('--title', type=str)
parser.add_argument('--description', type=str)
args = parser.parse_args()

data = feedparser.parse(args.feed_uri[0])

for entry in data.entries:
    if args.title is not None and args.description is not None:
        if args.title in entry.title and args.description in entry.description:
            print(entry.link)
    elif args.title is not None:
        if args.title in entry.title:
            print(entry.link)
    elif args.description is not None:
        if args.description in entry.description:
            print(entry.link)
    else:
        print(entry.link)
