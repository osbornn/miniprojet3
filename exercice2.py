from pandas import *
import re as r

#Concerne (i) et (ii) de l'exercice 2


infnodesList = [] #liste des valeurs de la sim pour les noeuds initiaux infectés
travelList = [] #liste des valeurs pour le rayon de mobilité
infperiodList = [] #liste des valeurs pour la durée de l'infection
contagperiodList = [] #liste des valeurs pour la durée de la contagiosité
immuneperiodList = [] #liste des valeurs pour la durée d'immunité
densitepopList = [] #liste des valeurs pour la densité de population

casesList = []
saneList = [] #liste des personnes saines
infectedList = [] #liste des infectés
immuneList = [] #liste des immunisés

listTime = [] #liste servant à calculer la durée de l'épidémie


#Question 1) : Impact du nombre initial d'infectés

with open('res_infected.txt', 'rt') as f:
    for line in f:
        if(r.search('infected nodes', line)):
            inf_node = line.split(' ')[1]
            infnodesList.append(inf_node)
        if(r.match('\d* \d* \d*', line)):
            casesList.append(line)

for i in casesList:
    sane = i.split(' ')[0]
    infected = i.split(' ')[1]
    immune = i.split(' ')[2]
    saneList.append(int(sane))
    infectedList.append(int(infected))
    immuneList.append(int(immune))

dsane = {infnodesList[0] : Series(saneList[:100]), infnodesList[1] : Series(saneList[100:200]), infnodesList[2] : Series(saneList[200:300]),
    infnodesList[3] : Series(saneList[300:400]), infnodesList[4] : Series(saneList[400:500]), infnodesList[5] : Series(saneList[500:600]),
    infnodesList[6] : Series(saneList[600:700]), infnodesList[7] : Series(saneList[700:800]), infnodesList[8] : Series(saneList[800:900]),
    infnodesList[9] : Series(saneList[900:])} 

dinfected = {infnodesList[0] : Series(infectedList[:100]), infnodesList[1] : Series(infectedList[100:200]), infnodesList[2] : Series(infectedList[200:300]),
    infnodesList[3] : Series(infectedList[300:400]), infnodesList[4] : Series(infectedList[400:500]), infnodesList[5] : Series(infectedList[500:600]),
    infnodesList[6] : Series(infectedList[600:700]), infnodesList[7] : Series(infectedList[700:800]), infnodesList[8] : Series(infectedList[800:900]),
    infnodesList[9] : Series(infectedList[900:])} 

dimmune = {infnodesList[0] : Series(immuneList[:100]), infnodesList[1] : Series(immuneList[100:200]), infnodesList[2] : Series(immuneList[200:300]),
    infnodesList[3] : Series(immuneList[300:400]), infnodesList[4] : Series(immuneList[400:500]), infnodesList[5] : Series(immuneList[500:600]),
    infnodesList[6] : Series(immuneList[600:700]), infnodesList[7] : Series(immuneList[700:800]), infnodesList[8] : Series(immuneList[800:900]),
    infnodesList[9] : Series(immuneList[900:])} 

df1 = DataFrame(dsane)
df2 = DataFrame(dinfected)
df3 = DataFrame(dimmune)

#Pour la proportion max infectée de la population (ii)
dftotal= DataFrame({'Proportion max infectée' : df2.max()})

#Pour la durée de l'épidémie (i)
for i in range(0,10):
    count = 0
    for y in range(100*i,100*(i+1)):
        min = 0
        if(infectedList[y] == min and count < 1):
            listTime.append(y-(100*i))
            count += 1
    if(count == 0):
        listTime.append(99)

dftotal['Durée Epidemie'] = Series(listTime, index=dftotal.index)
dftotal.to_csv('infectedNodes.csv')

listTime.clear()
casesList.clear()
saneList.clear()
infectedList.clear()
immuneList.clear()


#Question 2) : Impact du rayon de mobilité

with open('res_rayon.txt', 'rt') as f:
    for line in f:
        if(r.search('travel distance', line)):
            travel_d = line.split(' ')[1]
            travelList.append(travel_d)
        if(r.match('\d* \d* \d*', line)):
            casesList.append(line)

for i in casesList:
    sane = i.split(' ')[0]
    infected = i.split(' ')[1]
    immune = i.split(' ')[2]
    saneList.append(int(sane))
    infectedList.append(int(infected))
    immuneList.append(int(immune))

