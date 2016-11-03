
from subprocess import Popen

from colors import bcolors

def pull(repo, branch, otherArgs):
    #TODO: Find a way to list repos and branches so user can specify them
    print(otherArgs)
    proc = Popen(['git', 'pull', repo, branch])
    proc.wait()

def pull_recursive():
    print("meh")

def fetch():
    print("fetching")

def update(proj_name):
    exit_update = False

    repository = "origin"
    branch = "master"

    while not exit_update:
        user_input = raw_input(bcolors.BOLD + bcolors.OKGREEN + proj_name + bcolors.OKBLUE + ":~/update" + bcolors.ENDC + "$ ")
        input_list = user_input.split()

        if len(input_list) == 0:
            continue
        elif input_list[0] == "help" or input_list[0] == "h":
            print("Some helpful message about pulling")
        elif input_list[0] == "q" or input_list[0] == "quit":
            exit_update = True
        elif input_list[0] == "pull":
            pull(repository, branch, input_list[1:])
        elif input_list[0] == "fetch":
            fetch()
        else:
            print("Unrecognized command: {}".format(input_list[0]))
