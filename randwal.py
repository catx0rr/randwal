#!/usr/bin/python3

from time import sleep
from os import system, listdir
from random import uniform, choice

# If you want a static configuration for your pywal-randwal
# comment out @interval(intervals) on line 75

# Change these values for your customization

directory = '/home/user/Pictures/'              # change user to your username
randsaturate = False                            # Add chromatic saturation randomly
intervals = 1800                                # 30 minutes

# Do not change the code from below

def randfile(directory):
    return choice(listdir(directory))


def changetheme(filename, saturation=False):

    fullpath = directory + filename

    if saturation:
        saturation = round(uniform(0.1, 1.0), 1)
        cmd = '%s %s --saturate %s' % ('wal -q -i', fullpath, saturation)
        preview = '%s' % ('wal --preview')

        print('Changed wallpaper to %s with saturation of %s ' % (filename, saturation))
        system(cmd)
        system(preview)

    else:
        cmd = '%s %s' % ('wal -q -i', fullpath)
        preview = '%s' % ('wal --preview')
        
        print('Change wallpaper to %s with default saturation of %s' % (filename, '0.0'))
        system(cmd)
        system(preview)

def interval(intervaltime):
    
    def real_interval_decorator(function):
        
        def wrapper(*args, **kwargs):
            while True:
                function(*args, **kwargs)
                # Change on user specification
                sleep(intervaltime)
        return wrapper
    return real_interval_decorator

"""
Old decorator function with hardcoded interval
def interval(function):

    # Decorator function for interval calls
    def funcwrapper(*args, **kwargs):      
        while True:
            function(*args, **kwargs)
           # Change in 30 minutes
           sleep(30)
    return funcwrapper
"""

"""
NOTE:

Remove the @interval decorator if you don't want to change 
wallpapers / theme in interval.
"""

@interval(intervals)
def main(directory, saturation):
    filename = randfile(directory)
    changetheme(filename, saturation)


if __name__ == '__main__':
    
    main(directory, randsaturate)

