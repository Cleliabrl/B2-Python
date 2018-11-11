#!/usr/bin/python3.6
#nom : 2a-moy.py 
#auteur : BURLE Clélia
# Jeu du plus ou moins qui lit dans un fchier


#INPORTS
import re
import random 
import signal 


#FONCTIONS
#fonction qui écrit dans le fichier 
def ecriture(msg): 
	file = open(txt, "w") 
	file.write(msg)
	file.close() 


#fonction qui lit dans le fichier 
def lecture(): 
	file = open(txt, "r") 
	input = file.readline().strip()
	file.close() 
	return input 



#fonction qui vérifie la saisie 
def verifSaisie() : 
	nombre = lecture()
	while(nombre.isdigit() == False):
		nombre = lecture()
	return int(nombre) 


#fonction "plus" ou "moins"
def plusOuMoins() : 
	if (nbr_rand == essaie): 
		done=True
		return 'trouvé' 
	elif (essai < nbr_rand):
		return 'Trop petit' 
	else : 
		return 'trop grand' 


#fonction quitté CTRL C 
def ctrlC(sig, fram): 
	ecriture('Salut') 
	exit() 


signal.signal(signal.SIGINT,ctrlC)  






#VARIABLES
txt = "2a.txt" 
done = False 
nbr_rand = randint(1,100) 
essaie = -1 


ecriture('Bonjour, trouve le bon nombre entre 1 et 100') 

while(done is False and essaie != nbr_rand)
	essaie = verifSaisie() 
	resultat = plusOuMoins() 
	ecriture(resultat)
