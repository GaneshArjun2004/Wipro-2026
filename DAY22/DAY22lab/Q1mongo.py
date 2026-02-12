from pymongo import MongoClient

# ==========================================
# CONNECT TO MONGODB (Compass / Local Server)
# ==========================================
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["company_db"]
    collection = db["employees"]

    print("Connected to MongoDB successfully")

except Exception as e:
    print("Connection failed:", e)
    exit()


# ==========================================
# INSERT NEW EMPLOYEE DOCUMENT
# ==========================================
try:
    new_employee = {
        "name": "Ganesh",
        "department": "IT",
        "salary": 75000
    }

    collection.insert_one(new_employee)
    print("\nEmployee inserted successfully")

except Exception as e:
    print("Insert failed:", e)


# ==========================================
# FIND ALL EMPLOYEES IN IT DEPARTMENT
# ==========================================
try:
    print("\nEmployees in IT Department:")

    employees = collection.find({"department": "IT"})
    for emp in employees:
        print(emp)

except Exception as e:
    print("Fetch failed:", e)


# ==========================================
# UPDATE SALARY OF EMPLOYEE BY NAME
# ==========================================
try:
    employee_name = "Ganesh"

    collection.update_one(
        {"name": employee_name},
        {"$set": {"salary": 90000}}
    )

    print("\nSalary updated successfully")

except Exception as e:
    print("Update failed:", e)


# ==========================================
# CLOSE CONNECTION
# ==========================================
client.close()
print("\nMongoDB connection closed")
