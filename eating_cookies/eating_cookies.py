#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# def eating_cookies(n, cache=None):
#   pass

# def eating_cookies(n):
#   cookies = [0,1,2,3]      
  
#   times = n
#   count = 0
#   lis = []
#   if n==0:
#     return 1
#   if n > 0:
#     for i in cookies:
#       temp = i + eating_cookies(n-1)
#       if(temp == times):
#         count = count +1
# eating_cookies(100)


def eating_cookies(n):
  cookies = [0,1,2,3]

  # each_way = 0

  # total = n

  # if n==0 or n==1:
  #   return 1
  # if n > 1 :
  #   for i in range(0,len(cookies)):
  #     each_way = each_way + i
  # return 'pass'  
  #
  return cookies    

def ways(n):

  cookies_eaten_at_a_time = [0,1,2,3]

  total = n

  lis = []

  count = 0

  if(n==0 or n==1):
    return 1

  for k in range(2,n):

    lis.append(eating_cookies(k))      
    # for i in range(1,len(lis)):
    #   for j in range(1,len(lis[i])):
    #     print(lis[i])
          # print(f'i is {i}, j is {j} {lis[i][j]}')
          # print(f'before if: i is {i}, j is {j}')
          # if(i+j == n):
          #   print(f'i is {i}, j is {j}')
          #   count = count+1

  print(lis)
  # return count

print(ways(2))

# eating_cookies(2)

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')