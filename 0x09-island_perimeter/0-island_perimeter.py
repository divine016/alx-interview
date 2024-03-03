#!/usr/bin/python3
""" Getting the island perimeter"""


def island_perimeter(grid):
    """ Islands perimeter"""
    sum = 0
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x] == 1 and (i < (len(grid) - 1) and i > 0):
                fb_vers2 = (grid[i + 1][x] != 1 or grid[i - 1][x] != 1)
                fb_vers_n = (grid[i + 1][x] != 1 and grid[i - 1][x] != 1)
                fb_vers = (grid[i + 1][x] == 1 and grid[i - 1][x] == 1)
                sum += total(grid, i, x, fb_vers, fb_vers2, fb_vers_n)
            elif grid[i][x] == 1 and (i == (len(grid) - 1)):
                fb_vers2 = (grid[i - 1][x] != 1 or True)
                fb_vers_n = (grid[i - 1][x] != 1 and True)
                fb_vers = (grid[i - 1][x] == 1 and False)
                sum += total(grid, i, x, fb_vers, fb_vers2, fb_vers_n)
            elif grid[i][x] == 1 and (i == 0):
                fb_vers2 = (True or grid[i + 1][x] != 1)
                fb_vers_n = (True and grid[i + 1][x] != 1)
                fb_vers = (False and grid[i + 1][x] == 1)
                sum += total(grid, i, x, fb_vers, fb_vers2, fb_vers_n)
    return sum


def total(grid, i, x, fb_vers, fb_vers2, fb_vers_n):
    """ get total perimeter now """
    sum = 0
    if x == 0 and grid[i][x] == 1:
        if fb_vers2 and (not fb_vers_n) and grid[i][x + 1] != 1:
            sum += 3
        elif fb_vers_n and grid[i][x + 1] != 1:
            sum += 4
        elif fb_vers_n and grid[i][x + 1] == 1:
            sum += 3
        elif fb_vers2 and (not fb_vers_n) and grid[i][x + 1] == 1:
            sum += 2
        elif fb_vers and grid[i][x + 1] != 1:
            sum += 2
        elif fb_vers and grid[i][x + 1] == 1:
            sum += 1
    elif (x != len(grid[i]) - 1) and grid[i][x] == 1:
        fb_hor = (grid[i][x + 1] == 1 and grid[i][x - 1] == 1)
        fb_hor_n = (grid[i][x + 1] != 1 and grid[i][x - 1] != 1)
        fb_hor2 = (grid[i][x + 1] != 1 or grid[i][x - 1] != 1)
        if (fb_hor2 and (not fb_hor_n)) and (fb_vers2 and (not fb_vers_n)):
            sum += 2
        elif (fb_hor2 and (not fb_hor_n)) and fb_vers_n:
            sum += 3
        elif (fb_hor2 and (not fb_hor_n)) and fb_vers:
            sum += 1
        elif fb_hor and fb_vers_n:
            sum += 2
        elif fb_hor and (fb_vers2 and (not fb_vers_n)):
            sum += 1
        elif fb_hor_n and fb_vers_n:
            sum += 4
        elif fb_hor_n and fb_vers:
            sum += 2
        elif fb_hor_n and (fb_vers2 and (not fb_vers_n)):
            sum += 3
    elif grid[i][x] == 1:
        if fb_vers2 and (not fb_vers_n) and grid[i][x - 1] != 1:
            sum += 3
        elif fb_vers2 and (not fb_vers_n) and grid[i][x - 1] == 1:
            sum += 2
        elif fb_vers_n and grid[i][x - 1] != 1:
            sum += 4
        elif fb_vers_n and grid[i][x - 1] == 1:
            sum += 3
        elif fb_vers and grid[i][x - 1] != 1:
            sum += 2
        elif fb_vers and grid[i][x - 1] == 1:
            sum += 1
    return sum