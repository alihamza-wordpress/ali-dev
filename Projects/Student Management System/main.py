students = []

def add_student():
    id = int(input("Enter id: "))
    name = (input("Enter name: "))
    age = int(input("Enter age: "))
    course = (input("Enter course: "))

    student = {
        "id": id,
        "name": name,
        "age":age,
        "course": course
    }

    students.append(student)
    print("Student added successfully\n")


def view_student():
    if len(students) == 0:
        print("No student found")
        return
    
    for s in students:
        print("ID", s["id"])
        print("Name", s["name"])
        print("Age", s["age"])
        print("Course", s["course"])
        print("__________________")
    print()


def search_student():
    choice = input("Search student by (1) id or (2) name: ")

    if choice == "1":
        id = int(input("Enter id: "))
        for s in students:
            if s["id"] == id:
                print("Student found")
                print(s)
                return
            else:
                print("Student not found")
    elif choice == "2":
        id = int(input("Enter name: "))
        for s in students:
            if s["name"] == name:
                print("Student found")
                print(s)
                return
            else:
                print("Student not found")
    else:
        print("invalid choice\n")

def update_student():
    id = int(input("Enter id to update: "))

    for s in students:
        if s["id"] == id:
            s["name"] = input("Enter new name: ")
            s["age"] = int(input("Enter new age: "))
            s["course"] = input("Enter new course: ")

            print("Student updated\n")
            return
        
    print("No student found\n")

def delete_student():
    id = int(input(" Enter id to delete: "))

    for s in students:
        if s["id"] == id:
            students.remove(s)
            print("Student deleted")

while True:
    print("__________________")
    print("1. add student")    
    print("2. view student")    
    print("3. Search student")    
    print("4. Update student")    
    print("5. Delete student")    
    print("6. exit")

    choice= input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Goodbye! You have successfully exit from the program. Enjoy your life")
        break
    else:
        print("invalid choice\n")