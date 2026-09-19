class Wizard: #parent class
    def __init__(self, name):
            if not name:
                raise ValueError("Missing name")
            self.name = name
            
    ...


class Sutdent(Wizard):    #child class
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
        
class Professor:
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        