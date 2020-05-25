#!/usr/bin/python

##  Assignment-201948932
##  
##  Created by Hong Geun Ji on 24/05/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  Design and implement a recursive function called generate(), 
##  which generates all length-n strings of 0’s and 1’s, for a given non negative integer n. 
##  
# import time

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

def top_down_generate(n):
    '''
        1. top-down algorithm
        2. follow up the divide and conquer process
        3. root will have the O(2^n) memory
        4. Cons: Time complexity is O(2^n), which is not efficient
        5. Pros: Seems n can be putted bigger than dynamic version (but why?)
            -> My opinion is since this is a divide and conquer algirhtm, not like dynamic version,
               everytime the system flow follows divide and conquer, the stack also do append and pop quickly.
               Maybe this allows the n can be bigger than 10 but not sure my approach is right.
    '''
    
    tmp_lst = []
    
    # base case
    if n == 0:
        tmp_lst.append(0)
        return tmp_lst
    
    # divide and conquer
    tmp_lst += top_down_generate(n-1)
    tmp_lst += top_down_generate(n-1)
    
    # if we draw the tree, we can see that we should calculate the elements starting from 2^(n-1) to avoid
    # unnecessary calculation
    for i in range(pow(2, n-1), len(tmp_lst)):
        tmp_lst[i] = tmp_lst[i-1] + 1
    
    return tmp_lst


def dynamic_generate(n):
    '''
        1. Bottom-up algorithm (Dynamic programming)
        2. Cons: n is limited as the limit for python3's recursion is 1000 times
        3. Pros: Time complexity is O(n)
    '''
    res_lst = []
    
    if n == 0:
        res_lst.append(0)
        return res_lst
        
    res_lst += dynamic_generate(n-1)
    
    # append a element using the previous element
    for i in range(pow(2, n) - len(res_lst)):   # index needs to be starts from pow(2, n)
        res_lst.append(res_lst[-1]+1)
    
    return res_lst
    
def generate(n):
    print("The parameter n is -> ", n)
    print("\n1. Dynamic programming version")
    print("2. Top-down recursive version")
    v = int(input("Please type the version number... "))
    while v not in [1, 2]:
        print("Please type only 1 or 2")
        v = input("Please type the version number... ")
    
    if v == 1:
        print("\nreturning list using dynamic programming function")
        tmp = dynamic_generate(n)
        for i in range(len(tmp)):
            tmp[i] = decToBin(tmp[i], n)
        return tmp
    else:
        print("\nreturning list using top-down recursive function")
        tmp = top_down_generate(n)
        for i in range(len(tmp)):
            tmp[i] = decToBin(tmp[i], n)
        return tmp

# tm = generate(5)
# print(tm)
