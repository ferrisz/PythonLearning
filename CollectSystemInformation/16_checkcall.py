#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2016/11/29

import subprocess

try:
    subprocess.check_call('exit 1', shell=True)
except subprocess.CalledProcessError:
# except Exception:
    pass