dsane = {travelList[0] : Series(saneList[:100]), travelList[1] : Series(saneList[100:200]), travelList[2] : Series(saneList[200:300]),
    travelList[3] : Series(saneList[300:400]), travelList[4] : Series(saneList[400:500]), travelList[5] : Series(saneList[500:600]),
    travelList[6] : Series(saneList[600:700]), travelList[7] : Series(saneList[700:800]), travelList[8] : Series(saneList[800:900]),
    travelList[9] : Series(saneList[900:])} 

dinfected = {travelList[0] : Series(infectedList[:100]), travelList[1] : Series(infectedList[100:200]), travelList[2] : Series(infectedList[200:300]),
    travelList[3] : Series(infectedList[300:400]), travelList[4] : Series(infectedList[400:500]), travelList[5] : Series(infectedList[500:600]),
    travelList[6] : Series(infectedList[600:700]), travelList[7] : Series(infectedList[700:800]), travelList[8] : Series(infectedList[800:900]),
    travelList[9] : Series(infectedList[900:])} 

dimmune = {travelList[0] : Series(immuneList[:100]), travelList[1] : Series(immuneList[100:200]), travelList[2] : Series(immuneList[200:300]),
    travelList[3] : Series(immuneList[300:400]), travelList[4] : Series(immuneList[400:500]), travelList[5] : Series(immuneList[500:600]),
    travelList[6] : Series(immuneList[600:700]), travelList[7] : Series(immuneList[700:800]), travelList[8] : Series(immuneList[800:900]),
    travelList[9] : Series(immuneList[900:])} 

df1 = DataFrame(dsane)
df2 = DataFrame(dinfected)
df3 = DataFrame(dimmune)

#Pour la proportion max infectée de la population (ii)
dftotal2 = DataFrame({'Proportion max infectée' : df2.max()})

#Pour la durée de l'épidémie (i)
for i in range(0,10):
    count = 0
    for y in range(100*i,100*(i+1)):
        min = 0
        if(infectedList[y] == min and count < 1):
            listTime.append(y-(100*i))
            count += 1
    if(count == 0):
        listTime.append(99)

dftotal2['Durée Epidemie'] = Series(listTime, index=dftotal2.index)
dftotal2.to_csv('travel_distance.csv')

listTime.clear()
casesList.clear()
saneList.clear()
infectedList.clear()
immuneList.clear()


#Question 3) : Impact de la durée d'infection

with open('res_infectionperiod.txt', 'rt') as f:
    for line in f:
        if(r.search('infection period', line)):
            inf_p = line.split(' ')[1]
            infperiodList.append(inf_p)
        if(r.match('\d* \d* \d*', line)):
            casesList.append(line)

for i in casesList:
    sane = i.split(' ')[0]
    infected = i.split(' ')[1]
    immune = i.split(' ')[2]
    saneList.append(int(sane))
    infectedList.append(int(infected))
    immuneList.append(int(immune))

dsane = {infperiodList[0] : Series(saneList[:100]), infperiodList[1] : Series(saneList[100:200]), infperiodList[2] : Series(saneList[200:300]),
    infperiodList[3] : Series(saneList[300:400]), infperiodList[4] : Series(saneList[400:500]), infperiodList[5] : Series(saneList[500:600]),
    infperiodList[6] : Series(saneList[600:700]), infperiodList[7] : Series(saneList[700:800]), infperiodList[8] : Series(saneList[800:900]),
    infperiodList[9] : Series(saneList[900:1000]), infperiodList[10] : Series(saneList[1000:1100]), infperiodList[11] : Series(saneList[1100:1200]), 
    infperiodList[12] : Series(saneList[1200:1300]), infperiodList[13] : Series(saneList[1300:1400]), infperiodList[14] : Series(saneList[1400:1500]),
    infperiodList[15] : Series(saneList[1500:1600]), infperiodList[16] : Series(saneList[1600:1700]), infperiodList[17] : Series(saneList[1700:1800]),
    infperiodList[18] : Series(saneList[1800:1900]), infperiodList[19] : Series(saneList[1900:])} 

