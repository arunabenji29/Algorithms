#!/usr/bin/python

import sys
import math

cache = {}

def rock_paper_scissors(n):
  rps = ["rock","paper","scissors"] 

  a = [[] for _ in range(3**n)]
  count = 0
  firstCount = 0
  secondCount = 0
  thirdCount = 0
  fourthCount = 0
  

  for i in range(0,len(a)):
    # print(rps[count])
    # count = count+1

    # a[i].append(rps[count])
    # count = count+1

    if(n==1):
      a[i].append(rps[count])
    elif(n==2):
      a[i].extend((rps[count],rps[firstCount]))
    elif(n==3):
      a[i].extend((rps[count],rps[firstCount],rps[secondCount]))
    elif(n==4):
      a[i].extend((rps[count],rps[firstCount],rps[secondCount],rps[thirdCount]))
    elif(n==5):
      a[i].extend((rps[count],rps[firstCount],rps[secondCount],rps[thirdCount],rps[fourthCount]))
    
    count = count+1
    if(count==3):
      count=0
      firstCount += 1

    if(firstCount==3):
      count=0
      firstCount=0
      secondCount +=1

    if(secondCount==3):
      count=0
      firstCount=0
      secondCount = 0
      thirdCount +=1

    if(thirdCount==3):
      count=0
      firstCount=0
      secondCount =0
      thirdCount = 0
      fourthCount += 1


  # print(a)
  return a
print(rock_paper_scissors(0))  


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')