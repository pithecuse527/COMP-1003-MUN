#!/usr/bin/python

##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 24/05/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  return string with space
##  

# as the function requires only one parmeter, use global var
# or we can use a nested function... (will be more safe)
walker = 1

def spaced(s):
    global walker
    
    if walker >= len(s):
        walker = 1
        return s
    
    s = s[:walker] + ' ' + s[walker:]
    walker += 2
    return spaced(s)