dinfected = {infperiodList[0] : Series(infectedList[:100]), infperiodList[1] : Series(infectedList[100:200]), infperiodList[2] : Series(infectedList[200:300]),
    infperiodList[3] : Series(infectedList[300:400]), infperiodList[4] : Series(infectedList[400:500]), infperiodList[5] : Series(infectedList[500:600]),
    infperiodList[6] : Series(infectedList[600:700]), infperiodList[7] : Series(infectedList[700:800]), infperiodList[8] : Series(infectedList[800:900]),
    infperiodList[9] : Series(infectedList[900:1000]), infperiodList[10] : Series(infectedList[1000:1100]), infperiodList[11] : Series(infectedList[1100:1200]), 
    infperiodList[12] : Series(infectedList[1200:1300]), infperiodList[13] : Series(infectedList[1300:1400]), infperiodList[14] : Series(infectedList[1400:1500]),
    infperiodList[15] : Series(infectedList[1500:1600]), infperiodList[16] : Series(infectedList[1600:1700]), infperiodList[17] : Series(infectedList[1700:1800]),
    infperiodList[18] : Series(infectedList[1800:1900]), infperiodList[19] : Series(infectedList[1900:])} 

dimmune = {infperiodList[0] : Series(immuneList[:100]), infperiodList[1] : Series(immuneList[100:200]), infperiodList[2] : Series(immuneList[200:300]),
    infperiodList[3] : Series(immuneList[300:400]), infperiodList[4] : Series(immuneList[400:500]), infperiodList[5] : Series(immuneList[500:600]),
    infperiodList[6] : Series(immuneList[600:700]), infperiodList[7] : Series(immuneList[700:800]), infperiodList[8] : Series(immuneList[800:900]),
    infperiodList[9] : Series(immuneList[900:1000]), infperiodList[10] : Series(immuneList[1000:1100]), infperiodList[11] : Series(immuneList[1100:1200]), 
    infperiodList[12] : Series(immuneList[1200:1300]), infperiodList[13] : Series(immuneList[1300:1400]), infperiodList[14] : Series(immuneList[1400:1500]),
    infperiodList[15] : Series(immuneList[1500:1600]), infperiodList[16] : Series(immuneList[1600:1700]), infperiodList[17] : Series(immuneList[1700:1800]),
    infperiodList[18] : Series(immuneList[1800:1900]), infperiodList[19] : Series(immuneList[1900:])} 

df1 = DataFrame(dsane)
df2 = DataFrame(dinfected)
df3 = DataFrame(dimmune)

#Pour la proportion max infectée de la population (ii)
dftotal3 = DataFrame({'Proportion max infectée' : df2.max()})

#Pour la durée de l'épidémie (i)
for i in range(0,20):
    count = 0
    for y in range(100*i,100*(i+1)):
        min = 0
        if(infectedList[y] == min and count < 1):
            listTime.append(y-(100*i))
            count += 1
    if(count == 0):
        listTime.append(99)

dftotal3['Durée Epidemie'] = Series(listTime, index=dftotal3.index)
dftotal3.to_csv('inf_period.csv')

listTime.clear()
casesList.clear()
saneList.clear()
infectedList.clear()
immuneList.clear()

#Question 4) : Impact de la durée de contagiosité

with open('res_contagperiod.txt', 'rt') as f:
    for line in f:
        if(r.search('contagion period', line)):
            c_p = line.split(' ')[1]
            contagperiodList.append(c_p)
        if(r.match('\d* \d* \d*', line)):
            casesList.append(line)

for i in casesList:
    sane = i.split(' ')[0]
    infected = i.split(' ')[1]
    immune = i.split(' ')[2]
    saneList.append(int(sane))
    infectedList.append(int(infected))
    immuneList.append(int(immune))

dsane = {contagperiodList[0] : Series(saneList[:100]), contagperiodList[1] : Series(saneList[100:200]), contagperiodList[2] : Series(saneList[200:300]),
    contagperiodList[3] : Series(saneList[300:400]), contagperiodList[4] : Series(saneList[400:500]), contagperiodList[5] : Series(saneList[500:600]),
    contagperiodList[6] : Series(saneList[600:700]), contagperiodList[7] : Series(saneList[700:800]), contagperiodList[8] : Series(saneList[800:900]),
    contagperiodList[9] : Series(saneList[900:1000]), contagperiodList[10] : Series(saneList[1000:1100]), contagperiodList[11] : Series(saneList[1100:1200]), 
    contagperiodList[12] : Series(saneList[1200:1300]), contagperiodList[13] : Series(saneList[1300:1400]), contagperiodList[14] : Series(saneList[1400:1500]),
    contagperiodList[15] : Series(saneList[1500:1600]), contagperiodList[16] : Series(saneList[1600:1700]), contagperiodList[17] : Series(saneList[1700:1800]),
    contagperiodList[18] : Series(saneList[1800:1900]), contagperiodList[19] : Series(saneList[1900:])} 

