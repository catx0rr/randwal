# randwal
pywal randomizer for your setup customization

Have you ever getting bored of your terminal colors / background over and over?

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

Create a 'sh' directory and copy pywal.sh
```
mkdir ~/.local/sh
cp pywal.sh ~/.local/sh/
```

Copy randwal to your bin local directory
```
cp randwal ~/.local/bin/
```

Testing the script on your terminal. (Make sure there are .jpg, .png files inside ~/Pictures/ directory)
```
$ randwal &
```

FAQS
---
### I want to change the default time of 30 minutes.

edit ~/.local/bin/randwal and set intervals to whatever time you like in seconds.

### I want to change the default directory where should I look?

same thing. all config variables are inside the randwal script. edit ~/.local/bin/randwal

### I want to change the monochromatic colors of the wallpaper?

there is no specific option for that, but you can change it randomly in ~/.local/bin/randwal randsaturate set to True.

### I want to customize my vim to get the same colors as my terminal what should I do?

google. Nah, all you need to do is to install the [vim plugin](https://github.com/dylanaraps/wal.vim) by the same colorscheme developer.

### How do I make the script run after I reboot?

the answer is trivial, you need to create a cron job.

create a cron job and add this line (Change the user to your username)
```
@reboot /home/user/.local/sh/pywal.sh
```
and then call the pywal.sh script.

create a 'sh' directory and copy pywal.sh
```
mkdir ~/.local/sh
cp pywal.sh ~/.local/sh/
```

### When I close the terminal, the randwal script process is getting terminated, what should I do?

verify first the process by executing this command
```
ps aux | grep randwal
```

if there are no processes, create one by executing this command or you may check this [blog](https://janakiev.com/blog/python-background/)
```
nohup ~/.local/bin/randwal > /tmp/nohup.log &
```

close the terminal and check the process
```
ps aux | grep randwal
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

# Usage
---
Change color scheme and terminal colors.
```
wal -i /path/to/wallpaper.png
```

Pywal is not persistent on reboot execute commands upon logging in.
```
wal -R
```

Make it persistent on reboot (Add this to your .bashrc, .zshrc, .anyshrc)
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

Create a cron job and add this line (Change the user to your username)
```
@reboot /home/user/.local/sh/pywal.sh
```

Create a 'sh' directory and copy pywal.sh
```
mkdir ~/.local/sh
cp pywal.sh ~/.local/sh
```

# Pywal Troubleshooting
---
Check the [official repository of pywal](https://github.com/dylanaraps/pywal)
