from student import Student
from faculty import Faculty
from course import Course
from iterator import student_generator
from filehandling import save_students_json, generate_csv

students = []
faculty_list = []
courses = []

while True:
    print("\n1 Add Student\n2 Add Faculty\n3 Add Course\n4 Enroll\n5 Performance\n6 Compare\n7 Reports\n8 Exit")

    choice = input()

    try:
        if choice == "1":
            print("\n Enter Student Details")
            sid = input("Student ID: ")
            name = input("Student Name: ")
            dept = input("Department: ")
            sem = int(input("Semester: "))
            marks = list(map(int, input("Enter student marks: ").split()))

            students.append(Student(sid, name, dept, sem, marks))

            print("\nStudent details added")
            print("ID        :", sid)
            print("Name      :", name)
            print("Department:", dept)
            print("Semester  :", sem)

        elif choice == "2":
            print("\n...Enter Faculty Details....")
            fid = input("Faculty ID: ")
            name = input("Faculty Name: ")
            dept = input("Department: ")
            sal = int(input("Monthly Salary: "))

            faculty_list.append(Faculty(fid, name, dept, sal))

            print("\nFaculty added")
            print("ID        :", fid)
            print("Name      :", name)
            print("Department:", dept)

        elif choice == "3":
            print("\n....Enter Course Details....")
            code = input("Course Code: ")
            cname = input("Course Name: ")
            credits = int(input("Credits: "))
            fid = input("Faculty ID: ")

            fac = next(f for f in faculty_list if f.pid == fid)
            courses.append(Course(code, cname, credits, fac))

            print("\ncourse added")
            print("Course Code :", code)
            print("Course Name :", cname)
            print("Credits     :", credits)
            print("Faculty     :", fac.name)
        
        elif choice == "4":
            print('\n student enrolled')

        elif choice == "5":
            students[0].calculate_performance()

        elif choice == "6":
            print('\n compating students')
            print(students[0] > students[1])

        elif choice == "7":
            print('\n generated students')
            for s in student_generator(students):
                print(s)
            generate_csv(students)
            save_students_json(students)

        elif choice == "8":
            print("Thank you for using Smart University Management System")
            break

    except Exception as e:
        print("Error:", e)
