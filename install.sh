#!/bin/bash

# Randwal 
# pywal theme randomizer
# © catx0rr | War torrente 2020
# 
# Installer file for randwal

DIR=$(dirname $0)

source $DIR/source/install

banner(){

  banner='

    ____                  __               __
   / __ \____ _____  ____/ /      ______ _/ /
  / /_/ / __ `/ __ \/ __  / | /| / / __ `/ / 
 / _, _/ /_/ / / / / /_/ /| |/ |/ / /_/ / /  
/_/ |_|\__,_/_/ /_/\__,_/ |__/|__/\__,_/_/   
                PYWAL colorscheme randomizer '

echo -e "$banner"
}

install_randwal() {
    core_package
    core_script
    persist_on_reboot

}

main() {
    banner
    echo -e "\nInstalling randwal..\n"
    sleep 1
    install_randwal
    sleep 2
    echo -e "\nDone.\n\nExecute randwal command and ensure that you have .jpg,.png files on your ~/Pictures directory."

}

main
