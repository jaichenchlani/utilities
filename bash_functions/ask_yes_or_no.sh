#!/bin/bash

# Returns a "yes" only if 'y' or 'Y' is pressed.
# Else, returns "no"

function ask_yes_or_no() {
    read -p "$1 ([y]es or [N]o): "
    case $(echo $REPLY | tr '[A-Z]' '[a-z]') in
        y|yes) echo "yes" ;;
        *)     echo "no" ;;
    esac
}