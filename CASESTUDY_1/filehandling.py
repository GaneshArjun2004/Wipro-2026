import json
import csv

def save_students_json(students):
    with open("students.json", "w") as f:
        json.dump([vars(s) for s in students], f, indent=4)
    print("Student data successfully saved to students.json")

def generate_csv(students):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID","Name","Department","Average","Grade"])
        for s in students:
            avg = sum(s.marks) / len(s.marks)
            grade = "A" if avg >= 85 else "B"
            writer.writerow([s.pid, s.name, s.department, round(avg,2), grade])
