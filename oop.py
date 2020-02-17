class Dog():
    #Attribute
    species = 'Mamel'
    def __init__(self,name,breed,gender,spots):
        self.name=name
        self.breed=breed
        self.gender=gender
        self.spots=spots

    def bark(self):
        if self.breed=='husky':
            print("awooo! My name is {}".format(self.name))
        else:
            print("woof! My name is {}".format(self.name))

myDog=Dog('frankie','husky','M','False')
myDog.bark()
