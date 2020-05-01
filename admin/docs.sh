#! /bin/bash 
###########################################
# Generate docs
# https://pypi.org/project/pydoc-markdown/
# pip install pydoc-markdown
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
export PYTHONUNBUFFERED=1
export PATH=/opt/miniconda3/envs/venv-py3/bin:$PATH

# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/../app
pydocmd simple chatopera.chatbot++ > api.md
