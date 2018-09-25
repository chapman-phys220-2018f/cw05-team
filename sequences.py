#!/usr/bin/env python3

# Abigail Wheaton
# 2299246
# wheaton@chapman.edu
# PHYS220 Fall 2018
# HW 03

# This file contains the function fibonacci(n) that returns the nth term of the fibonacci sequence

def fibonacci(n):
    i = 1
    j = 0
    f = 1
    if (not n > 0):
        raise Exception('Please enter a positive integer.')
    l = []
    for k in range(n):
        l.append(f)
        f = i + j
        j = i
        i = f
    return l

