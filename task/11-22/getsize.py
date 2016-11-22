#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/22

from optparse import OptionParser

import sys,os

def opt():
    parser = OptionParser("Usage:%prog [file1] [file2]...")

    parser.add_option('-H', '--readonly',
                      dest='readonly',
                      action='store_true',
                      default=False,
                      help='open file readonly')

    options, agrs = parser.parse_args()
    return options, agrs

def get_count(data):
    chars = len(data)
    words = len(data.split())
    lines = data.count('\n')
    return lines, words, chars

def print_wc(options, lines, words, chars, fn):
    if options.lines:
        print lines,

    if options.words:
        print words,

    if options.chars:
        print chars,
    print fn

def main():
    options, args = opt()
    if not (options.lines or options.words or options.chars):
        options.lines, options.words, options.chars = True, True, True

    if args:
        fn = args[0]
        with open(fn) as fd:
            data = fd.read()
        lines, words, chars = get_count(data)
        print_wc(options, lines, words, chars, fn)

    else:
        data = sys.stdin.read()
        fn = ''
        lines, words, chars = get_count(data)
        print_wc(options, lines, words, chars, fn)

if __name__ == '__main__':
    main()