dinfected = {contagperiodList[0] : Series(infectedList[:100]), contagperiodList[1] : Series(infectedList[100:200]), contagperiodList[2] : Series(infectedList[200:300]),
    contagperiodList[3] : Series(infectedList[300:400]), contagperiodList[4] : Series(infectedList[400:500]), contagperiodList[5] : Series(infectedList[500:600]),
    contagperiodList[6] : Series(infectedList[600:700]), contagperiodList[7] : Series(infectedList[700:800]), contagperiodList[8] : Series(infectedList[800:900]),
    contagperiodList[9] : Series(infectedList[900:1000]), contagperiodList[10] : Series(infectedList[1000:1100]), contagperiodList[11] : Series(infectedList[1100:1200]), 
    contagperiodList[12] : Series(infectedList[1200:1300]), contagperiodList[13] : Series(infectedList[1300:1400]), contagperiodList[14] : Series(infectedList[1400:1500]),
    contagperiodList[15] : Series(infectedList[1500:1600]), contagperiodList[16] : Series(infectedList[1600:1700]), contagperiodList[17] : Series(infectedList[1700:1800]),
    contagperiodList[18] : Series(infectedList[1800:1900]), contagperiodList[19] : Series(infectedList[1900:])} 

dimmune = {contagperiodList[0] : Series(immuneList[:100]), contagperiodList[1] : Series(immuneList[100:200]), contagperiodList[2] : Series(immuneList[200:300]),
    contagperiodList[3] : Series(immuneList[300:400]), contagperiodList[4] : Series(immuneList[400:500]), contagperiodList[5] : Series(immuneList[500:600]),
    contagperiodList[6] : Series(immuneList[600:700]), contagperiodList[7] : Series(immuneList[700:800]), contagperiodList[8] : Series(immuneList[800:900]),
    contagperiodList[9] : Series(immuneList[900:1000]), contagperiodList[10] : Series(immuneList[1000:1100]), contagperiodList[11] : Series(immuneList[1100:1200]), 
    contagperiodList[12] : Series(immuneList[1200:1300]), contagperiodList[13] : Series(immuneList[1300:1400]), contagperiodList[14] : Series(immuneList[1400:1500]),
    contagperiodList[15] : Series(immuneList[1500:1600]), contagperiodList[16] : Series(immuneList[1600:1700]), contagperiodList[17] : Series(immuneList[1700:1800]),
    contagperiodList[18] : Series(immuneList[1800:1900]), contagperiodList[19] : Series(immuneList[1900:])} 

df1 = DataFrame(dsane)
df2 = DataFrame(dinfected)
df3 = DataFrame(dimmune)

#Pour la proportion max infectée de la population (ii)
dftotal4 = DataFrame({'Proportion max infectée' : df2.max()})

#Pour la durée de l'épidémie (i)
for i in range(0,20):
    count = 0
    for y in range(100*i,100*(i+1)):
        min = 0
        if(infectedList[y] == min and count < 1):
            listTime.append(y-(100*i))
            count += 1
    if(count == 0):
        listTime.append(99)

dftotal4['Durée Epidemie'] = Series(listTime, index=dftotal4.index)
dftotal4.to_csv('contag_period.csv')


listTime.clear()
casesList.clear()
saneList.clear()
infectedList.clear()
immuneList.clear()

#Question 5) : Impact de la durée d'immunité

with open('res_immunityperiod.txt', 'rt') as f:
    for line in f:
        if(r.search('immune period', line)):
            im_p = line.split(' ')[1]
            immuneperiodList.append(im_p)
        if(r.match('\d* \d* \d*', line)):
            casesList.append(line)

for i in casesList:
    sane = i.split(' ')[0]
    infected = i.split(' ')[1]
    immune = i.split(' ')[2]
    saneList.append(int(sane))
    infectedList.append(int(infected))
    immuneList.append(int(immune))

