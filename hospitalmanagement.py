import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital_db"
)

cursor = db.cursor()

# Create the patients table if it doesn't already exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(40),
        age INT,
        disease VARCHAR(100)
    )
""")

def add_patient():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    disease = input("Enter patient's disease: ")

    query = "INSERT INTO patients (name, age, disease) VALUES (%s, %s, %s)"
    values = (name, age, disease)

    cursor.execute(query, values)
    db.commit()

    print("Patient added successfully.")

def view_patients():
    query = "SELECT * FROM patients"
    cursor.execute(query)

    # Fetch all rows from the last executed statement
    rows = cursor.fetchall()

    # Convert the data to a pandas DataFrame for better visualization
    df = pd.DataFrame(rows, columns=[i[0] for i in cursor.description])
    print(df)

def update_patient():
    patient_id = input("Enter the ID of the patient to update: ")
    new_disease = input("Enter the new disease: ")

    query = "UPDATE patients SET disease = %s WHERE id = %s"
    values = (new_disease, patient_id)

    cursor.execute(query, values)
    db.commit()

    print("Patient updated successfully.")

while True:
    print("1. Add patient")
    print("2. View patients")
    print("3. Update patient")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_patient()
    elif choice == '2':
        view_patients()
    elif choice == '3':
        update_patient()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
