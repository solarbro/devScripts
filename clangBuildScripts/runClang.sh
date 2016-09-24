#Run executable\n
# echo "Running compiled app"

#print text function
function print
{
    echo -e "$1"
    echo  "-------------------------------------"
    echo  "$2"
    echo -e "$3"
}

RED='\033[0;31m'
NC='\033[0m' # No Color

arr=($(ls ../buildClang/bin64/))
# echo "${arr[@]}"
#if theres only one executable, run it

if [ "${#arr[@]}" -eq 1 ]
then
    print ${RED} "Starting Application" ${NC}
    ../buildClang/bin64/${arr[0]} "$@"
    # wait
    print ${RED} "Application quit with exit code $?" ${NC}
    # exit $?
else
    #TODO: Prompt user when there are multiple executables
    echo "Prompting for app selection"
    for i in `seq 1 ${#arr[@]}`;
    do
        echo "$i. ${arr[i-1]}"
    done
fi
