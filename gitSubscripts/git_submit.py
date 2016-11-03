#! /usr/bin/env python
from subprocess import Popen

from colors import bcolors

def file_list(list_options):
    print(list_options)
    if len(list_options) == 0 or list_options[0] == "all":
        print("list all files")
    elif list_options[0] == "modified":
        print("modified files")
    elif list_options[0] == "untracked":
        print("Untracked files")


def submit(proj_name):
    exit_submit = False
    commit_message = ""

    while not exit_submit:
        user_input = raw_input(bcolors.BOLD + bcolors.OKGREEN + proj_name + bcolors.OKBLUE + ":~/submit" + bcolors.ENDC + "$ ")
        input_list = user_input.split()

        if len(input_list) == 0:
            continue
        elif input_list[0] == "help" or input_list[0] == "h":
            print("Some helpful message")
        elif input_list[0] == "cancel" or input_list[0] == "quit" or input_list[0] == "q":
            exit_submit = True
        elif input_list[0] == "list":
            file_list(input_list[1:])
        elif input_list[0] == "message" or input_list[0] == "m":
            msg = user_input.split(" ", 1)
            if(len(msg) > 1):
                commit_message = msg[1]
        elif input_list[0] == "add":
            print("files to add", input_list[1:])
        else:
            print("Unrecognized command: {}".format(input_list[0]))
