#!/bin/python

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Complete this function
    aScore = 0
    oScore = 0
    for distance in apples:
        if a + distance in range(s,t+1):
            aScore+=1
    for distance in oranges:
        if b + distance in range(s,t+1):
            oScore+=1
    print(aScore)
    print(oScore)
        

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)
