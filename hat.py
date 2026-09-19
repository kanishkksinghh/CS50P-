import random

class Hat:
    houses = ["Gryffindor", "Ravenclaw"]
    
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
    
    
    
hat = Hat()
hat.sort("Harry")
