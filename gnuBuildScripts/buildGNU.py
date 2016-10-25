import os
import subprocess

def build(config):
    if not config == "--debug" and not config == "--release":
        print("Invalid build configuration chosen")
        print("Valid options are \"--debug\" and \"--release\"")
        return

    os.chdir('../')

    if config == "--debug":
        BuildPath = "buildGNU_debug"
        BuildType = "-DCMAKE_BUILD_TYPE=Debug"
    elif config == "--release":
        BuildPath = "buildGNU_release"
        BuildType = "-DCMAKE_BUILD_TYPE=Release"

    if not os.path.exists(BuildPath):
        os.mkdir(BuildPath)

    os.chdir(BuildPath)

    cmakeArgs = ["cmake", BuildType, "-G", "Unix Makefiles", "../src"]
    subprocess.call(cmakeArgs)

    result = subprocess.call('make')
    os.chdir('../devScripts')
    return result
