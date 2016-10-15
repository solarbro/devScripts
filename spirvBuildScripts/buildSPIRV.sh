cd ../
mkdir -p SpirVBinaries
cd shaderSrc
GREEN='\033[0;32m'
DEFAULT='\033[0m'
echo -e "${GREEN}Compiling vertex shaders${DEFAULT}"
for i in *.vert; do
    echo "- Compiling $i"
    glslangValidator -V "$i" -o "../SpirVBinaries/$i.spv"
done
echo -e "${GREEN}Compiling fragment shaders${DEFAULT}"
for i in *.frag; do
    echo "- Compiling $i"
    glslangValidator -V "$i" -o "../SpirVBinaries/$i.spv"
done
