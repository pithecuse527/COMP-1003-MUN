#!/usr/bin/python

##  Assignment-201948932
##  
##  Created by Hong Geun Ji on 24/05/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  return string with space
##  

def spaced(s):
    '''
        Returning the string contains space between each character
        Time complexity: O(n)
    '''
    new_str = ""
    
    # base case1
    if len(s) == 1:
        return s
    
    # base case2
    if len(s) == 2:
        new_str = s[0] + ' ' +s[-1]
        return new_str
    
    mid = len(s) // 2
    is_even = len(s) % 2 == 0
    
    # if the len of s is even, divide into exactly half
    if is_even:
        new_str += spaced(s[:mid])
        new_str += ' '      # add space between them
        new_str += spaced(s[mid:])
        
    # if the len of s is odd, right is 1 less than left
    else:
        new_str += spaced(s[:mid+1])
        new_str += ' '      # add space between them
        new_str += spaced(s[mid+1:])
    
    return new_str

# print(spaced("HelloWorld!"))
