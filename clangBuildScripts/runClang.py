import os
import subprocess

def run(config, args):
    print("Running Clang executable")
    print(config)
    for a in args:
        print(a)

    if config == "--debug":
        ExePath = "../buildClang_debug/bin64"
    elif config == "--release":
        ExePath = "../buildClang_release/bin64"

    os.chdir(ExePath)

    Exes = os.listdir('.')

    if len(Exes) == 1:
        appName = "./" + Exes[0]
        appLaunch = [appName] + args
    else:
        print("Prompting user for input")

        for i in range(len(Exes)):
            print("{}. {}".format(i + 1, Exes[i]))

        appSelect = int(raw_input("Select executable to run: "))
        while appSelect <= 0 or appSelect > len(Exes):
            print("Invalid selection. Selection must be in the range [1,{}]".format(len(Exes)))
            appSelect = int(raw_input("Select executable to run: "))

        appName = "./" + Exes[appSelect - 1]
        appLaunch = [appName] + args

    if config == "--debug":
        print("Launching in GDB")
    elif config == "--release":
        result = subprocess.call(appLaunch)
        print("Program quit with exit code {}".format(result))
    os.chdir('../../devScripts/')
