import os
import shutil

def clean(config):
    os.chdir('../')

    BuildPath_debug = "buildGNU_debug"
    BuildPath_release = "buildGNU_release"

    if config == "debug" or config == "":
        if os.path.exists(BuildPath_debug):
            shutil.rmtree(BuildPath_debug)
        print("Cleaned gnu debug build artefacts")

    if config == "release" or config == "":
        if os.path.exists(BuildPath_release):
            shutil.rmtree(BuildPath_release)
        print("Cleaned gnu release build artefacts")

    os.chdir('devScripts')
