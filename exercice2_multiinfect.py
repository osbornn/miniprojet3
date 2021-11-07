from pandas import *
import numpy as np
import re as r

#Concerne (iii) de l'exercice 2


casesList = []

passageList = []
totalMultiinfectionList = []

#Question 1) : Multi-Infections - noeuds initiaux infectés

with open('multi_infected.txt', 'rt') as f:
    for line in f:
        if(r.match('[0-9]+', line)):
            values = line.split(' ')
            for v in range (0,100):
                casesList.append(values[v])           

arr = np.array(casesList)
arrs = np.reshape(arr, (1000, 100))

for sim in range(0,10):
    for i in range(0,100):
        counter_state = 0
        for j in range(100*sim,100*(sim+1)):
            if((int(arrs[j,i]) == 1) and (int(arrs[(j-1),i]) == 0)):
                counter_state+=1
        passageList.append(counter_state) #liste de passage pour stocker les fois où un noeud est infecté

    simMultiinfectionList = np.array(passageList) #on la convertit en array numpy
    totalMultiinfectionList.append(simMultiinfectionList.mean()) #on stocke la moyenne du changement de tous les noeuds de la simulation dans une liste

df_infected = read_csv('infectedNodes.csv')
df_infected["Distribution Multi-Infections"] = totalMultiinfectionList
df_infected = df_infected.rename(columns={'Unnamed: 0' : 'Noeuds initiaux infectés'})

df_infected.to_csv('infectedNodes.csv', index=False)

casesList.clear()
totalMultiinfectionList.clear()
passageList.clear()

#Question 2) : Multi-Infections - rayon de mobilité

with open('multi_rayon.txt', 'rt') as f:
    for line in f:
        if(r.match('[0-9]+', line)):
            values = line.split(' ')
            for v in range (0,100):
                casesList.append(values[v])           

arr = np.array(casesList)
arrs = np.reshape(arr, (1000, 100))

for sim in range(0,10):
    for i in range(0,100):
        counter_state = 0
        for j in range(100*sim,100*(sim+1)):
            if((int(arrs[j,i]) == 1) and (int(arrs[(j-1),i]) == 0)):
                counter_state+=1
        passageList.append(counter_state) #liste de passage pour stocker les fois où un noeud est infecté

    simMultiinfectionList = np.array(passageList) #on la convertit en array numpy
    totalMultiinfectionList.append(simMultiinfectionList.mean()) #on stocke la moyenne du changement de tous les noeuds de la simulation dans une liste

df_travel = read_csv('travel_distance.csv')
df_travel["Distribution Multi-Infections"] = totalMultiinfectionList
df_travel = df_travel.rename(columns={'Unnamed: 0' : 'Rayon de mobilité'})

df_travel.to_csv('travel_distance.csv', index=False)

casesList.clear()
totalMultiinfectionList.clear()
passageList.clear()

#Question 3) : Multi-Infections - Durée d'infection

with open('multi_infectionperiod.txt', 'rt') as f:
    for line in f:
        if(r.match('[0-9]+', line)):
            values = line.split(' ')
            for v in range (0,100):
                casesList.append(values[v])           

arr = np.array(casesList)
arrs = np.reshape(arr, (2000, 100))

for sim in range(0,20):
    for i in range(0,100):
        counter_state = 0
        for j in range(100*sim,100*(sim+1)):
            if((int(arrs[j,i]) == 1) and (int(arrs[(j-1),i]) == 0)):
                counter_state+=1
        passageList.append(counter_state) #liste de passage pour stocker les fois où un noeud est infecté

    simMultiinfectionList = np.array(passageList) #on la convertit en array numpy
    totalMultiinfectionList.append(simMultiinfectionList.mean()) #on stocke la moyenne du changement de tous les noeuds de la simulation dans une liste

df_infperiod = read_csv('inf_period.csv')
df_infperiod["Distribution Multi-Infections"] = totalMultiinfectionList
df_infperiod = df_infperiod.rename(columns={'Unnamed: 0' : 'Durée Infection'})

