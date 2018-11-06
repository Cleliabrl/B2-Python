#!/usr/bin/python3.6
# nom : 1d-mol.py
# auteur : BURLE Clélia
# jeu du plus ou momins 

import random 
import re 


nombrerand = random.randint(0,100)
print(nombrerand)
saisie=input("Entre un nombre entre 0 et 100 : ")
note_regex=re.compile('^(([0-9])|(1[0-9])|100)$') 




def Goodbay(): 
	 print("Au revoir !  La réponse était : " + str(nombrerand))  


#def VerifSaisie(saisie): 
#	if (note_regex.match(saisie)):
#		saisie = int(saisie)
#		if (saisie > 100):
#			return False
#			print("Un nombre entre 0 ete 100 : " ) 		
#		else : 
#			return True 
#	else : 
#		return False


def SaisieSortie(saisie): 
	if (str(saisie) == q or str(saisie) == Q) : 
		exit()  




while (int(saisie) != nombrerand):
	if (int(saisie) < nombrerand): 
		print("C'est plus grand")
		saisie = input("Entre un nouveau nombre : ")
		SaisieSortie(saisie) 
	elif (int(saisie) > nombrerand):
		print("C'est plus petit")  
		saisie = input("Etre un nouveau nombre : ")
		SaisieSortie(saisie)  
print("Gachné ! La réponse était : " + str(nombrerand))  





 
