#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-

""" Password Generator Program """

__authors__ = "gerson23 and jbsilva"

import argparse
import random


class Password:

    ''' Class constructor '''
    def __init__(self, size, chars, numbers, others):

        self.size = size
        self.chars = chars
        self.numbers = numbers
        self.others = others

    ''' Returns a random char '''
    def select_char(self):
        if(not self.chars):
            return

        is_caps = random.randint(0, 1)

        if(is_caps):
            return chr(random.randint(65, 90))
        else:
            return chr(random.randint(97, 122))

    ''' Return a random number converted to char '''
    def select_num(self):
        if(not self.numbers):
            return

        return chr(random.randint(48, 57))

    ''' Return an alternate character '''
    def select_others(self):
        if(not self.others):
            return

        return random.choice('@#!&.')

    ''' Chooses type of next character and returns it '''
    def select_next(self):
        opt = random.randint(0, 4)

        if opt == 3:
            return self.select_others()
        elif opt == 2:
            return self.select_num()
        else:
            return self.select_char()

    ''' Create password given the parameters '''
    def get_pass(self):
        psw_ = []

        for i in range(self.size):
            psw_.append(self.select_next())

        return ''.join(psw_)


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
    psw = Password(args.length, args.chars, args.num, args.other)

    print ">>", psw.get_pass()
