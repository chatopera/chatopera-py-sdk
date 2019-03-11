#! /bin/bash 
###########################################
#
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)

source ~/venv-py2/bin/activate
# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..
python2 demo.py --verbosity 1 \
    --bot_ip corsair \
    --bot_port 28003 \
    --bot_id saas_5bf266aa6f80090017b40215 
