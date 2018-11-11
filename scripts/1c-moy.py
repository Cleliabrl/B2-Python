#!/usr/bin/python3.6
# nom : 1c-moy.py
# auteur : BURLE Clélia
# Moyenne et top 5 de note   

#IMPORTS
import operator



#FONCTIONS
#fonction qui vérifie la saisie nombre
def verifSaisie():
	note = input('Entre une note :') 
	while (note.isdigit() is False):
		note = input('Entre un vrai note : ') 
	return int(note) 



#fonction saisie
def saisie(dict):
	prenom=' ' 
	note=0
	while name != 'q' : 
		prenom = input('Entre un prénom : ')
		if prenom != 'q' : 
			note = verifSaisie() 
			dict[prenom] = note
		return dict
	

#fonction calcul moyenne
def calculMoy(total_note, nbr_note):
	moy = (total_note / nbr_note)
	return moy


#fonction affiche moyenne 
def moyenne(dict) : 
	total_note = 0 
	nbr_note = 0 
	for name, note in dict.items(): 
		nbr_note += 1
		total_note += note
	print('La moyenne est de : '+ calculMoy(total_note, nbr_note) 



#VARIABLES
dict = {}  
 

#CODE 
saisie(dict) 













mon_dictionnaire = {} 
saisie = 0 

mon_dictionnaire["prénom"] = input("entre un prenom : ") 
mon_dictionnaire["note"] = input("entre une note : " )  

print (mon_dictionnaire) 
#while (prenom =! q) : 
#	prenom=input("Entre un prénom : ") 
#	note=int(input("Entre une note : "))
 
 
	 








 










				