dsane = {immuneperiodList[0] : Series(saneList[:100]), immuneperiodList[1] : Series(saneList[100:200]), immuneperiodList[2] : Series(saneList[200:300]),
    immuneperiodList[3] : Series(saneList[300:400]), immuneperiodList[4] : Series(saneList[400:500]), immuneperiodList[5] : Series(saneList[500:600]),
    immuneperiodList[6] : Series(saneList[600:700]), immuneperiodList[7] : Series(saneList[700:800]), immuneperiodList[8] : Series(saneList[800:900]),
    immuneperiodList[9] : Series(saneList[900:1000]), immuneperiodList[10] : Series(saneList[1000:1100]), immuneperiodList[11] : Series(saneList[1100:1200]), 
    immuneperiodList[12] : Series(saneList[1200:1300]), immuneperiodList[13] : Series(saneList[1300:1400]), immuneperiodList[14] : Series(saneList[1400:1500]),
    immuneperiodList[15] : Series(saneList[1500:1600]), immuneperiodList[16] : Series(saneList[1600:1700]), immuneperiodList[17] : Series(saneList[1700:1800]),
    immuneperiodList[18] : Series(saneList[1800:1900]), immuneperiodList[19] : Series(saneList[1900:])} 

dinfected = {immuneperiodList[0] : Series(infectedList[:100]), immuneperiodList[1] : Series(infectedList[100:200]), immuneperiodList[2] : Series(infectedList[200:300]),
    immuneperiodList[3] : Series(infectedList[300:400]), immuneperiodList[4] : Series(infectedList[400:500]), immuneperiodList[5] : Series(infectedList[500:600]),
    immuneperiodList[6] : Series(infectedList[600:700]), immuneperiodList[7] : Series(infectedList[700:800]), immuneperiodList[8] : Series(infectedList[800:900]),
    immuneperiodList[9] : Series(infectedList[900:1000]), immuneperiodList[10] : Series(infectedList[1000:1100]), immuneperiodList[11] : Series(infectedList[1100:1200]), 
    immuneperiodList[12] : Series(infectedList[1200:1300]), immuneperiodList[13] : Series(infectedList[1300:1400]), immuneperiodList[14] : Series(infectedList[1400:1500]),
    immuneperiodList[15] : Series(infectedList[1500:1600]), immuneperiodList[16] : Series(infectedList[1600:1700]), immuneperiodList[17] : Series(infectedList[1700:1800]),
    immuneperiodList[18] : Series(infectedList[1800:1900]), immuneperiodList[19] : Series(infectedList[1900:])} 

dimmune = {immuneperiodList[0] : Series(immuneList[:100]), immuneperiodList[1] : Series(immuneList[100:200]), immuneperiodList[2] : Series(immuneList[200:300]),
    immuneperiodList[3] : Series(immuneList[300:400]), immuneperiodList[4] : Series(immuneList[400:500]), immuneperiodList[5] : Series(immuneList[500:600]),
    immuneperiodList[6] : Series(immuneList[600:700]), immuneperiodList[7] : Series(immuneList[700:800]), immuneperiodList[8] : Series(immuneList[800:900]),
    immuneperiodList[9] : Series(immuneList[900:1000]), immuneperiodList[10] : Series(immuneList[1000:1100]), immuneperiodList[11] : Series(immuneList[1100:1200]), 
    immuneperiodList[12] : Series(immuneList[1200:1300]), immuneperiodList[13] : Series(immuneList[1300:1400]), immuneperiodList[14] : Series(immuneList[1400:1500]),
    immuneperiodList[15] : Series(immuneList[1500:1600]), immuneperiodList[16] : Series(immuneList[1600:1700]), immuneperiodList[17] : Series(immuneList[1700:1800]),
    immuneperiodList[18] : Series(immuneList[1800:1900]), immuneperiodList[19] : Series(immuneList[1900:])} 

df1 = DataFrame(dsane)
df2 = DataFrame(dinfected)
df3 = DataFrame(dimmune)

#Pour la proportion max infectée de la population (ii)
dftotal5 = DataFrame({'Proportion max infectée' : df2.max()})

#Pour la durée de l'épidémie (i)
for i in range(0,20):
    count = 0
    for y in range(100*i,100*(i+1)):
        min = 0
        if(infectedList[y] == min and count < 1):
            listTime.append(y-(100*i))
            count += 1
    if(count == 0):
        listTime.append(99)

dftotal5['Durée Epidemie'] = Series(listTime, index=dftotal5.index)
dftotal5.to_csv('immune_period.csv')

listTime.clear()
casesList.clear()
saneList.clear()
infectedList.clear()
immuneList.clear()

#Question 6) : Impact de la densité de la population

with open('res_pop.txt', 'rt') as f:
    for line in f:
        if(r.search('nodes.$', line)):
            dens_p = line.split(' ')[1]
            densitepopList.append(dens_p)
        if(r.match('\d* \d* \d*', line)):
            casesList.append(line)

