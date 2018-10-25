#LEARNING RULE: facilitation with neighbours
from get_one_neighbour import oneneigh8, oneneigh24, oneneigh48
import pandas as pd
from random import sample
from getting_birds import syllables, num_of_syll
from numpy import mean, random
#from initial_setup import birds

#b=birds[1].song

#this function works with an individual so it should be implemented in a cycle
# which loops through the "birds" list


def learning(individual, l, mode):
    #for ui in range(len(l)):
    #collecting juveniles:
    indi = num_of_syll
    indn= num_of_syll
    a=[]
    isyll_index=len(l[individual].syll_rep)
    nsyll_index=len(l[individual].syll_rep)
    sharedsyllind=[]
    if l[individual].age==0: 
    #collecting the syllables used by  the juveniles' neighbours
        # we should collect them in a dataframe or something, because
        # we will need the probabilities of syllable-use as well
        # and we have to work with both of them
        df=pd.DataFrame(data=(l[individual].neighbours[0].syll_rep))
        l[individual].neigh_song = df.assign(use=l[individual].neighbours[0].syll_use)
    #learning: randomly from neighbours
        if len(l[individual].neigh_song)==0:
            #so if they don't have any neighbour, they will have a random
            # syll_rep
            df=pd.DataFrame(sample(syllables, 50))
            a=random.exponential(1.0, 50)
            l[individual].neigh_song = df.assign(use=a/sum(a))
        # so everyone has a dataframe of one of his neighbour's syll_rep 
        # and syll_use;
        # we want to choose those syllables that both of them use and
        # the individual's neighbour uses it the most frequent:
        for i in range(len(l[individual].song)):
            for ii in range(len(l[individual].neigh_song)):
                if l[individual].song.loc[i,0]==l[individual].neigh_song.loc[ii,0]:
                    # make a list of shared syllables' indeces:
                    sharedsyllind.append(i)
                    #we have to choose randomly from them:
                    indi=sample(sharedsyllind,1)
                    indi=indi[0]
                    #print(l[individual].song.loc[i,0])
                    #print(l[individual].neigh_song.loc[ii,0])
                    """mostfreq = min(l[individual].neigh_song['use'])
                    # choosing which syllable uses the neighbour the most 
                    # frequently because we want to be similar
                    maxi = l[individual].neigh_song.loc[ii,'use']
                    #print(l[individual].song.loc[i,'use'])
                    #print(l[individual].neigh_song.loc[ii,'use'])
                    if maxi > mostfreq:
                        indi = i #memorizing the syllable's index
                        indn = ii
                        mostfreq = maxi
                        """
                    #print(ind)
                    #ldiff.append(l[individual].song.loc[i,0])
                # it could happen that there is are no matching syllables:
        if indi<num_of_syll: # so if there is a shared syllable
            #print(ind)
            #print(l[individual].song.loc[ind])
            # changing the syll_use:
            l[individual].song.loc[indi,'use'] = l[individual].song.loc[indi,'use'] + mode
            if l[individual].song.loc[indi,'use'] < 0:
                l[individual].song.loc[indi,'use'] = 0
            if l[individual].song.loc[indi,'use'] > 1:
                l[individual].song.loc[indi,'use'] = 1
        else: # so if there are no shared syllables:
            if mode>0: # so if the individ wants to facilitate:
                # he should find the neighbour's most used syllable:
                maxsylln = max(l[individual].neighbours[0].song['use'])
                minsylli = min(l[individual].song['use'])
                nsyll_index=l[individual].neighbours[0].song.loc[l[individual].neighbours[0].song['use']==maxsylln].index[0]
                isyll_index=l[individual].song.loc[l[individual].song['use']==minsylli].index[0]
                l[individual].song.loc[isyll_index, :]=l[individual].neighbours[0].song.loc[nsyll_index, :]
        # normalize back to rel_freq:
        l[individual].song['use'] = l[individual].song['use']/sum(l[individual].song['use'])
        l[individual].syll_rep = l[individual].song[0].tolist()
        l[individual].syll_use = l[individual].song['use'].tolist()
        #print(l[individual].song.loc[ind]) 
        # ATTENTION: you didn;t change the syll_rep and syll_use vectors,
        # just the song dataframe!!!
    #print(l[individual].neigh_syll)
"""
#inhibition(0)
for i in range(len(birds)):
    #song=l[i].song
    oneneigh48(i, birds, bird_grid)
    learning(i, birds, 0.01)
    #print(song==l[i].song)
    #print(len((l[i].neigh_song)))
    
#print(l[9].song)
#print(l[9].neigh_song)
#print(b==l[1].song)
#print(l[9].neigh_song.sort_values('use'))
#print(l[11].neigh_syll.sort_values(by=['use']))
"""