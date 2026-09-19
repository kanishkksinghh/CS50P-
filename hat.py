import random

class Hat:
    def __int__(self):
        self.houses = ["Gryffindor", "Ravenclaw"]
    
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))
    
    
    
hat = Hat()
hat.sort("Harry")
