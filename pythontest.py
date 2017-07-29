import os

def fonction(*liste,**dictionnaire):
    print("Les paramètres non nommées sont : {}, et les paramètres nommées sont : {}".format(liste,dictionnaire))

class Personne:
    #Classe
    def __init__(self,first_name,name):
        self._first_name = first_name
        self._name = name
    def _get_name(self):
        return self.name
    def _set_name(self,new_name):
        self.name = new_name
        return self.name
    name = property(_get_name,_set_name)
    def _get_first_name(self):
        return self.first_name
    def _set_first_name(self,new_first_name):
        self.first_name = new_first_name
        return self.first_name
    first_name = property(_get_first_name,_set_first_name)
    def __del__(self):
        print("Vous avez supprimé votre objet")
    def __repr__(self):
        return "{} {}".format(self.first_name,self.name)
    def __str__(self):
        return "{}".format(self.first_name,self.name)
    def __getattr__(self,attribut):
        print("L'attribut {} n'existe pas".format(self.attribut))
    def __setattr__(self,attribut,nouvelAttribut):
        object.__setattr__(self,attribut,nouvelAttribut)

class Zdict:
    def __init__(self,name):
        self.name = name

class Duree:
    #Classe permettant d'afficher des minutes et des secondes
    def __init__(self,minutes,secondes):
        self.minutes = minutes
        self.secondes = secondes
    def __str__(self):
        return "{0:02}:{1:02}".format(self.minutes, self.secondes)

class Compteur:
    compteur_objet = 0
    def __init__(self,name):
        Compteur.compteur_objet += 1
        self.name = name

class Temp:
    #Classe avec des attributs temporaires
    def __init__(self):


fonction(1,2,3,4,5,a=6,b=7,c=8,d=9,e=10)

fichier = open("fichier.txt","w")
fichier.write("Hello")
fichier.close()
Me = Personne("Sacha","Degoix")
Me.first_name = "Sushi"
print(Me)

test = Compteur("Test")
print(test.compteur_objet)
test2 = Compteur("Test2")
print(test.compteur_objet)
print(test.compteur_objet)
