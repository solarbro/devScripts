#helper script for handling git stuff
echo "I want to git"

#update
if [ "$1" = "update" -o "$1" = "pull" ]
then
    shift
    sh subscripts/pull.sh "$@"

#commit (main / submodules / subtrees)
elif [ "$1" = "commit" ]
then
    shift
    sh subscripts/commit.sh "$@"

#stage (stage files)
elif [ "$1" = "stage" ]
then
    shift
    sh subscripts/stage.sh "$@"

#push
elif [ "$1" = "push" ]
then
    shift
    sh subscripts/push.sh "$@"

elif [ "$1" = "submodule" ]
then
    shift
    sh subscripts/submodule.sh "$@"

#log
elif [ "$1" = "log" ]
then
    git log

else
    echo "Invalid command \"$1\""
fi
