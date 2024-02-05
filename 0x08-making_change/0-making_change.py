#!/usr/bin/python3

def min_coins(coins, total):

    if total <= 0:
        return 0
    
    # Initialize an array to store the minimum number of coins 
    array = [float('inf')] * (total + 1)

    # o is the minimum number of coins needed to make a change
    array[0] = 0

    for coin in coins:
        
        for amount in range(coin, total + 1):
            array[amount] = min(array[amount], array[amount - coin] + 1)

    # If array[total] is still float('inf'), no combination of coins is possible
    if array[total] == float('inf'):
        return -1
    else:
        return array[total]