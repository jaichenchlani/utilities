#!/bin/bash

# Waits for keypress
# Keeps reminding the user every 3mins...

wait_for_keypress() {
  # Review time for user.. 
  echo "Press any key to continue"
  while [ true ] ;
  do
      read -t 3 -n 1
      if [ $? = 0 ] ; then
          break ;
      else
          echo "waiting for the keypress"
      fi
  done
}