#!/bin/bash

# Randwal 
# pywal theme randomizer
# © catx0rr | War torrente 2020
# 
# Installer file for randwal

DIR=$(dirname $0)

source $DIR/source/install

install_randwal() {
    core_package
    core_script
    persist_on_reboot

}

main() {
    echo "Installing randwal.."
    sleep 1
    install_randwal
    sleep 2
    echo -e "Done.\nExecute randwal command and ensure that you have .jpg,.png files on your ~/Pictures directory."

}

main
