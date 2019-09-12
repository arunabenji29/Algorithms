#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = -1000
  for i in range(0,len(prices)):
    for j in range(1,len(prices)):
      if(j>i):

        diff = prices[j]-prices[i]
        print(f'{prices[j]} - {prices[i]} is {diff}')
        print(f'max profit is {max_profit}')
        if(diff > max_profit):
          max_profit = diff

  return max_profit

print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))
# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))