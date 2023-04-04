#!/bin/bash

# Check previous command return code. Exit if not successful.
check_previous_command_status() {
    if [ $? -ne 0 ]; then
        e_error "Failed. Aborting."
        exit 1
    fi
}