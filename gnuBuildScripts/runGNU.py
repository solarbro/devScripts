import os
import subprocess

def run(config, args):

    if config == "--debug":
        ExePath = "../buildGNU_debug/bin64"
    elif config == "--release":
        ExePath = "../buildGNU_release/bin64"

    os.chdir(ExePath)

    Exes = os.listdir('.')

    if len(Exes) == 1:
        appName = "./" + Exes[0]
        appLaunch = [appName] + args
        if config == "--debug":
            print("Launching in GDB")
        elif config == "--release":
            result = subprocess.call(appLaunch)
            print("Program quit with exit code {}".format(result))
    else:
        print("Prompting user for input")

    os.chdir('../../devScripts/')
