#! /bin/bash 
###########################################
#
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)

# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..
if [ -f .env ]; then
    source .env
else
    echo `pwd`"/.env file not exist."
    echo "Copy "`pwd`"/sample.env as"`pwd`"/.env and modify it." 
    exit 1
fi

python demo.py
