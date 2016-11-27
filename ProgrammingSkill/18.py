#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/27

from optparse import OptionParser

import sys,os

def opt():
    parser = OptionParser("Usage:%prog [file1] [file2]...")

    parser.add_option('-c', '--char',
                      dest='chars',
                      action='store_true',
                      default=False,
                      help='only count chars')

    parser.add_option('-w', '--word',
                      dest='words',
                      action='store_true',
                      default=False,
                      help='only count words')

    parser.add_option('-l', '--line',
                      dest='lines',
                      action='store_true',
                      default=False,
                      help='only count lines')

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
        total_lines, total_words, total_chars = 0, 0, 0
        for fn in agrs:
            if os.path.isfile(fn):
                with open(fn) as fd:
                    data = fd.read()
                lines, words, chars = get_count(data)
                print_wc(options, lines, words, chars, fn)
                total_lines += lines
                total_words += words
                total_chars += chars
            elif os.path.isdir(fn):
                # print "%s: is a directory" % fn
                print >> sys.stderr, "%s: is a directory" % fn
                # sys.stderr.write("%s: is a directory\n" % fn)

            else:
                # print "%s: No such file or directory" % fn
                # print >> sys.stderr, "%s: No such file or directory" % fn
                sys.stderr.write("%s: No such file or directory\n" % fn)

        if len(args) > 1:
            print_wc(options, total_lines, total_words, total_chars, 'total')

    else:
        data = sys.stdin.read()
        fn = ''
        lines, words, chars = get_count(data)
        print_wc(options, lines, words, chars, fn)

if __name__ == '__main__':
    main()