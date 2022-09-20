#!/usr/local/bin/python3.10
from random import *


numChoisi = int(input("Sur quel numéro voulez-vous miser ? "))
sommeMisee = int(input("Quelle somme souhaitez-vous miser ? "))
numTirage = (randint(0, 49))

#pour les tests
5numTirage = 5

print("le numéro sorti est :" ,numTirage)
print("-------------")

#couleur sortie
if (numTirage % 2) == 0:
    couleurTirage = int(2)
    print("couleur noire")
else :
    couleurTirage = int(1)
    print("couleur rouge")

#couleur choisi
if (numChoisi % 2) == 0:
    couleurChoisi = int(2)
    print("couleur noire")
else :
    print("couleur rouge")
    couleurChoisi = int(1)


print("-------------")
print("numéro choisi :" ,numChoisi)
print("numéro sorti :" ,numTirage)
print("-------------")

if numChoisi == numTirage :
    print("vous avez gagné :" ,sommeMisee*3)
elif (couleurTirage == couleurChoisi):
    print("même couleur !")
    print("le croupié vous donne" ,sommeMisee * 1.5)
else :
    print("vous avez perdu " ,sommeMisee)
