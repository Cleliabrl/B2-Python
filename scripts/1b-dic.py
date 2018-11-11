#!/usr/bin/python3.6
# nom : 1b-dic.py
# auteur : BURLE Clélia
# Afficher liste de prénom par ordre alphabétique :w

#FONCTIONS
#Saisie et sortie avec "q" 
def saisiePrenom(ma_liste):
	prenom = input('Entre un prénom : ')
	while prenom != 'q' : 
		ma_liste.append(prenom)
		prenom = input('Entre un prénom : ')
	return ma_liste

#Affiche la liste
def afficheListe(ma_liste) :
	for name in ma_liste: 
		print(name) 


#VARIABLES
ma_liste=[]

saisiePrenom(ma_liste) 
print(sorted(ma_liste)) #Liste les prénoms par ordre alphabétique
	 
 


 










				
