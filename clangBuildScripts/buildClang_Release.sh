cd ../
mkdir -p buildClang
cd buildClang
cmake -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_C_COMPILER=clang -DCMAKE_BUILD_TYPE=Release -G "Unix Makefiles" ../src
make
exit $?