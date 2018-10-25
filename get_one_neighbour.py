#Collecting just one of the neighbours from the given neighbourhood

from neigh8 import neigh8 #importing the definition/type of neighbourhood
#from initial_setup import birds
from neigh24 import neigh24
from neigh48 import neigh48
from neigh80 import neigh80

def oneneigh8(ni, l, array): #searching for every bird
    #collecting every birds' neighbours' places: there could be ones that have\
    # multiple neighbourplaces pairs (x,y)
    l[ni].neighboursplaces=neigh8(l[ni].x, l[ni].y, array)
    #looping through one bird's neighbours:
    for nii in range(len(l[ni].neighboursplaces)):
        #loopig through the birds list to search for the individuals located
        # at that given place (neighboursplace), and appending that individual
        # to the original bird's neighbours
        # This way we collect all neighbours in the given neighbourhood
        for niii in range(len(l)):
            #With the if statement I precise that I need only one neighbour:
            if (l[ni].neighboursplaces[nii][0]==l[niii].x and \
               l[ni].neighboursplaces[nii][1]==l[niii].y) and \
                len(l[ni].neighbours)<1:
                l[ni].neighbours.append(l[niii])
    #print(birds[ni].place, birds[ni].neighboursplaces, birds[ni].neighbours)
    
def oneneigh24(ni, l, array): #searching for every bird
    #collecting every birds' neighbours' places: there could be ones that have\
    # multiple neighbourplaces pairs (x,y)
    l[ni].neighboursplaces=neigh24(l[ni].x, l[ni].y, array)
    #looping through one bird's neighbours:
    for nii in range(len(l[ni].neighboursplaces)):
        #loopig through the birds list to search for the individuals located
        # at that given place (neighboursplace), and appending that individual
        # to the original bird's neighbours
        # This way we collect all neighbours in the given neighbourhood
        for niii in range(len(l)):
            #With the if statement I precise that I need only one neighbour:
            if (l[ni].neighboursplaces[nii][0]==l[niii].x and \
               l[ni].neighboursplaces[nii][1]==l[niii].y) and \
                len(l[ni].neighbours)<1:
                l[ni].neighbours.append(l[niii])
    #print(l[ni].place, birds[ni].neighboursplaces, birds[ni].neighbours)

def oneneigh48(ni, l, array): #searching for every bird
    #collecting every birds' neighbours' places: there could be ones that have\
    # multiple neighbourplaces pairs (x,y)
    l[ni].neighboursplaces=neigh48(l[ni].x, l[ni].y, array)
    #looping through one bird's neighbours:
    for nii in range(len(l[ni].neighboursplaces)):
        #loopig through the birds list to search for the individuals located
        # at that given place (neighboursplace), and appending that individual
        # to the original bird's neighbours
        # This way we collect all neighbours in the given neighbourhood
        for niii in range(len(l)):
            #With the if statement I precise that I need only one neighbour:
            if (l[ni].neighboursplaces[nii][0]==l[niii].x and \
               l[ni].neighboursplaces[nii][1]==l[niii].y) and \
                len(l[ni].neighbours)<1:
                l[ni].neighbours.append(l[niii])
    #print(birds[ni].place, birds[ni].neighboursplaces, birds[ni].neighbours)

def oneneigh80(ni, l, array): #searching for every bird
    #collecting every birds' neighbours' places: there could be ones that have\
    # multiple neighbourplaces pairs (x,y)
    l[ni].neighboursplaces=neigh80(l[ni].x, l[ni].y, array)
    #looping through one bird's neighbours:
    for nii in range(len(l[ni].neighboursplaces)):
        #loopig through the birds list to search for the individuals located
        # at that given place (neighboursplace), and appending that individual
        # to the original bird's neighbours
        # This way we collect all neighbours in the given neighbourhood
        for niii in range(len(l)):
            #With the if statement I precise that I need only one neighbour:
            if (l[ni].neighboursplaces[nii][0]==l[niii].x and \
               l[ni].neighboursplaces[nii][1]==l[niii].y) and \
                len(l[ni].neighbours)<1:
                l[ni].neighbours.append(l[niii])
"""for i in range(len(l)):
    oneneigh8(i)
    if len(l[i].neighbours)==0:
        oneneigh24(i)
    if len(l[i].neighbours)==0:
        oneneigh48(i)
    print(l[i].neighbours)"""
#print(bird_grid)
# NOTE: this way only the .neighbours attribute will have one element, the
    # .neighboursplaces will still contain all of the neighbours' places