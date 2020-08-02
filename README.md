# randwal - a simple randomizer script for pywal colorscheme

Have you ever get bored of your terminal colors / vim / wallpaper over and over?

If you are like me then this is for you.

![randwal demo](https://github.com/catx0rr/randwal/blob/master/img/randwal.gif)

Monochromatic colors works best for minimal wallpapers.

# Requirements
---
- A unix-like machine
- Python3.6+
- [pywal](https://github.com/catx0rr/randwal#pywal-installation-core-package) and [dependencies](https://github.com/catx0rr/randwal#dependencies)
- DE: gnome, xfce  
- WM: i3, i3gaps

You may check pywal documentations for more info

# More Screenshots
---
View more [here](https://github.com/catx0rr/randwal/tree/master/screenshots)

# Installation (Manual)
---

Just copy randwal to your bin local directory. Ensure to rename copy it to randwal (without .py)
```
cp randwal.py ~/.local/bin/randwal
```
Change the user in config/randwal.desktop and copy it in autostart.
```
/home/your_username/.local/bin/randwal
cp config/randwal.desktop ~/.config/autostart/randwal.desktop
```

Testing the script on your terminal. (Make sure there are .jpg, .png files inside ~/Pictures/ directory)
```
$ randwal &
```

# Installation (script)
---

Just run the shell script
```
chmod u+x install.sh
./install.sh
```

---
FAQS
---
### I want to change the default time of 30 minutes.

Edit ~/.local/bin/randwal and set intervals to whatever time you like in seconds.

### I want to change the default directory where should I look?

Same thing. all config variables are inside the randwal script. Edit ~/.local/bin/randwal

### I want to change the tone of the monochromatic colors of my terminal?

There is no specific option for that, but it can randomly change in ~/.local/bin/randwal randsaturate set to True.

### My vim colors is not changing whenever randwal / pywal changes its colors. What should I do?

Google. Nah, all you need to do is to install the [vim plugin](https://github.com/dylanaraps/wal.vim) manually or your favorite vim plugin manager.

### How do I make the script run after I reboot?

Tried to do a cronjob but it didn't work. I do not want to complicate things and  I found a simple solution for this issue. Copy the randwal.desktop file and put it on your autostart. Make sure you change the user to your username inside the config.

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
on your .rc file, copy the path and add it along with the /home/user/.local/bin path.

export PATH=$PATH:/home/user/.local/bin
```

---
# Pywal Installation (core package)
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

Pywal doesn't come with imagemagick and some other dependencies. In order to generate colors, install it by executing this command.
```
    sudo apt install -y imagemagick hsetroot nitrogen
```

Arch:
```
    pacman -S imagemagick hsetroot nitrogen
```

Fedora / RedHat:
```
    dnf install -y imagemagick hsetroot nitrogen
```

# Pywal Usage and Configuration setup for randwal
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
```

# Pywal Troubleshooting
---
Check the [official repository of pywal](https://github.com/dylanaraps/pywal)
