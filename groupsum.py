#!/usr/bin/python

##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 25/05/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  Takes a target integer value, n, and a set of integers, 
##  and determines whether or not any subset of those integers can be summed to make n.
##  

def generate(n, s):
    '''
        Return boolean value for whether n can be made by subset
        Time complexity: O(n^2)
    '''
    
    # base case (if the recursive call reaches to the end, with subset containing single element)
    if len(s) == 1:
        return n == s[0]
    
    # case1: using the first element as part of n
    if generate(n - s[0], s[1:]): return True
    
    # case2: not using the first element as part of n
    if generate(n, s[1:]): return True
    
    return False

#print(generate(9, [0, 0, 1, 0, 0, 0, 7, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
