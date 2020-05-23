#!/usr/bin/python

##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 24/05/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  Design and implement a recursive function called generate(), 
##  which generates all length-n strings of 0’s and 1’s, for a given non negative integer n. 
##  
import time

## ======================== from bindec.py (revised the return type) ======================== ##
# converts decimal to a binary list of at least n digits
def decToBin(x, n):
    binary = []
    while (x > 0):
        binary.append(0 if x % 2 == 0 else 1)
        x = int(x / 2)
    while (len(binary) < n):
        binary.append(0)
    binary.reverse()
    return ''.join(str(e) for e in binary)
## ================================================================ ##

def recursion_generate(n, i_num_start = 0):
    '''
        1. top-down algorithm
        2. follow up the divide and conquer process
        3. root will have the O(2^n) memory
        4. Cons: Time complexity is O(2^n), which is not efficient
        5. Pros: Seems n can be putted bigger than dynamic version
            -> My opinion is since this is a divide and conquer algirhtm, not like dynamic version,
               everytime the system flow follow divide and conquer, the stack also do append and pop quickly.
               Maybe this allows the n can be bigger than 10 but not sure my approach is right.
    '''
    
    tmp_lst = []
    
    # base case
    if n == 0:
        tmp_lst.append(i_num_start)
        return tmp_lst
    
    tmp_lst += recursion_generate(n-1, i_num_start)
    tmp_lst += recursion_generate(n-1, tmp_lst[-1]+1)
    
    return tmp_lst
