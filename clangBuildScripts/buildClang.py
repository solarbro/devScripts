#! /usr/bin/env python

import os
import subprocess

# print(os.getcwd())
def build(config):
    # d = os.path.dirname('buildClang_debug')
    if not config == "--debug" and not config == "--release":
        print("Invalid build configuration chosen")
        print("Valid options are \"--debug\" and \"--release\"")
        return

    os.chdir('../')

    if config == "--debug":
        BuildPath = "buildClang_debug"
        BuildType = "-DCMAKE_BUILD_TYPE=Debug"
    elif config == "--release":
        BuildPath = "buildClang_release"
        BuildType = "-DCMAKE_BUILD_TYPE=Release"

    if not os.path.exists(BuildPath):
        os.mkdir(BuildPath)

    os.chdir(BuildPath)

    cmakeArgs = ["cmake", "-DCMAKE_CXX_COMPILER=clang++", "-DCMAKE_C_COMPILER=clang", BuildType, "-G", "Unix Makefiles", "../src"]
    subprocess.call(cmakeArgs)

    result = subprocess.call('make')
    os.chdir('../devScripts')
    return result
