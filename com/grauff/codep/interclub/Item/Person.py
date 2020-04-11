PERSON IDPERS="1913252" NUM_LICENSE="06482927" CHECK_LICENSE="1" LASTNAME="BARRIERE" FIRSTNAME="Léo" SEX="0" BIRTHDAY="1995-06-12" CATEGORY="Senior" NUM_EQUIPE="3">
         <CLASS_SINGLE LEVEL="R6" CPPH="154.76"/>
         <CLASS_DOUBLE
CLASS MIXTED


class Person:

    classement = {
        'N1': 11,
        'N2': 10,
        'N3' : 9,
        'R4' : 8,
        'R5' : 7,
        'R6' : 6,
        'D7' : 5,
        'D8' : 4,
        'D9' : 3,
        'P10' : 2,
        'P11' : 1,
        'P12' : 0
    }

    def __init__(self,id, numlicence,classementsimple,classementdouble,classementmixte):
        self._id=id
        self._numLicence=numlicence
        self._simple=classement[classementsimple]
        self._mx=classement[classementmixte]
        self._double=classement[classementdouble]

    def Classement(self,):

# 1 seul club dans la saison pour un joueur
# 1 joueur ayant joué 3 rencontres en pré régionale ne peut plus joué en départementale
# 1 seule équipe par journée

#defaut équipe
#défaut régionale