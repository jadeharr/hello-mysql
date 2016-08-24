#!/usr/bin/env python3

"""Test."""

from __future__ import print_function
import argparse
import pymysql


def main():
    """run main function."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-s", "--subject", help="imputs subject to website.",
        required=True)
    parser.add_argument(
        "-b", "--body", help="inputs body to website.",
        required=True)
    parser.add_argument(
        "-i", "--image_url",
        help="inputs image_url to website.", required=True)
    parser.add_argument(
        "-l", "--link",
        help="inputs link to website.", required=True)

    args = parser.parse_args()

    blog = Blog(args.body, args.subject, args.image_url, args.link)

    blog.post()

    if args.subject:
        print("subject has been updatated")

    if args.body:
        print("body has been updated")

    if args.image_url:
        print("image_url has been updated")

    if args.link:
        print("link has been updated")


class Blog(object):
    """funtion for posting."""

    def __init__(self, body, subject, image_url, link):
        """init for blog."""
        self.body = body
        self.subject = subject
        self.image_url = image_url
        self.link = link

        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', passwd='Hello123?', db='blog')

    def post(self):
        """Add a post to blog."""
        cur = self.conn.cursor()

        sql = (
            'INSERT INTO flask_tbl (subject, body, image_url, link) '
            'VALUES ("%s", "%s", "%s", "%s")') % (
                self.subject, self.body, self.image_url, self.link)

        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()


if __name__ == "__main__":
    main()
