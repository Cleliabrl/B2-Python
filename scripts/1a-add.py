#!/usr/bin/python3.6
# nom : 1a-add.py
# auteur : BURLE Clélia
# Affiche le résultat d'une addition 

import re 



def Addition(nbr1,nbr2) :  #Fonction qui additionne les deux nombres saisies  
	return int(nbr1) + int(nbr2)  

def VerifSaisie():  #Fonction qui vérifie si la saisie nbr1 est un nombre
	if regex.match(nbr1):
		return True
	else : 
		print("La saisie n'est pas un nombre") 



nbr1=0
nbr2=0 
regex=re.compile('^(([0-9])|(1[0-9])|100)$')



nbr1=input("Entrez un nombre :") 
nbr2=input("Entrez un deuxième nombre :") 



result=Addition(nbr1, nbr2)  #appel de la fonction Addition() dans le code
print(result)
  








 










				
