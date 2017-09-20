import spy_details

class Spy_Info:
    name = ""
    salutation = ""
    age = 0
    rating = 0.0
    status = True
    chats = []

    def __init__(self, salutation, name, age, rating, status):
        self.salutation = salutation
        self.name = name
        self.age = age
        self.rating = rating
        self.is_online = status

    def set_details(self, name, salutation, age, rating, status):
        self.name = name
        self.salutation = salutation
        self.rating = rating
        self.age = age
        self.status = True

    def displayDetails(self):
        print self.Name, " ", self.Age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_rating(self):
        return self.rating
    def get_salutation(self):
        return self.salutation
    def get_status(self):
        return self.True
    def get_chats(self):
        return self.chats
    def clear_chats(self):
        self.chats=[]