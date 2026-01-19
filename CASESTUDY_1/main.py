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
            sid = input()
            name = input()
            dept = input()
            sem = int(input())
            marks = list(map(int, input().split()))
            students.append(Student(sid, name, dept, sem, marks))
            print("Student Created Successfully")

        elif choice == "2":
            fid = input()
            name = input()
            dept = input()
            sal = int(input())
            faculty_list.append(Faculty(fid, name, dept, sal))
            print("Faculty Created Successfully")

        elif choice == "3":
            code = input()
            cname = input()
            credits = int(input())
            fid = input()
            fac = next(f for f in faculty_list if f.pid == fid)
            courses.append(Course(code, cname, credits, fac))
            print("Course Added Successfully")

        elif choice == "5":
            students[0].calculate_performance()

        elif choice == "6":
            print(students[0] > students[1])

        elif choice == "7":
            for s in student_generator(students):
                print(s)
            generate_csv(students)
            save_students_json(students)

        elif choice == "8":
            print("Thank you for using Smart University Management System")
            break

    except Exception as e:
        print("Error:", e)
