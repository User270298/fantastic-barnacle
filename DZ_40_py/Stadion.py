class Stadion:
    def __init__(self, label, opening_year, country, town, сapacity):
        self.__label = label
        self.__opening_year = opening_year
        self.__country = country
        self.__town = town
        self.__сapacity = сapacity

    def get_label(self):
        return self.__label

    def set_label(self, value):
        self.__label = value

    def get_opening_year(self):
        return self.__opening_year

    def set_opening_year(self, value):
        self.__opening_year = value

    def get_country(self):
        return self.__country

    def set_country(self, value):
        self.__country = value

    def get_town(self):
        return self.__town

    def set_town(self, value):
        self.__town = value

    def get_сapacity(self):
        return self.__сapacity

    def set_сapacity(self, value):
        self.__сapacity = value


stadion = Stadion('Rostov Arena', '2018', 'Russia', 'Rostov-on-Don', '2345')
# 43 472
print(stadion.__dict__)
print(stadion.get_сapacity())
stadion.set_сapacity('43 472')
print(stadion.get_сapacity())
print(stadion.__dict__)
