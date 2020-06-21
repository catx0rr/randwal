# randwal
pywal randomizer for your setup customization

Have you ever getting bored of your terminal colors / vim / wallpaper over and over?

If you are like me then this is for you.

![pywal_colorscheme](https://github.com/catx0rr/randwal/blob/master/screenshots/sample.png)

# Requirements
---
- A nix machine
- Python3.6+
- pywal and imagemagick
- Your brain

# More Screenshots
---
View more [here](https://github.com/catx0rr/randwal/tree/master/screenshots)

# Installation (randwal)
---

Just copy randwal to your bin local directory. Ensure to rename copy it to randwal (without .py)
```
cp randwal.py ~/.local/bin/randwal
```

Testing the script on your terminal. (Make sure there are .jpg, .png files inside ~/Pictures/ directory)
```
$ randwal &
```

FAQS
---
### I want to change the default time of 30 minutes.

Edit ~/.local/bin/randwal and set intervals to whatever time you like in seconds.

### I want to change the default directory where should I look?

Same thing. all config variables are inside the randwal script. edit ~/.local/bin/randwal

### I want to change the monochromatic colors of the wallpaper?

There is no specific option for that, but you can change it randomly in ~/.local/bin/randwal randsaturate set to True.

### I want to customize my vim to get the same colors as my terminal what should I do?

Google. Nah, all you need to do is to install the [vim plugin](https://github.com/dylanaraps/wal.vim) manually or your favorite vim plugin manager.

### How do I make the script run after I reboot?

I tried a cronjob for user on this but it failed, I found a simple solution on this. Copy the randwal.desktop file and put it on your autostart. Make sure you change the user to your username.
```
cp config/randwal.desktop ~/.config/autostart/
```

### When I run randwal manually on terminal, and close it, the randwal script process is getting terminated. What should I do?

Verify first the process by executing this command
```
ps aux | grep randwal
```

If there are no processes, create one by executing this command or you may check this [blog](https://janakiev.com/blog/python-background/)
```
nohup ~/.local/bin/randwal > /tmp/nohup.log &
```

Close the terminal and check the process
```
ps aux | grep randwal
```

### randwal issue, command not found!

make sure that you have .local/bin directory if none create one and add this command to your .bashrc, .zshrc, ,anyshrc file..
```
on your terminal:
$ echo $PATH

on your .rc file, copy the path and add it along with the /home/user/.local/bin path.
export PATH=/your/copied/path:/home/user/.local/bin
```

---
# pywal Installation (core package)
---
### System-wide install (sudo)
```
    pip3 install pywal
```
### User install (No sudo)
```
    pip3 install --user pywal
```

# Dependencies
---
Debian / Ubuntu Distros:

Pywal doesn't come with imagemagick, to generate colors install it by executing this command
```
    sudo apt install -y imagemagick
```

Arch:
```
    pacman -S imagemagick
```

Fedora / RedHat:
```
    dnf install -y imagemagick
```

# Pywal Usage and Configuration setup to work with randwal accordingly
---
Change color scheme and terminal colors.
```
wal -i /path/to/wallpaper.png
```

Pywal is not persistent on reboot execute commands upon logging in.
```
wal -R
```

Make pywal it persistent on reboot (Add this to your .bashrc, .zshrc, .anyshrc)
```
import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
(cat ~/.cache/wal/sequences &)

# To add support for TTYs this line can be optionally added.
source ~/.cache/wal/colors-tty.sh
# Troubleshooting

for more documentation kindly check pywal [official repository](https://github.com/dylanaraps/pywal)
```

# Pywal Troubleshooting
---
Check the [official repository of pywal](https://github.com/dylanaraps/pywal)
