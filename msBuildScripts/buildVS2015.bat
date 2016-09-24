cls
cd ../
mkdir buildMSVC
cd buildMSVC
cmake -G"Visual Studio 14 2015 Win64" ../src -DCMAKE_BUILD_TYPE="Debug;Release;RelWithDebInfo" >> ..\buildScripts\cmakeoutput.log > ..\buildScripts\cmakeoutput.log
cd ../buildScripts
start notepad++ cmakeoutput.log
