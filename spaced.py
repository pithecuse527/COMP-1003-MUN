#!/usr/bin/python

##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 24/05/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  return string with space
##  

def spaced(s):
    new_str = ""
    
    if len(s) == 1:
        return s
    
    if len(s) == 2:
        new_str = s[0] + ' ' +s[-1]
        return new_str
    
    mid = len(s) // 2
    is_even = len(s) % 2 == 0
    
    if is_even:
        new_str += spaced(s[:mid])
        new_str += ' '
        new_str += spaced(s[mid:])
    else:
        new_str += spaced(s[:mid+1])
        new_str += ' '
        new_str += spaced(s[mid+1:])
    
    return new_str
