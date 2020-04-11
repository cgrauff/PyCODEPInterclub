import xml.etree.ElementTree as ET
import os
#import com.grauff.codep.interclub.Item.Club as Team

Club=dict()
MatchNumber=dict()
TeamNumber=dict()

folder='DataFile/'
for file in os.listdir(folder):
    if 'xml' in file :
        print(file)
        tree = ET.parse(folder + file)
        root = tree.getroot()
        print(root.tag)
#        for club in root.findall('CLUB'):
#            idClub=club.get('IDCLUB')
#            if idClub not in Club:
#                Club[idClub]=Team(idClub,club.get('ACRONYM'))
#            for person in club.findall('PERSON'):
#                idjoueur=person.get('IDPERS')
#                licence=person.get('NUM_LICENSE')
#                csimple=person.find('CLASS_SINGLE').get('LEVEL')
#                cdouble=person.find('CLASS_DOUBLE').get('LEVEL')
#                cmixte=person.find('CLASS_MIXED').get('LEVEL')
#        for rencontre in root.findall('ROUND'):
#            for game in rencontre.findall('MATCH'):
#                for pair in game.findall('PAIR'):
#                    for player in pair.findall('')


#Creation du club si il n'existe pas
#pour chaque club création de l'équipe si n'existe pas
#pour chaque équipe création d'un joueur


#1 seul club dans la saison pour un joueur
#1 joueur ayant joué 3 rencontres en pré régionale ne peut plus joué en départementale
#pas plus de 2 joueurs mutés dans une équipe lors d'une rencontre
#Valeur d'équipe à respecter ; N1 12, N2 11, N3 10, R4 9, R5 8, R6 7, D7 6, D8 5, D9 4, P10 3, P11 2, P12 1, NC 0 (3 H/2 F OU 4H)
#Hiéarchie des joueurs
#1 seule équipe par journée
#nombre de montée illimitée
#nombre de descente 1
