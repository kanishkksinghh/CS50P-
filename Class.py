class Student:
    def __init__(self, name, house): 
        if not name:
            raise ValueError("Missing Value")
        if house not in ["Vikas", "GomtiNagar", "Lucknow"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

    # This controls what prints when you print the object directly
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student) 

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
