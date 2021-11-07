from subprocess import run

#Simulations exécutées cette fois-ci pour chaque noeud individuellement, sert pour traiter l'exercice 2 (iii)


nb_infected = 0
rayon_mobilite = 10
duree_infection = 10
duree_contag = 10
duree_immunite = 10
nb_nodes = 1

#10 simulations en faisant varier le nombre initial d'infectés, en affichant l'état de chaque noeud
for i in range(10):
    res = run(['java', '-jar', 'Virus_old.jar', '-gui=0', '-nb_snapshots=100','-printout=2', f'-nb_infected={nb_infected}'], capture_output=True)
    nb_infected+=10 #on augmente le nombre d'infectés de 10 à chaque itération
    with open('multi_infected.txt', 'a') as f:
        f.write(res.stdout.decode('utf-8'))

#10 simulations en faisant varier le rayon de mobilité, en affichant l'état de chaque noeud
for i in range(10):
    res = run(['java', '-jar', 'Virus_old.jar', '-gui=0', '-nb_snapshots=100', '-printout=2', f'-travel_distance={rayon_mobilite}'], capture_output=True)
    rayon_mobilite+=50 #on augmente le rayon initial de 50 à chaque itération
    with open('multi_rayon.txt', 'a') as f:
        f.write(res.stdout.decode('utf-8'))

#20 simulations en faisant varier la durée d'infection, en affichant l'état de chaque noeud
for i in range(20):
    res = run(['java', '-jar', 'Virus_old.jar', '-gui=0', '-nb_snapshots=100', '-printout=2', f'-infection_period={duree_infection}'], capture_output=True)
    duree_infection+=10
    with open('multi_infectionperiod.txt', 'a') as f:
        f.write(res.stdout.decode('utf-8'))


#20 simulations en faisant varier la durée de contagiosité, en affichant l'état de chaque noeud
for i in range(20):
    res = run(['java', '-jar', 'Virus_old.jar', '-gui=0', '-nb_snapshots=100', '-printout=2', f'-contagion_period={duree_contag}'], capture_output=True)
    duree_contag+=10
    with open('multi_contagperiod.txt', 'a') as f:
        f.write(res.stdout.decode('utf-8'))

#20 simulations en faisant varier la durée d'immunité, en affichant l'état de chaque noeud
for i in range(20):
    res = run(['java', '-jar', 'Virus_old.jar', '-gui=0', '-nb_snapshots=100', '-printout=2', f'-immune_period={duree_immunite}'], capture_output=True)
    duree_immunite+=10
    with open('multi_immunityperiod.txt', 'a') as f:
        f.write(res.stdout.decode('utf-8'))

#20 simulations en faisant varier la densité de population, en affichant l'état de chaque noeud
for i in range(20):
    res = run(['java', '-jar', 'Virus_old.jar', '-gui=0', '-nb_snapshots=100', '-printout=2', f'-nb_nodes={nb_nodes}'], capture_output=True)
    nb_nodes+=5
    with open('multi_pop.txt', 'a') as f:
        f.write(res.stdout.decode('utf-8'))