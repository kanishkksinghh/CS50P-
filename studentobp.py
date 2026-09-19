def main():
    student = get_student()
    if student[0] == "Kanishk":
        student[1] = "Vikas Khand"
    print(f"{student['name']} from {student['house']}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house] #[name, house] list mutable(can be changed)
# #(name, house) tuple

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
    

if __name__ == "__main__":
    main()