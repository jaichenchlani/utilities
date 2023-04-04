#!/bin/bash

# Function to execute a bash command with timeout
# Arguments expected:
# $1(mandatory): command to execute
# $2(optional): timeout in secs. Default is set to 3s

execute_command() {
    # Command to execute is a mandatory parameter
    if [ -z "$1" ]; then
        e_error "Command is a mandatory parameter. Aborting."
        exit 1
    else
        execute_command=$1
    fi
    # Evaluate whether the 2nd argument is provided
    if [ -z "$2" ]; then
        command_timeout=$default_timeout
    else
        # Validate for integers only.
        if [[ $2 =~ [^0-9] ]]; then
            # Invalid value. Warn the user, and proceed with default value.
            e_warning "Only integers allowed for the timeout parameter; proceeding with the default $default_timeout sec."
            command_timeout=$default_timeout
        else
            command_timeout=$2
        fi
    fi
   
    # Execute the command with timout
    e_warning "Executing '$execute_command' with timeout $command_timeout sec..."
    timeout $command_timeout $execute_command
    EXIT_STATUS=$?
    case $EXIT_STATUS in
        0)
            e_success "Command execution successful."
            ;;
        124)
            e_error "Timed out."
            ;;
        *)
            e_error "Failed with exit status $EXIT_STATUS."
    esac
}