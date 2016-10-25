#! /usr/bin/env python

# print("I'm trying to clean")

import sys
sys.path.insert(0, 'clangBuildScripts')
sys.path.insert(0, 'gnuBuildScripts')

import cleanClang
import cleanGNU

if len(sys.argv) < 2:
    cleanClang.clean("")
    cleanGNU.clean("")
else:
    if sys.argv[1] == "clang":
        if len(sys.argv) > 2:
            cleanClang.clean(sys.argv[2])
        else:
            cleanClang.clean("")
    elif sys.argv[1] == "gnu":
        if len(sys.argv) > 2:
            cleanGNU.clean(sys.argv[2])
        else:
            cleanGNU.clean("")
    else:
        print("Invalid argument")
        print("Valid arguments are \"clang\" and \"gnu\"")
