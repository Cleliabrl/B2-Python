#!/usr/bin/python3.6
# nom : 1d-mol.py
# auteur : BURLE Clélia
# jeu du plus ou momins 

import random 
import re 


nombrerand = random.randint(0,100)
saisie = -1  
print(nombrerand) 

def VerifSaisie(saisie): 
	if (re.match('^[0-9]+$',saisie)):
		saisie = int(saisie) 
		if (saisie > 100):
			return False 		
		else : 
			return True 
	else : 
		return False

def SaisieSortie(saisie): 
	if (saisie == q or saisie == Q) : 
		exit()  

while (saisie != nombrerand):
	while (VerifSaisie(saisie) == False) : 
		saisie = input("ERREUR Saisir un nombre entre 1 et 100 : ") 
	if (saisie ==  nombrerand):
		print("Gagné") 
	elif (saisie < nombrerand): 
		print("C'est plus grand")
	elif (saisie > nombrerand):
		  print("C'est plus petit")  
				
