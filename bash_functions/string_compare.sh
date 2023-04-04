#!/bin/bash

# Input: 3 Arguments
# Argument 1: first string | Mandatory
# Argument 2: second string | Mandatory
# Argument 3: 1 for case sensitive, case insensitive(default)

# Output
# returns "match" if the strings match
# returns "nomatch" if the strings do not match

function string_compare() {
    # Validate Argument | First String
    if [ -z "$1" ]; then
        e_error "String 1 is mandatory."
        e_warning "Please provide the necessary input and try again."
        e_error "Exiting now..."
        echo
        exit 1
    else
        string_1=$1
    fi

    # Validate Argument | Second String
    if [ -z "$2" ]; then
        e_error "String 2 is mandatory."
        e_warning "Please provide the necessary input and try again."
        e_error "Exiting now..."
        echo
        exit 1
    else
        string_2=$2
    fi
    string_1_lower_case=$(echo $string_1 | tr '[A-Z]' '[a-z]')
    string_2_lower_case=$(echo $string_2 | tr '[A-Z]' '[a-z]')
    if [ -z "$3" ]; then
        # Default. Case insensitive
        if [[ "$string_1_lower_case" == "$string_2_lower_case" ]]; then
            echo "match"
        else
            echo "nomatch"
        fi
    else
        if [[ "$string_1" == "$string_2" ]]; then
            echo "match"
        else
            echo "nomatch"
        fi
    fi
 }