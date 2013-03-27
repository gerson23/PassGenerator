#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-

""" Password Generator Program """

__authors__ = "gerson23 and jbsilva"

import sys
import argparse
import random


class Password:
    ''' Class constructor '''
    def __init__(self, size, chars, numbers, others):
        self.size = size
        self.opts = []

        if chars:
            self.opts.append('c')
        if numbers:
            self.opts.append('n')
        if others:
            self.opts.append('o')

    ''' Returns a random char '''
    def select_char(self):
        is_caps = bool(random.getrandbits(1))

        if is_caps:
            return chr(random.randrange(65, 91))
        else:
            return chr(random.randrange(97, 123))

    ''' Return a random number converted to char '''
    def select_num(self):
        return chr(random.randrange(48, 58))

    ''' Return an alternate character '''
    def select_others(self):
        return random.choice('_$+=-~()@#!&.|')

    ''' Chooses type of next character and returns it '''
    def select_next(self):
        # The verification that 'opts' is not empty was made in main()
        opt = random.choice(self.opts)
        if opt == 'o':
            return self.select_others()
        elif opt == 'n':
            return self.select_num()
        else:
            return self.select_char()

    ''' Create password given the parameters '''
    def get_pass(self):
        psw_ = []

        for i in range(self.size):
            psw_.append(self.select_next())

        return ''.join(psw_)


def main():
    parser = argparse.ArgumentParser(description='Password Generator Program.',
                                     epilog='This program generates passwords')
    parser.add_argument('-l', '--length', type=int, default=10,
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

    if not (args.chars or args.num or args.other):
        print "You can't combine all the options!"
        return 1
    else:
        psw = Password(args.length, args.chars, args.num, args.other)
        print ">>", psw.get_pass()
        return 0


if __name__ == "__main__":
    sys.exit(main())
