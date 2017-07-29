import os

os.chdir("C:\Users\sacha\Desktop")

def fonction(*liste,**dictionnaire):
    print("Les paramètres non nommées sont : {}, et les paramètres nommées sont : {}".format(liste,dictionnaire))

class Personne:
    def __init__(self,first_name,name):
        self.first_name = first_name
        self.name = name
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
    def __init__(self,minutes,secondes):
        self.minutes = minutes
        self.secondes = secondes
     def __str__(self):
        return "{0:02}:{1:02}".format(self.minutes, self.secondes)

fonction(1,2,3,4,5,a=6,b=7,c=8,d=9,e=10)

fichier = open("fichier.txt","w")
fichier.write("Hello")
fichier.close()
Me = Personne("Sacha","Degoix")
Me.first_name = "Sushi"
print(Me)
