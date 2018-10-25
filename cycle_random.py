# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 12:22:52 2018

@author: Karola
"""

#THE CYCLE:
"""EZT CSINALD MEG HOGY LEGYEN JO"""
from matplotlib import pyplot as plt
#from def_relative_frequency import get_relfreq
from random import choice
from random import random
from random import sample
import numpy as np
#from learn_random import learning
from get_one_neighbour import oneneigh8, oneneigh24, oneneigh48, oneneigh80
from getting_birds import rows, cols, Birds, syllables, num_of_syll, prob_surviving, bird_grid
#from initial_setup import bird_grid, birds
import pandas as pd


"""
orig_pop_rep=pd.DataFrame()
orig_pop_syllrep = []
orig_pop_sylluse = []
# we need the rel_freq of each syllable in the whole population
for i in range(len(birds)): # searching through the population
    for ii in range(len(birds[i].syll_rep)): # searching through their syll_rep
        orig_pop_syllrep.append(birds[i].syll_rep[ii])
        orig_pop_sylluse.append(birds[i].syll_use[ii])

orig_pop_rep[0]=orig_pop_syllrep
orig_pop_rep[1]=orig_pop_sylluse
orig_pop_rep=orig_pop_rep.sort_values([0,1])
sum_use = []

for i in range(len(syllables)):
    sum_use.append(orig_pop_rep.loc[orig_pop_rep[0] == i, 1].sum())
