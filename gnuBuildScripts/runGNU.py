import os
import subprocess
from shutil import copy2

def run(config, args):

    if config == "debug":
        ExePath = "../buildGNU_debug/bin64"
        #create gdbinit script
        copy2('gdbInit/gdbinit', '../buildGNU_debug/bin64/.gdbinit')
        gdbRunCommand = 'run ' + " ".join(args)
        #add run command
        with open('../buildGNU_debug/bin64/.gdbinit', 'a') as file:
            file.write(gdbRunCommand)
    elif config == "release":
        ExePath = "../buildGNU_release/bin64"

    os.chdir(ExePath)

    Exes = os.listdir('.')
    while len(Exes) > 0 and Exes[0][0] == '.':
        Exes.pop(0)

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

        appName = "./" + Exes[appSelect -1]
        appLaunch = [appName] + args

    if config == "debug":
        gdbLaunch = ['gdb', '-iex', "add-auto-load-safe-path .gdbinit", appName]
        result = subprocess.call(gdbLaunch)
    elif config == "release":
        result = subprocess.call(appLaunch)
        print("Program quit with exit code {}".format(result))
    os.chdir('../../devScripts/')