df_infperiod.to_csv('inf_period.csv', index=False)

casesList.clear()
totalMultiinfectionList.clear()
passageList.clear()

#Question 4) : Multi-Infections - Durée de contagion

with open('multi_contagperiod.txt', 'rt') as f:
    for line in f:
        if(r.match('[0-9]+', line)):
            values = line.split(' ')
            for v in range (0,100):
                casesList.append(values[v])           

arr = np.array(casesList)
arrs = np.reshape(arr, (2000, 100))

for sim in range(0,20):
    for i in range(0,100):
        counter_state = 0
        for j in range(100*sim,100*(sim+1)):
            if((int(arrs[j,i]) == 1) and (int(arrs[(j-1),i]) == 0)):
                counter_state+=1
        passageList.append(counter_state) #liste de passage pour stocker les fois où un noeud est infecté

    simMultiinfectionList = np.array(passageList) #on la convertit en array numpy
    totalMultiinfectionList.append(simMultiinfectionList.mean()) #on stocke la moyenne du changement de tous les noeuds de la simulation dans une liste

df_contagperiod = read_csv('contag_period.csv')
df_contagperiod["Distribution Multi-Infections"] = totalMultiinfectionList
df_contagperiod = df_contagperiod.rename(columns={'Unnamed: 0' : 'Durée de contagiosité'})

df_contagperiod.to_csv('contag_period.csv', index=False)

casesList.clear()
totalMultiinfectionList.clear()
passageList.clear()

#Question 5) : Multi-Infections - Durée d'immunité

with open('multi_immunityperiod.txt', 'rt') as f:
    for line in f:
        if(r.match('[0-9]+', line)):
            values = line.split(' ')
            for v in range (0,100):
                casesList.append(values[v])           

arr = np.array(casesList)
arrs = np.reshape(arr, (2000, 100))

for sim in range(0,20):
    for i in range(0,100):
        counter_state = 0
        for j in range(100*sim,100*(sim+1)):
            if((int(arrs[j,i]) == 1) and (int(arrs[(j-1),i]) == 0) ):
                counter_state+=1
        passageList.append(counter_state) #liste de passage pour stocker les fois où un noeud est infecté

    simMultiinfectionList = np.array(passageList) #on la convertit en array numpy
    totalMultiinfectionList.append(simMultiinfectionList.mean()) #on stocke la moyenne du changement de tous les noeuds de la simulation dans une liste

df_immuneperiod = read_csv('immune_period.csv')
df_immuneperiod["Distribution Multi-Infections"] = totalMultiinfectionList
df_immuneperiod = df_immuneperiod.rename(columns={'Unnamed: 0' : 'Durée Immunité'})

df_immuneperiod.to_csv('immune_period.csv', index=False)

casesList.clear()
totalMultiinfectionList.clear()
passageList.clear()

#Question 6) : Multi-Infections - Densité de la population

nb_values = 0

with open('multi_pop.txt', 'rt') as f:
    for line in f:
        if(r.match('[0-9]+', line)):
            values = line.split(' ')
            nb_values = len(values) - 1
            for v in range(0, nb_values):
                casesList.append(values[v])
        if(len(casesList) == (100*nb_values) and len(casesList) > 0):
            arrSim = np.array(casesList)
            arrSim = np.reshape(arrSim, (100, nb_values))
            for i in range(0,nb_values):
                counter_state = 0
                for j in range(0,100):
                    if((int(arrSim[j,i]) == 1) and (int(arrSim[(j-1),i]) == 0)):
                        counter_state+=1
                passageList.append(counter_state)
            simMultiinfectionList = np.array(passageList) 
            totalMultiinfectionList.append(simMultiinfectionList.mean())
            casesList.clear() 

df_densitypop = read_csv('densite_pop.csv')
df_densitypop["Distribution Multi-Infections"] = totalMultiinfectionList
df_densitypop = df_densitypop.rename(columns={'Unnamed: 0' : 'Densité de la population'})

df_densitypop.to_csv('densite_pop.csv', index=False)