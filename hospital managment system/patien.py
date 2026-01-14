from getconn import get_connection
from error_handling import *


def add_patient():
    conn = get_connection()
    cursor = conn.cursor()
    
    print("\nAdding a new patient:\n")
    name = get_string("Enter patient name: ")
    age = get_int("enter patient age : ")
    gender = get_gender("Enter patient gender: ")
    address = input("Enter patient address: ")
    phone = get_contact("Enter patient phone number: ")   
    daises = input("Enter patient diseases: ")
    a = input("is paiyent OPD or IPD...").upper()
    if a == "IPD":
         ward_no = input("Enter ward number: ")
         admit_date = get_date("Enter admit date (YYYY-MM-DD): ")
         cursor.execute("insert into patient (name, age, gender, address, contact, daises, ward_no, admit_date) values (%s, %s, %s, %s, %s, %s, %s, %s)", (name, age, gender, address, phone, daises, ward_no, admit_date))
         conn.commit()
         print("Patient added successfully.")
    else:
         cursor.execute("insert into patient (name, age, gender, address, contact, daises) values (%s, %s, %s, %s, %s, %s)", (name, age, gender, address, phone, daises))
         conn.commit()
         print("Patient added successfully.")

        

def view_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select * from patient")
    patients = cursor.fetchall()
    for patient in patients:
        print(patient)

def delete_patient():
    conn = get_connection()
    cursor = conn.cursor()
    patient_id = get_int("Enter patient ID to delete: ")
    cursor.execute("delete from patient where patient_id = %s", (patient_id,))
    conn.commit()
    print("Patient deleted successfully.") 


def search_patient():
    conn = get_connection()
    cur = conn.cursor()
    print("how do you want to search patient...?")
    print("1. By Name")
    print("2. By ID")
    choice = input("Enter choice (1 or 2): ")  
    if choice ==  '1':
        name = get_string("name of paitents : ")
        cur.execute("select * from patient where name =%s ", (name))
        patients = cur.fetchall()
        for patient in patients:
            print(patient)
    elif choice == '2':
        patient_id = get_int("ID of paitents : ")
        cur.execute("select * from patient where patient_id =%s ", (patient_id))
        patients = cur.fetchall()
        for patient in patients:
            print(patient)  
    else:
        print("Invalid choice.")        