"""
# it can happen that some syllables are missing from the df, but we have to 
# calculate them as well -> this is solved!
#print(orig_pop_rep)
systype = 1 # this is the system's type, meaning: if it closed or opened in the 
# case of youngsters starting syll_rep: 0 - it is open, they can learn from the
# whole syllables; 1 - it is closed, they can only learn from the existing pop_rep
num_birds=100
learningoccasions = 30
num_cycle=40
countyears=1
syllget=0
#mr=[0.2, 0.4, 0.8]
mr=[0.6]

pop_rep = pd.DataFrame() 
pop20_rep = pd.DataFrame() 

alpha=[-0.01,-0.005,-0.001, 0, 0.001, 0.005, 0.01]
#alpha=[0, 0.001, 0.005, 0.01]
#alpha=[-0.001]
for m_r in mr:
    for a in alpha:
        birds=list()
        for bi in range(num_birds):
            birds.append(Birds(bi))
            birds[bi].age=0
            if syllget==1:
                # getting the syllables exponentially:
                su=np.random.exponential(1,50)
                birds[bi].syll_use=[x/sum(su) for x in su]
            else: # getting the syllables randomly:
                su=[random() for x in range(50)]
                birds[bi].syll_use=[x/sum(su) for x in su]
            while bird_grid[birds[bi].place[0], birds[bi].place[1]]!=0:
                #meaning, if that place is already taken, then reassign a place, and do this until that place is free
                birds[bi].x=choice(range(len(bird_grid)))
                birds[bi].y=choice(range(len(bird_grid[1])))
                birds[bi].place=[birds[bi].x, birds[bi].y]
            bird_grid[birds[bi].x, birds[bi].y]=1.0
            #we also need to define syllable reppertoire for them, because the learning
            # rule will not work otherwise
            birds[bi].syll_rep=sample(syllables, 50)
            # creating a dataframe for every bird's song, which we can use in the 
            # learning rule:
            df=pd.DataFrame(data=(birds[bi].syll_rep))
            birds[bi].song = df.assign(use=birds[bi].syll_use)
        
        ind1=sample(birds, 1)
        if a>0:
            learnmode='rand0'+str(a)[2:]
        elif a<0:
            learnmode='randm0'+str(a)[3:]
        else:
            learnmode='rand0'
        ind1_rep = pd.DataFrame() 
        ind2_rep = pd.DataFrame()  
        pop_rep = pd.DataFrame() 
        pop20=[]
        pop20_rep= pd.DataFrame()
    
        for c in range(num_cycle):
            #print(bird_grid)
            #UPDATE RULES:
            for lo in range(learningoccasions):
                for i in range(len(birds)):
                    # learning:
                    sc=sample(range(len(birds[i].syll_use)), 1)[0]
                    aa=sample([-a, a], 1)[0]
                    birds[i].song.loc[sc,'use']=birds[i].song.loc[sc,'use']+ aa
                    birds[i].song['use']=birds[i].song['use']/sum(birds[i].song['use'])
                    birds[i].syll_use=birds[i].song['use'].tolist()
                if ind1[0] in birds and ind1[0].age==0:
                    ind1_rep[str(lo+1)] = ind1[0].song['use'] # here I put lc+1 because otherwise there would be 
                if c==num_cycle-10:
                    ind2=birds[99]
                    ind2_rep[str(lo+1)] = ind2.song['use']
            # Attach the new population's syll_use to the pop_rep dataframe: and I want
            # to get not just the syll_rep but the syll_use as well!!!
            pop20=sample(birds,20)
            if (c+1)% countyears == 0:
                new_pop20_rep=pd.DataFrame()
                new_pop20_syllrep = []
                new_pop20_sylluse = []
            # we need the rel_freq of each syllable in the whole population
                for i in range(len(pop20)): # searching through the population
                    for ii in range(len(pop20[i].syll_rep)): # searching through their syll_rep
                        new_pop20_syllrep.append(pop20[i].syll_rep[ii])
                        new_pop20_sylluse.append(pop20[i].syll_use[ii])
            
                new_pop20_rep[0]=new_pop20_syllrep
                new_pop20_rep[1]=new_pop20_sylluse
                new_pop20_rep=new_pop20_rep.sort_values([0,1])
                sum_use = []
            
                for i in range(len(syllables)):
                    sum_use.append(new_pop20_rep.loc[new_pop20_rep[0] == i, 1].sum())
            
                pop20_rep[str(c+1)] = sum_use/sum(sum_use) # here I put c+1 because otherwise there would be 
        
                new_pop_rep=pd.DataFrame()
                new_pop_syllrep = []
                new_pop_sylluse = []
            # we need the rel_freq of each syllable in the whole population
                for i in range(len(birds)): # searching through the population
                    for ii in range(len(birds[i].syll_rep)): # searching through their syll_rep
                        new_pop_syllrep.append(birds[i].syll_rep[ii])
                        new_pop_sylluse.append(birds[i].syll_use[ii])
            
                new_pop_rep[0]=new_pop_syllrep
                new_pop_rep[1]=new_pop_sylluse
                new_pop_rep=new_pop_rep.sort_values([0,1])
                sum_use = []
            
                for i in range(len(syllables)):
                    sum_use.append(new_pop_rep.loc[new_pop_rep[0] == i, 1].sum())
            
                pop_rep[str(c+1)] = sum_use/sum(sum_use) # here I put c+1 because otherwise there would be 
                # two columns with the name "0"
            
        #next step: some of them gotta die
            #survivors=list(np.random.choice(birds, int(len(birds)*(1-m_r)), replace=False))
            survivors = []
            for i in range(len(birds)):
                birds[i].prob_surviving=prob_surviving[birds[i].age]
                p=random() #generate a random number between 0 and 1
                if p<birds[i].prob_surviving:
                    #if p is less than the prob of surviving of that bird, then
                    # that bird is  a survivor, huray!
                    survivors.append(birds[i])
        
        #renewing the site:
            #print(len(birds))
            bird_grid = np.zeros((rows, cols))
        
            for i in range(len(survivors)):
                bird_grid[survivors[i].x, survivors[i].y]=1.0
            #print("survivors:" + str(sum(sum(bird_grid))))
            #for i in range(len(birds)):
                survivors[i].age=survivors[i].age+1
        
        #creating new birds:
            new=list()
            num_birds = len(birds)
            for uuui in range(num_birds-len(survivors)):
                new.append(Birds(uuui))
                while bird_grid[new[uuui].x, new[uuui].y]!=0:
                    #meaning, if that place is already taken, then reassign a place, and do this until that place is free
                    new[uuui].x=choice(range(len(bird_grid)))
                    new[uuui].y=choice(range(len(bird_grid[1])))
                    new[uuui].place=[new[uuui].x, new[uuui].y]
                bird_grid[new[uuui].x, new[uuui].y]=1
            #print(bird_grid)
            #print("with newbies:"+ str(sum(sum(bird_grid))))
            #giving a repertoire to the new ones:
            if systype==0:
                for i in range(len(new)):
                    if syllget==1:
                # getting the syllables exponentially:
                        su=np.random.exponential(1,50)
                        new[i].syll_use=[x/sum(su) for x in su]
                    else: # getting the syllables randomly:
                        su=[random() for x in range(50)]
                        new[i].syll_use=[x/sum(su) for x in su]
                    new[i].syll_rep=sample(syllables, 50)
                    df=pd.DataFrame(data=(new[i].syll_rep))
                    new[i].song = df.assign(use=new[i].syll_use)
            else:
                new_m_r=new[0:int(len(new)*m_r)] # this can be an empty list!!!
                new_n = new[int(len(new)*m_r):len(new)]
                syllpop =[]
                for s in range(len(pop_rep[str(c+1)])):
                    syllpop.append([s]*int(round(pop_rep.iloc[s,c]*10000)))
                syllpop=[item for sublist in syllpop for item in sublist]
                for ni in range(len(new_n)):
                    new_n[ni].syll_rep=sample(syllpop, 50)
                    new_n[ni].syll_use=[pop_rep.iloc[x,c] for x in new_n[ni].syll_rep]
                    df=pd.DataFrame(data=(new_n[ni].syll_rep))
                    new_n[ni].song = df.assign(use=new_n[ni].syll_use)
                for mi in range(len(new_m_r)):
                    su=[random() for x in range(50)]
                    new_m_r[mi].syll_use=[x/sum(su) for x in su]
                    new_m_r[mi].syll_rep=sample(syllables, 50)
                    df=pd.DataFrame(data=(new_m_r[mi].syll_rep))
                    new_m_r[mi].song = df.assign(use=new_m_r[mi].syll_use)
                new=new_n+new_m_r
            birds=survivors+new
    
        ind1_rep.to_csv('ind1rep_'+learnmode+'_'+str(num_cycle)+'x'+str(learningoccasions)+'sys'+str(systype)+str(syllget)+str(num_of_syll)+str(m_r)[2:]+'.csv')
        ind2_rep.to_csv('ind2rep_'+learnmode+'_'+str(num_cycle)+'x'+str(learningoccasions)+'sys'+str(systype)+str(syllget)+str(num_of_syll)+str(m_r)[2:]+'.csv')    
        pop_rep.to_csv('poprep_'+learnmode+'_'+str(num_cycle)+'x'+str(learningoccasions)+'sys'+str(systype)+str(syllget)+str(num_of_syll)+str(m_r)[2:]+'.csv')
        pop20_rep.to_csv('pop20rep_'+learnmode+'_'+str(num_cycle)+'x'+str(learningoccasions)+'sys'+str(systype)+str(syllget)+str(num_of_syll)+str(m_r)[2:]+'.csv')
        
        dmp = pd.DataFrame()
        dij=[]
        
        for i in range(len(pop_rep.loc[0,])): # getting through columns/years/num_cycle
            dij=[]
            for j in range(len(pop_rep.loc[0,])): # getting through columns/years/num_cycle again
                diff=[] # creating list for collecting the differeneces between years
                for s in range(len(syllables)): # getting through syllables
                    diff.append(abs(pop_rep.iloc[s,i]-pop_rep.iloc[s,j]))
                dij.append(0.5*sum(diff))
            dmp[str(i)]=dij
        
        dmp.to_csv('distmatpop_'+learnmode+'_'+str(num_cycle)+'x'+str(learningoccasions)+'sys'+str(systype)+str(syllget)+str(num_of_syll)+str(m_r)[2:]+'.csv')
        
        dmp20 = pd.DataFrame()
        dij20=[]
        
        for i in range(len(pop20_rep.loc[0,])): # getting through columns/years/num_cycle
            dij20=[]
            for j in range(len(pop20_rep.loc[0,])): # getting through columns/years/num_cycle again
                diff=[] # creating list for collecting the differeneces between years
                for s in range(len(syllables)): # getting through syllables
                    diff.append(abs(pop20_rep.iloc[s,i]-pop20_rep.iloc[s,j]))
                dij20.append(0.5*sum(diff))
            dmp20[str(i)]=dij20
        
        dmp20.to_csv('distmatpop20_'+learnmode+'_'+str(num_cycle)+'x'+str(learningoccasions)+'sys'+str(systype)+str(syllget)+str(num_of_syll)+str(m_r)[2:]+'.csv')
        
        dmi1 = pd.DataFrame()
        dij=[]
        for i in range(len(ind1_rep.loc[0,])): # getting through columns/years/num_cycle
            dij=[]
            for j in range(len(ind1_rep.loc[0,])): # getting through columns/years/num_cycle again
                diff=[] # creating list for collecting the differeneces between years
                for s in range(len(ind1_rep[str(1)])): # getting through syllables
                    diff.append(abs(ind1_rep.iloc[s,i]-ind1_rep.iloc[s,j]))
                dij.append(0.5*sum(diff))
            dmi1[str(i)]=dij   
        dmi1.to_csv('distmatind1_'+learnmode+'_'+str(num_cycle)+'x'+str(learningoccasions)+'sys'+str(systype)+str(syllget)+str(num_of_syll)+str(m_r)[2:]+'.csv')
        
        dmi2 = pd.DataFrame()    
        dij=[]
        for i in range(len(ind2_rep.loc[0,])): # getting through columns/years/num_cycle
            dij=[]
            for j in range(len(ind2_rep.loc[0,])): # getting through columns/years/num_cycle again
                diff=[] # creating list for collecting the differeneces between years
                for s in range(len(ind2_rep[str(1)])): # getting through syllables
                    diff.append(abs(ind2_rep.iloc[s,i]-ind2_rep.iloc[s,j]))
                dij.append(0.5*sum(diff))
            dmi2[str(i)]=dij   
        dmi2.to_csv('distmatind2_'+learnmode+'_'+str(num_cycle)+'x'+str(learningoccasions)+'sys'+str(systype)+str(syllget)+str(num_of_syll)+str(m_r)[2:]+'.csv')
    
        lydmp = pd.DataFrame()
        diff=[]
        values=[]
        for c in range(num_cycle-10,num_cycle):
            for r in range(num_cycle-10,num_cycle):
                if c>r:
                    diff.append(c-r)
                    values.append(dmp.iloc[r,c])
        lydmp[1]=diff
        lydmp[2]=values
        lydmp=lydmp.sort_values([1,2])
        lydmp.to_csv('lydmp_'+learnmode+'_'+str(num_cycle)+'x'+str(learningoccasions)+'sys'+str(systype)+str(syllget)+str(num_of_syll)+str(m_r)[2:]+'.csv')
        
        lydmp20 = pd.DataFrame()
        diff=[]
        values=[]
        for c in range(num_cycle-10,num_cycle):
            for r in range(num_cycle-10,num_cycle):
                if c>r:
                    diff.append(c-r)
                    values.append(dmp20.iloc[r,c])
        lydmp20[1]=diff
        lydmp20[2]=values
        lydmp20 = lydmp20.sort_values([1,2])
        lydmp20.to_csv('lydmp20_'+learnmode+'_'+str(num_cycle)+'x'+str(learningoccasions)+'sys'+str(systype)+str(syllget)+str(num_of_syll)+str(m_r)[2:]+'.csv')
    
years = []

for i in range(num_cycle+1):
    if i%countyears==0 and i!=0:
        years.append(i)
yeardiss = pd.DataFrame()
yeardiff=[]
for i in years:
    yeardiff=[]
    for j in years:
        yeardiff.append(abs(i-j))
    yeardiss[i]=yeardiff
    
yeardiss.to_csv("distmatyears_"+str(num_cycle)+'x'+str(learningoccasions)+'.csv')

learnocc=[]
for i in range(learningoccasions+1):
    if i%countyears==0 and i!=0:
        learnocc.append(i)
learnoccdiss = pd.DataFrame()
learnoccdiff=[]
for i in learnocc:
    learnoccdiff=[]
    for j in learnocc:
        learnoccdiff.append(abs(i-j))
    learnoccdiss[i]=learnoccdiff
    
learnoccdiss.to_csv("distmatlearnocc_"+str(num_cycle)+'x'+str(learningoccasions)+'.csv')
    
"""for i in range(len(birds)):
    #print(birds[i].age, birds[i].syll_rep)
    for ii in range(len(birds[i].syll_rep)):
        new_pop_rep.append(birds[i].syll_rep[ii])

#print(new_pop_rep, len(new_pop_rep))

#print(get_relfreq(new_pop_rep, num_of_syll))
plt.plot(pop_rep[str(1)])
plt.plot(pop_rep[str(num_cycle)])

plt.show()
"""