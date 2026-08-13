import json
class Student:
    def __init__(self, name, age, department, matric_no):
        self.name = name
        self.age = age 
        self.department = department
        self.matric_no = matric_no
    
    def introduce(self):
        print(
            f'My name is {self.name}. '
            f'I am studying {self.department}'
        )
    
    def display_info(self):
        #print("Inside display_info")
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Department: {self.department}')
        print(f'Matric Number: {self.matric_no}') \

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "department":  self.department,
           "matric_no": self.matric_no 
        }


def menu():
    print("===== Student Management System ===== " \
    "\n 1. Add student " \
    "\n 2. View Student " \
    "\n 3. Search student " \
    "\n 4. Update student" \
    "\n 5. Delete student " \
    "\n 6. Save students " \
    "\n 7. Exit")

    choice = int(input("Enter your choice: "))
    return choice

students = []

try:
    with open("Student_data.txt", "r") as file:
        data = json.load(file)
        for s in data:
            new_students = Student(
                s["name"],
                s["age"],
                s["department"],
                s["matric_no"]
            )
    students.append(new_students)

except FileNotFoundError:
    pass

while True: 
    
    saveChoice = menu()
    if saveChoice == 1:
        name = input("Enter student's name: ")
        age = input("Enter age: ")
        dept = input("Enter department: ")
        mat = input("Enter matric number: ")
        
        new_student = Student(name, age, dept, mat)
        students.append(new_student)
        print("Student added successfully!")

    elif saveChoice == 2:
        if not students:
            print("No students available.")
        else:
            for s in students:
                s.display_info()
                
    elif saveChoice == 3:
        getName = input("Enter student's name: ")
        found = False
        for s in students:
            if getName.lower() == s.name.lower():
                s.display_info()
                found = True
                break
        if not found:
            print("Student not found.")
    
    elif saveChoice == 4:
        getName = input("Enter student's name: ")
        for s in students:
            if getName.lower() == s.name.lower():
                new_name = input("New name: ")
                new_age = input("New age: ")
                new_department = input("New department: ")
                new_matric = input("New matric number: ")

                s.name = new_name
                s.age = new_age
                s.department = new_department
                s.matric_no = new_matric

                print("Student updated successfully!")
                break
        else:
            print("Student not found.")
    elif saveChoice == 5:
        getName = input("Enter student's name: ")
        found = False
        for s in students:
            if getName.lower() == s.name.lower():
                students.remove(s)
                print("Student deleted succesfully")
                found = True
                break
        else:
                print("Student not found!")
    elif saveChoice == 6:
        new_students_dict = []
        for s in students:
            s = s.to_dict()
            new_students_dict.append(s)

        with open("Student_data.txt", "w") as file:
            json.dump(new_students_dict, file, indent= 4)
            print("Data saved successfully!")

    elif saveChoice == 7:
        print("Goodbye!")
        break

