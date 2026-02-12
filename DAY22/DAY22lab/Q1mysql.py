import mysql.connector

# ==========================================
# MYSQL CONNECTION
# ==========================================
try:
    mysql_conn = mysql.connector.connect(
        host="localhost",       
        user="root",            
        password="database",    
        database="company_db"
    )

    cursor = mysql_conn.cursor()
    print("Connected to MySQL successfully")

except Exception as e:
    print("MySQL connection failed:", e)
    exit()


# ==========================================
# 1. FETCH EMPLOYEES WITH SALARY > 50000
# ==========================================
try:
    fetch_query = "SELECT * FROM employees WHERE salary > 50000"
    cursor.execute(fetch_query)

    results = cursor.fetchall()

    print("\nEmployees earning more than 50,000:")
    for emp in results:
        print(emp)

except Exception as e:
    print("Error fetching data:", e)


# ==========================================
# 2. INSERT NEW EMPLOYEE RECORD
# ==========================================
try:
    insert_query = """
    INSERT INTO employees (name, department, salary)
    VALUES (%s, %s, %s)
    """

    new_employee = ("Ganesh", "IT", 70000)
    cursor.execute(insert_query, new_employee)

    mysql_conn.commit()
    print("\nNew employee inserted successfully")

except Exception as e:
    print("Error inserting employee:", e)


# ==========================================
# 3. UPDATE SALARY BY 10% FOR SPECIFIC EMPLOYEE
# ==========================================
try:
    emp_id = 1

    update_query = """
    UPDATE employees
    SET salary = salary * 1.10
    WHERE id = %s
    """

    cursor.execute(update_query, (emp_id,))
    mysql_conn.commit()

    print("\nEmployee salary updated by 10%")

except Exception as e:
    print("Error updating salary:", e)


# ==========================================
# CLOSE MYSQL CONNECTION
# ==========================================
cursor.close()
mysql_conn.close()
print("\nMySQL connection closed")
