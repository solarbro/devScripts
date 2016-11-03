from os import chdir, listdir, path, getcwd

import sys
sys.path.insert(0, 'gitSubscripts')

from colors import bcolors

def print_DirList():
    dirs = filter(path.isdir, listdir('.'))
    for i in range(len(dirs)):
        subDirs = listdir(dirs[i])
        dirname = ""
        if ".git" in subDirs:
            dirname += bcolors.BOLD + bcolors.OKGREEN
        dirname += dirs[i] + bcolors.ENDC
        print(dirname)

################################################################################

def file_browser(start_path):
    from subprocess import check_output

    exit_browser = False
    user_name = check_output('whoami')
    current_path = "/home/" + user_name[:len(user_name)-1] + "/Documents"
    if not len(start_path) == 0:
        current_path = start_path
    try:
        chdir(current_path)
    except OSError:
        print("Invalid path: {}".format(current_path))
        current_path = "/home/" + user_name + "/Documents"
        chdir(current_path)

    folder_opened = False

    while not exit_browser:
        print_DirList()
        user_input = raw_input(bcolors.OKBLUE + bcolors.BOLD + current_path + bcolors.ENDC + "$ ")
        input_list = user_input.split()

        if len(input_list) == 0:
            continue
        elif input_list[0] == "c" or input_list[0] == "cancel":
            exit_browser = True
        elif input_list[0] == "o" or input_list == "open":
            folder_opened = True
            exit_browser = True
        elif input_list[0] == "cd":
            if len(input_list) == 1:
                continue
            else:
                try:
                    chdir(input_list[1])
                except OSError:
                    print("Invalid path")
                    # continue
                # current_path += input_list[1]
        elif input_list[0] == "b" or input_list[0] == "back":
            chdir("..")
        else:
            print("Invalid command {}".format(input_list[0]))

    if folder_opened:
        return getcwd()
    return getcwd()

################################################################################

def project_open():
    exit_open_dialog = False

    while not exit_open_dialog:
        user_input = raw_input("> ")
        input_list = user_input.split()

        if len(input_list) == 0:
            continue
        elif input_list[0] == "recent":
            print("pick from a list of recent projects")
        elif input_list[0] == "browse":
            if len(input_list) > 1:
                return file_browser(input_list[1])
            else:
                return file_browser("")
        elif input_list[0] == "cancel" or input_list[0] == "c":
            exit_open_dialog = True
        else:
            print("Unrecognizd command: {}".format(input_list[0]))

    return ""
    
################################################################################
