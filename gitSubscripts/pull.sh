#git pull and other stuff

echo "I'm trying to pull from git"
if [ "$#" -eq 0 ]
then
    git pull
elif [ "$1" = "-r" -o "$1" = "--recursive" ]
then
    git pull --recurse-submodules
else
    echo "Invalid argument \"$1\" provided for pulling"
fi
