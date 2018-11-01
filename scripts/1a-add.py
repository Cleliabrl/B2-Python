#!/usr/bin/python3.6
# nom : 1a-add.py
# auteur : BURLE Clélia
# Affiche le résultat d'une addition 

import re 



def Addition(nbr1,nbr2) :  #Fonction qui additionne les deux nombres saisies  
	return (nbr1) +(nbr2)  

def VerifSaisie(nbr1,nbr2):  #Fonction qui vérifie si la saisie nbr1 est un nombre
	if nbr_regex.match(nbr1):
		return True
	else : 
		print("La première saisie n'ai pas un nombre") 
		exit()
	if nbr_regex.match(nbr2): 
		return True 
	else : 
		print("La deuxieme saisie n'est pas un nombre") 
		exit()


nbr1=0
nbr2=0 
nbr_regex = re.compile('^(([0-9])|(1[0-9])|100)$')



nbr1=input("Entrez un nombre :")
nbr2=input("Entrez un deuxième nombre :") 


#if nbr_regex.match(nbr1):
#	print ("le nombre est entre 0 et 100")
#else : 
#	print("le nombre n'est pas entre 0 et 100") 

VerifSaisie(nbr1,nbr2) 

result=Addition(nbr1, nbr2)  #appel de la fonction Addition() dans le code
print(result)
  








 










				
