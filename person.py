class Person:
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def setAddress(self, address):
        self.address = address
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getAddress(self):
        return self.address
    
person = Person()

name = person.setName("Dharyl Duclisen")
age = person.setAge(20)
address = person.setAddress("La Trinidad, Benguet")

profile = f"""
    Person's Profile
    ----------------------------
    Name: {person.getName()}
    Age: {person.getAge()}
    Address: {person.getAddress()}
"""

print(profile)