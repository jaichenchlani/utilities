#!/bin/bash

# This script should be included in all the scripts across the repo
# Performs the following tasks:
# Load the default config parameters
# Load the utilities

# Load Bash Config
source $UTILITIES/bash_config.sh

# Load Bash Functions
path="$UTILITIES/bash_functions"
files=$(ls $path)
# Load each utility file
for file in ${files[@]}
    do
      source $path/$file
    done
