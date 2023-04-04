#!/bin/bash

# NOT TESTED YET... TO BE USED LATER...

# Check if the supplied path/folder exists
check_folder_exists() {
    if [ -d $1 ]; then
        return 0
    else
        return 1
    fi
}

# Check if the supplied file name exists
check_file_exists() {
    if [ -e $1 ]; then
        return 0
    else
        return 1
    fi
}