class Student:  #Class
    def __int__(self, name, house):
        self.name = name
        self.house = []
    
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name:")
    house = input("house")
    student = Student(name, house)
    return student

#methods classes comes with certain methods

    

if __name__ == "__main__":
    main() 