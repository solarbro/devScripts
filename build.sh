#if there are args
if [ "$#" -ne 0 ]
then
    if [ "$1" = "clang" -o "$1" = "gnu" ]
    then
        # echo "Going to build with clang"
        # shift
        sh ./args.sh "$@"
    # elif [ "$1" = "gnu" ]
    # then
    #     shift
    #     sh ./gnu_args.sh "$@"
    else
        echo "Invalid command \"$1\". \nValid commands are \"clang\" and \"gnu\""
    fi
#if there are no args
else
    echo "No arguments were passed"
    echo "Use \"clang\" to compile using clang. e.g. build clang"
    echo "Use \"gnu\" to compile using g++. e.g. build gnu"
fi
