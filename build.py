#! /usr/bin/env python

import argparse
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
#            Parse switches               #
###########################################

###########################################
#                  HELP                   #
###########################################
def printHelpMsg():
    print("Recognized compiler names are \"clang\" or \"gnu\"")

def printBuildConfigHelp():
        print("Valid options are \"--debug\" and \"--release\"")

###########################################
#             Clang options               #
###########################################
def clangOptions():
    # print(sys.argv[2:])
    if argsList.clean:
        cleanClang.clean(argsList.config)
    buildResult = buildClang.build(argsList.config)
    if buildResult == 0:
        if argsList.run:
            runClang.run(argsList.config, argsList.args)
    else:
        print("Build failed")
###########################################
#              GNU options                #
###########################################
def gnuOptions():
    if argsList.clean:
        cleanGNU.clean(argsList.config)
    buildResult = buildGNU.build(argsList.config)
    if buildResult == 0:
        if argsList.run:
            runGNU.run(argsList.config, argsList.args)
    else:
        print("Build failed")


#init args list
parser = argparse.ArgumentParser(description='Build project')
parser.add_argument("-b", "--compiler", type=str, help="Specify compiler. Use either \"clang\" or \"gnu\"", required=True, default=None)
parser.add_argument("-c", "--config", type=str, help="use \"release\" or \"debug\" configuration", required=True, default=None)
parser.add_argument("--rebuild", help="clean and rebuild project", dest="clean", action="store_const", const=True, default=False, required=False)
parser.add_argument("--run", dest="run", help="run project executable if build succeeds", action="store_const", const=True, default=False, required=False)
parser.add_argument("-a", "--args", type=str, help="pass arguments to the application when using the \"--run\" switch.", nargs='+', required=False, default=[])
argsList = parser.parse_args();

if argsList.compiler == "clang":
    # print("Building with clang")
    clangOptions()
elif argsList.compiler == "gnu":
    # print("Building with gnu")
    gnuOptions()
else:
    print("Unrecognized compiler: {}".format(argsList.compiler))
    printHelpMsg()
