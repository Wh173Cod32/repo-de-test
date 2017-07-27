class Property:
    def __init__(self,user_place_of_residence):
        self._place_of_residence = user_place_of_residence
    def _get_place_of_residence(self):
        print("We have the permission to get the attribut")
        return self._place_of_residence
    def _set_place_of_residence(self,new_place_of_residence):
        print("We have the permission to modify the attribut")
        self._lieu_residence = new_place_of_residence
        return self._place_of_residence
    place_of_residence = property(_get_place_of_residence,_set_place_of_residence)


San_Francisco = Property("San_Francisco")
print(San_Francisco.place_of_residence)
