#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-

""" Password Generator Program """

__authors__ = "gerson23 and jbsilva"

import argparse
import Password


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Password Generator Program.',
                                     epilog='This program generates passwords')
    parser.add_argument('-l', '--length', type=str, default=10,
                        help='Length of password')
    parser.add_argument('-nc', '--no_chars', dest="chars",
                        action='store_false',
                        help='Excludes characters [a-zA-Z] from password.')
    parser.add_argument('-nn', '--no_numbers', dest="num",
                        action='store_false',
                        help='Excludes numbers from password.')
    parser.add_argument('-ns', '--no_special', dest="other",
                        action='store_false',
                        help='Excludes miscellaneous characters.')

    args = parser.parse_args()
    psw = Password.Password(args.length, args.chars, args.num, args.other)

    print ">>", psw.get_pass()
