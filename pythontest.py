def fonction(*liste,**dictionnaire):
    print("Les paramètres non nommées sont : {}, et les paramètres nommées sont : {}".format(liste,dictionnaire))

fonction(1,2,3,4,5,a=6,b=7,c=8,d=9,e=10)
