#! /usr/bin/env python
import sys
from os import chdir, getcwd

sys.path.insert(0, 'gitSubscripts')

from colors import bcolors

import open


app_dir =
exit_app = False

while not exit_app:
    user_input = raw_input(bcolors.BOLD + bcolors.HEADER + "> " + bcolors.ENDC)

    cmd_list = user_input.split()

    if len(cmd_list) == 0:
        continue
    elif cmd_list[0] == "help" or cmd_list[0] == "h":
        print("Helpful text")
    elif cmd_list[0] == "open":
        proj_dir = open.project_open()
        print(os.getcwd())
    elif cmd_list[0] == "quit" or cmd_list[0] == "q":
        exit_app = True
    else:
        print("Unrecognized command: {}".format(cmd_list[0]))

# print("Closing...")
