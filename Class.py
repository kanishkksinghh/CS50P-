class Student:
    def __init__(self, name, house, local_area): 
        if not name:
            raise ValueError("Missing Value")
        if house not in ["Vikas", "GomtiNagar", "Lucknow"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.local_area = local_area

    # This controls what prints when you print the object directly
    def __str__(self):
        return f"{self.name} from {self.house} also {self.local_area}"
    def charm(self):
        match self.local_area:
            case "Dayal":
                return "hehe"
            case "VV":
                return "blup blup"
            

def main():
    student = get_student()
    print("Excepto Area!")
    print(student.charm()) 

def get_student():
    name = input("Name: ")
    house = input("House: ")
    local_area = input("Local Area: ")
    return Student(name, house, local_area)

if __name__ == "__main__":
    main()
