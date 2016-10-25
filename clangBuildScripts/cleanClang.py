#! /usr/bin/env python

import os
import shutil

def clean(config):
    os.chdir('../')

    # if config == "--debug":
    BuildPath_debug = "buildClang_debug"
    # elif config == "--release":
    BuildPath_release = "buildClang_release"

    if config == "--debug" or config == "":
        if os.path.exists(BuildPath_debug):
            shutil.rmtree(BuildPath_debug)
        print("Cleaned clang debug build artefacts")

    if config == "--release" or config == "":
        if os.path.exists(BuildPath_release):
            shutil.rmtree(BuildPath_release)
        print("Cleaned clang release build artefacts")

    os.chdir('devScripts')