for i in casesList:
    sane = i.split(' ')[0]
    infected = i.split(' ')[1]
    immune = i.split(' ')[2]
    saneList.append(int(sane))
    infectedList.append(int(infected))
    immuneList.append(int(immune))

dsane = {densitepopList[0] : Series(saneList[:100]), densitepopList[1] : Series(saneList[100:200]), densitepopList[2] : Series(saneList[200:300]),
    densitepopList[3] : Series(saneList[300:400]), densitepopList[4] : Series(saneList[400:500]), densitepopList[5] : Series(saneList[500:600]),
    densitepopList[6] : Series(saneList[600:700]), densitepopList[7] : Series(saneList[700:800]), densitepopList[8] : Series(saneList[800:900]),
    densitepopList[9] : Series(saneList[900:1000]), densitepopList[10] : Series(saneList[1000:1100]), densitepopList[11] : Series(saneList[1100:1200]), 
    densitepopList[12] : Series(saneList[1200:1300]), densitepopList[13] : Series(saneList[1300:1400]), densitepopList[14] : Series(saneList[1400:1500]),
    densitepopList[15] : Series(saneList[1500:1600]), densitepopList[16] : Series(saneList[1600:1700]), densitepopList[17] : Series(saneList[1700:1800]),
    densitepopList[18] : Series(saneList[1800:1900]), densitepopList[19] : Series(saneList[1900:])} 

dinfected = {densitepopList[0] : Series(infectedList[:100]), densitepopList[1] : Series(infectedList[100:200]), densitepopList[2] : Series(infectedList[200:300]),
    densitepopList[3] : Series(infectedList[300:400]), densitepopList[4] : Series(infectedList[400:500]), densitepopList[5] : Series(infectedList[500:600]),
    densitepopList[6] : Series(infectedList[600:700]), densitepopList[7] : Series(infectedList[700:800]), densitepopList[8] : Series(infectedList[800:900]),
    densitepopList[9] : Series(infectedList[900:1000]), densitepopList[10] : Series(infectedList[1000:1100]), densitepopList[11] : Series(infectedList[1100:1200]), 
    densitepopList[12] : Series(infectedList[1200:1300]), densitepopList[13] : Series(infectedList[1300:1400]), densitepopList[14] : Series(infectedList[1400:1500]),
    densitepopList[15] : Series(infectedList[1500:1600]), densitepopList[16] : Series(infectedList[1600:1700]), densitepopList[17] : Series(infectedList[1700:1800]),
    densitepopList[18] : Series(infectedList[1800:1900]), densitepopList[19] : Series(infectedList[1900:])} 

dimmune = {densitepopList[0] : Series(immuneList[:100]), densitepopList[1] : Series(immuneList[100:200]), densitepopList[2] : Series(immuneList[200:300]),
    densitepopList[3] : Series(immuneList[300:400]), densitepopList[4] : Series(immuneList[400:500]), densitepopList[5] : Series(immuneList[500:600]),
    densitepopList[6] : Series(immuneList[600:700]), densitepopList[7] : Series(immuneList[700:800]), densitepopList[8] : Series(immuneList[800:900]),
    densitepopList[9] : Series(immuneList[900:1000]), densitepopList[10] : Series(immuneList[1000:1100]), densitepopList[11] : Series(immuneList[1100:1200]), 
    densitepopList[12] : Series(immuneList[1200:1300]), densitepopList[13] : Series(immuneList[1300:1400]), densitepopList[14] : Series(immuneList[1400:1500]),
    densitepopList[15] : Series(immuneList[1500:1600]), densitepopList[16] : Series(immuneList[1600:1700]), densitepopList[17] : Series(immuneList[1700:1800]),
    densitepopList[18] : Series(immuneList[1800:1900]), densitepopList[19] : Series(immuneList[1900:])} 

df1 = DataFrame(dsane)
df2 = DataFrame(dinfected)
df3 = DataFrame(dimmune)

#Pour la proportion max infectée de la population (ii)
dftotal6 = DataFrame({'Proportion max infectée' : df2.max()})

#Pour la durée de l'épidémie (i)
for i in range(0,20):
    count = 0
    for y in range(100*i,100*(i+1)):
        min = 0
        if(infectedList[y] == min and count < 1):
            listTime.append(y-(100*i))
            count += 1
    if(count == 0):
        listTime.append(99)

dftotal6['Durée Epidemie'] = Series(listTime, index=dftotal6.index)
dftotal6.to_csv('densite_pop.csv')