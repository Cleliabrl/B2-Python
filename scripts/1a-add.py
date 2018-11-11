#!/usr/bin/python3.6
# nom : 1a-add.py
# auteur : BURLE Clélia
# Affiche le résultat d'une addition 


#IMPORTS

import re 


#FONCTIONS


# fonction qui additionne les deux nombres
def addition(nbr1,nbr2) : 
	return int(nbr1) + int(nbr2)  


# fonction qui vérifie la saisie
def verifSaisie(nbr_regex): 
	nb = input('Entre un nombre : ') 
	while not nbr_regex.match(nb) : 
		nb = input('Entre un vrai nombre : ') 
	return int(nb) 


#VARIABLES

nbr1=0
nbr2=0 
nbr_regex = re.compile('^[0-9]+$') 



nbr1 = verifSaisie(nbr_regex)
nbr2 = verifSaisie(nbr_regex) 
 
  
print(addition(nbr1,nbr2)) 







 










				
