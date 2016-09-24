#parse clang args
################################################
#                    HELP                      #
################################################
if [ "$2" = "--help" ]
then
    echo "help"
################################################
#            Build in debug mode               #
################################################
elif [ "$2" = "--debug" ]
then
    echo "Build in debug mode"
    if [ "$1" = "clang" ]
    then
        sh clangBuildScripts/buildClang_Debug.sh
    elif [ "$1" = "gnu" ]
    then
        sh gnuBuildScripts/buildGCC_Debug.sh
    fi
################################################
#            Build in release mode             #
################################################
elif [ "$2" = "--release" ]
then
    echo "Build in release mode"
    if [ "$1" = "clang" ]
    then
        sh clangBuildScripts/buildClang_Release.sh
    elif [ "$1" = "gnu" ]
    then
        sh gnuBuildScripts/buildGCC_Release.sh
    fi
################################################
#            Clean build artefacts             #
################################################
elif [ "$2" = "clean" ]
then
    if [ "$1" = "clang" ]
    then
        sh clangBuildScripts/cleanClang.sh
    elif [ "$1" = "gnu" ]
    then
        sh gnuBuildScripts/cleanGCC.sh
    fi
    echo "Cleaned "$1" build artefacts"
################################################
#                Build and run                 #
################################################
elif [ "$2" = "run" ]
then
    #######################################
    #           build in debug            #
    #######################################
    if [ "$3" = "--debug" ]
    then
        # echo "build and run debug"
        if [ "$1" = "clang" ]
        then
            sh clangBuildScripts/buildClang_Debug.sh
        elif [ "$1" = "gnu" ]
        then
            sh gnuBuildScripts/buildGCC_Debug.sh
        fi
        if [ "$?" -eq 0 ]
        then
            if [ "$1" = "clang" ]
            then
                shift; shift; shift
                sh clangBuildScripts/runClang.sh "$@"
            elif [ "$1" = "gnu" ]
            then
                shift; shift; shift
                sh gnuBuildScripts/rungnu.sh "$@"
            fi
        else
            echo -e "${RED}Build failed${NC}"
        fi
    #######################################
    #           build in release          #
    #######################################
    elif [ "$3" = "--release" ]
    then
        # echo "build and run release"
        if [ "$1" = "clang" ]
        then
            sh clangBuildScripts/buildClang_Release.sh
        elif [ "$1" = "gnu" ]
        then
            sh gnuBuildScripts/buildGCC_Release.sh
        fi
        if [ "$?" -eq 0 ]
        then
            shift; shift; shift
            if [ "$1" = "clang" ]
            then
                sh clangBuildScripts/runClang.sh "$@"
            elif [ "$1" = "gnu" ]
            then
                sh gnuBuildScripts/rungnu.sh "$@"
            fi
        else
            echo -e "${\033[0;31m}Build failed${\033[0m}"
        fi
    #######################################
    #           Invalid argument          #
    #######################################
    else
        if [ "$#" -eq 2 ]
        then
            echo "No arguments were given for run"
        else
            echo "Invalid command \"$3\""
        fi
        echo "Available commands are \"--debug\" and \"--release\""
    fi
################################################
#              Invalid argument                #
################################################
else
    if [ "$#" -eq 1 ]
    then
        echo "No arguments were provided for the compiler"
    else
        echo "Invalid command \"$2\""
    fi
    echo "Use --help for available commands"
fi
