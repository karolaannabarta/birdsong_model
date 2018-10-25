# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:33:15 2018

@author: Karola
"""
# Collecting the neighbours' places in the 8 neighbourhood (1st cycle around \
# the individual).
# !!! We can't import anything, we need to be as general as possible !!!
#from initial_setup import bird_grid

#print(bird_grid)

def neigh8(x, y, array):
    neighbour=[]
    for r in [x-1, x, x+1]:
        for s in [y-1, y, y+1]:
            if r<0 or s<0 or r==len(array) or s==len(array[0]) \
            or (r==x and s==y):
                continue
            else:
                if array[r][s]==1:
                    neighbour.append((r, s))
    return neighbour


    
