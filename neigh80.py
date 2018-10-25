# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:51:19 2018

@author: Karola
"""

#from initial_setup import bird_grid

#print(bird_grid)

def neigh80(x, y, array):
    neighbour=[]
    for r in [x-4,x-3, x-2, x-1, x, x+1, x+2, x+3, x+4]:
        for s in [y-4, y-3, y-2, y-1, y, y+1, y+2, y+3, y+4]:
            if r<0 or s<0 or r>=len(array) or s>=len(array[0]) \
            or (r==x and s==y):
                continue
            else:
                if array[r][s]==1:
                    neighbour.append((r, s))
    return neighbour