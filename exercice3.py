from pandas import *
from matplotlib import pyplot

#1) Analyse pour le nombre de noeuds initiaux infectés

df_infnodes = read_csv('infectedNodes.csv')

a = df_infnodes["Noeuds initiaux infectés"]
b = df_infnodes["Proportion max infectée"]
c = df_infnodes["Durée Epidemie"]
d = df_infnodes["Distribution Multi-Infections"]

#Histogramme de l'évolution des multi infections selon la quantité des noeuds initiaux infectés
pyplot.figure(1)
pyplot.bar(a, d, align = 'center')
pyplot.xlabel('Noeuds initiaux infectés')
pyplot.ylabel('Moyenne multi-infections pour 100 noeuds')
pyplot.title("Multi-Infections")

#Graphique de l'évolution de la proportion max infectée/durée de l'épidémie selon la quantité de noeuds initiaux infectés
pyplot.figure(2)
pyplot.plot(a, b, label='Proportion Max Infectée')
pyplot.plot(a, c, label='Durée Epidemie')
pyplot.xlabel('Noeuds initiaux infectés')
pyplot.title('Proportion Max Infectée/Durée Epidemie')
pyplot.legend()


#2) Analyse pour le rayon de mobilité

df_travel = read_csv('travel_distance.csv')

a = df_travel["Rayon de mobilité"]
b = df_travel["Proportion max infectée"]
c = df_travel["Durée Epidemie"]
d = df_travel["Distribution Multi-Infections"]

#Histogramme de l'évolution des multi infections selon le rayon de mobilité
pyplot.figure(3)
pyplot.bar(a, d, align = 'center')
pyplot.xlabel('Rayon de mobilité')
pyplot.ylabel('Moyenne multi-infections pour 100 noeuds')
pyplot.title("Multi-Infections")

#Graphique de l'évolution de la proportion max infectée/durée de l'épidémie selon le rayon de mobilité
pyplot.figure(4)
pyplot.plot(a, b, label='Proportion Max Infectée')
pyplot.plot(a, c, label='Durée Epidemie')
pyplot.xlabel('Rayon de mobilité')
pyplot.title('Proportion Max Infectée/Durée Epidemie')
pyplot.legend()



#3) Analyse pour la durée de contagiosité

df_contag = read_csv('contag_period.csv')

a = df_contag["Durée de contagiosité"]
b = df_contag["Proportion max infectée"]
c = df_contag["Durée Epidemie"]
d = df_contag["Distribution Multi-Infections"]

#Histogramme de l'évolution des multi infections selon la durée de contagiosité
pyplot.figure(5)
pyplot.bar(a, d, align = 'center')
pyplot.xlabel('Durée de contagiosité')
pyplot.ylabel('Moyenne multi-infections pour 100 noeuds')
pyplot.title("Multi-Infections")

#Graphique de l'évolution de la proportion max infectée/durée de l'épidémie selon la durée de contagiosité
pyplot.figure(6)
pyplot.plot(a, b, label='Proportion Max Infectée')
pyplot.plot(a, c, label='Durée Epidemie')
pyplot.xlabel('Durée de contagiosité')
pyplot.title('Proportion Max Infectée/Durée Epidemie')
pyplot.legend()



#4) Analyse pour la durée d'infection

df_inf = read_csv('inf_period.csv')

a = df_inf["Durée Infection"]
b = df_inf["Proportion max infectée"]
c = df_inf["Durée Epidemie"]
d = df_inf["Distribution Multi-Infections"]

#Histogramme de l'évolution des multi infections selon la durée d'infection
pyplot.figure(7)
pyplot.bar(a, d, align = 'center')
pyplot.xlabel('Durée Infection')
pyplot.ylabel('Moyenne multi-infections pour 100 noeuds')
pyplot.title("Multi-Infections")

#Graphique de l'évolution de la proportion max infectée/durée de l'épidémie selon la durée d'infection
pyplot.figure(8)
pyplot.plot(a, b, label='Proportion Max Infectée')
pyplot.plot(a, c, label='Durée Epidemie')
pyplot.xlabel('Durée Infection')
pyplot.title('Proportion Max Infectée/Durée Epidemie')
pyplot.legend()



#5) Analyse pour la durée d'immunité

df_immune = read_csv('immune_period.csv')

a = df_immune["Durée Immunité"]
b = df_immune["Proportion max infectée"]
c = df_immune["Durée Epidemie"]
d = df_immune["Distribution Multi-Infections"]

#Histogramme de l'évolution des multi infections selon la durée d'immunité
pyplot.figure(9)
pyplot.bar(a, d, align = 'center')
pyplot.xlabel('Durée Immunité')
pyplot.ylabel('Moyenne multi-infections pour 100 noeuds')
pyplot.title("Multi-Infections")

#Graphique de l'évolution de la proportion max infectée/durée de l'épidémie selon la durée d'immunité
pyplot.figure(10)
pyplot.plot(a, b, label='Proportion Max Infectée')
pyplot.plot(a, c, label='Durée Epidemie')
pyplot.xlabel('Durée Immunité')
pyplot.title('Proportion Max Infectée/Durée Epidemie')
pyplot.legend()



#6) Analyse pour la densité de la population

df_pop = read_csv('densite_pop.csv')

a = df_pop["Densité de la population"]
b = df_pop["Proportion max infectée"]
c = df_pop["Durée Epidemie"]
d = df_pop["Distribution Multi-Infections"]

#Histogramme de l'évolution des multi infections selon la densité de la population
pyplot.figure(11)
pyplot.bar(a, d, align = 'center')
pyplot.xlabel('Densité de la population')
pyplot.ylabel('Moyenne multi-infections')
pyplot.title("Multi-Infections")

#Graphique de l'évolution de la proportion max infectée/durée de l'épidémie selon la densité de la population
pyplot.figure(12)
pyplot.plot(a, b, label='Proportion Max Infectée')
pyplot.plot(a, c, label='Durée Epidemie')
pyplot.xlabel('Densité de la population')
pyplot.title('Proportion Max Infectée/Durée Epidemie')
pyplot.legend()


#Affichage de tous les graphiques
pyplot.show()