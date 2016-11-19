#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/16

import os, sys
def print_files(path):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    if files:
        for f in files:
            print os.path.join(path, f)
    if dirs:
        for d in dirs:
            print_files(os.path.join(path, d))

if __name__ == '__main__':
    print_files(sys.argv[1])