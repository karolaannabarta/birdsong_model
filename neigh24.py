# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 16:25:51 2018

@author: Karola
"""

#from initial_setup import bird_grid

#print(bird_grid)

def neigh24(x, y, array):
    neighbour=[]
    for r in [x-2, x-1, x, x+1, x+2]:
        for s in [y-2, y-1, y, y+1, y+2]:
            if r<0 or s<0 or r>=len(array) or s>=len(array[0]) \
            or (r==x and s==y):
                continue
            else:
                if array[r][s]==1:
                    neighbour.append((r, s))
    return neighbour

"""from initial_setup import birds
for i in range(len(birds)):
    print(neigh24(birds[i].x, birds[i].y))"""