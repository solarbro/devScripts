#! /usr/bin/env python

# import argparse
from subprocess import check_output, CalledProcessError
import sys

sys.path.insert(0, 'gitSubscripts')

import git_submit
import git_update
from colors import bcolors
try:
    remote_name = check_output(['git', 'config', '--local', 'remote.origin.url'])
except CalledProcessError:
    print("Error: The current directory isn't part of a git repository")
    quit()

namestart = remote_name.rfind('/')
nameend = remote_name.rfind('.')
userStart = remote_name.rfind('/', 0, namestart-1)
proj_name = remote_name[namestart+1:nameend]
user_name = remote_name[userStart+1:namestart]
# print(remote_name[namestart+1:nameend])

user_exit = False

console = user_name + "/" + proj_name

while not user_exit:
    #app logic
    user_input = raw_input(bcolors.BOLD + bcolors.OKGREEN + console + bcolors.ENDC + "$ ")
    input_list = user_input.split()

    if len(input_list) == 0:
        continue
    elif input_list[0] == "help" or input_list[0] == "h":
        print("Some nice help message")
    elif input_list[0] == "quit" or input_list[0] == "q":
        user_exit = True
    elif input_list[0] == "log":
        print("Run log app")
    elif input_list[0] == "submit":
        git_submit.submit(console)
    elif input_list[0] == "update":
        git_update.update(console)
    else:
        print("Unrecognized command: {}".format(input_list[0]))
