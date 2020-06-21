#!/bin/bash

# Static Theme

## If the theme is static uncomment this line
#$HOME/.local/bin/wal -R

# Dynamic Theme

## If static theme is selected, comment this out.
$HOME/.local/bin/randwal

# Debugger:
## If dynamic reboot is not working, comment it out and uncomment the next line
#nohup ~/.local/bin/randwal > /tmp/nohup.log &
