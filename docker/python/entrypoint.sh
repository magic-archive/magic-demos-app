#!/bin/bash

# Usage: bash entrypoint.sh <github URL for project> <name of main python file>

echo "Cloning project", $1

git clone https://github.com/magic-archive/$1 /project

cd /project

echo "Running project"
echo ""

python command_prompt_todo_list.py

echo "Type exit to restart the demo"
bash
