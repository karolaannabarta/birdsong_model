#Defining the birds class and the grid and filling up the grid
import numpy as np
from random import sample
from random import choice
import pandas as pd

# 500 nest -> 10x50 matrix:
rows=10
cols=50
bird_grid = np.zeros((rows, cols))
num_of_syll=500
die=[0,1]
# from the 500 sites 100 is occupied by birds -> this occupation happens randomly
#function for site occupation

#general variables and parameters
age = [0,1,2,3,4,5,6,7] #ages: 1 means 1 year old; 2 means older than 1 year old
#I put multiple 2s in place of the older ages
prob_surviving=[0.5, 1 , 0.5, 0.5, 0.5, 0.5, 0.5, 0]
syllables = [syll for syll in range(num_of_syll)] #the x syllables used by the birds

#individual-based variables:
#syll_rep = sample(syllables, 50) #individually used syllables: 50/2000
#IMPORTANT: this is without replacement
#syll_use = [x/sum(range(1,51)) for x in sample(range(1,51), 50)] #probability of choosing a given syllable



#let us create a class called birds:
class Birds:
    #these variables are general to all of the birds:
    m_r = 0.4 #mortality rate
    #these things should be individualistic:
    def __init__(self, ID):
        self.id=ID
        self.age=0
        #self.age=age[0]
        if self.age<1: #so if they are juveniles
            self.syll_rep=() #they wont have a repertoire
        self.syll_use=[]
        self.song=[]
        #assigning a probability to use a given syllable to every bird
        #NOTE TO SELF: this way the juveniles will have their own syllable using probabilities, independent of the fitness or others' syllable use
        #giving every bird a spatial place:
        self.x=choice(range(len(bird_grid)))
        self.y=choice(range(len(bird_grid[1])))
        #print(self.x,self.y)
        self.place=[self.x, self.y]
        """while bird_grid[self.place[0], self.place[1]]!=0: #meaning, if
            that place is already taken, then reassign a place, and do this
            until that place is free
            self.x=choice(range(len(bird_grid)))
            self.y=choice(range(len(bird_grid[1])))
            self.place=[self.x, self.y]"""
        #bird_grid[self.place[0], self.place[1]]=1.0 #switching the given bird's place occupied on the grid
        self.neighbours=[]
        self.neighboursplaces=[]
        self.neigh_song=[]
        self.neigh_syll=[]
        self.prob_surviving=prob_surviving[self.age]
        self.die=0

#print(bird_grid)
