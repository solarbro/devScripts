#! /usr/bin/env python

import sys
import subprocess

sys.path.insert(0, 'clangBuildScripts')
sys.path.insert(0, 'gnuBuildScripts')

import buildClang
import cleanClang
import runClang
import buildGNU
import cleanGNU
import runGNU

# print("I'm trying to build")

###########################################
#                  HELP                   #
###########################################
def printHelpMsg():
    print("[List of allowed arguments]")

def printBuildConfigHelp():
        print("Valid options are \"--debug\" and \"--release\"")

###########################################
#             Clang options               #
###########################################
def clangOptions():
    # print(sys.argv[2:])
    if len(sys.argv) < 3:
        print("No build configurations provided")
        printBuildConfigHelp()
    else:
        RunExecutable = False
        if len(sys.argv) > 3:
            if sys.argv[3] == "--rebuild":
                cleanClang.clean(sys.argv[2])
            elif sys.argv[3] == "--run":
                RunExecutable = True
            else:
                print("Unknown secondary argument {}".format(sys.argv[3]))
        buildResult = buildClang.build(sys.argv[2])
        if RunExecutable:
            if buildResult == 0:
                runClang.run(sys.argv[2], sys.argv[4:])
            else:
                print("Build failed")
###########################################
#              GNU options                #
###########################################
def gnuOptions():
    RunExecutable = False
    if len(sys.argv) < 3:
        print("No build configurations provided")
        printBuildConfigHelp()
    else:
        if len(sys.argv) > 3:
            if sys.argv[3] == "--rebuild":
                cleanGNU.clean(sys.argv[2])
            elif sys.argv[3] == "--run":
                RunExecutable = True
            else:
                print("Unknown secondary argument {}".format(sys.argv[3]))
        buildResult = buildGNU.build(sys.argv[2])
        if RunExecutable:
            if buildResult == 0:
                runGNU.run(sys.argv[2], sys.argv[4:])
            else:
                print("Build failed")


if len(sys.argv) == 1:
    print("No arguments provided")
    printHelpMsg()
else:
    if sys.argv[1] == "--help":
        # print("Build help")
        printHelpMsg()
    elif sys.argv[1] == "clang":
        # print("Building with clang")
        clangOptions()
    elif sys.argv[1] == "gnu":
        # print("Building with gnu")
        gnuOptions()
    else:
        print("Unrecognized arguments")
        printHelpMsg()
