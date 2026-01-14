from getconn import get_connection
from error_handling import *

def add_doctor():
    conn = get_connection()
    cur = conn.cursor()
    print("\n adding doctor..............\n")
    name = get_string("enter the name of doctor : ")
    doctor_id = get_int("enter the id of doctor : ")
    address = input("enter the address of doctor :")
    specilise = input("enter the doctor specilise : ")
    phone =  get_contact("enter the phone number of doctor :")
    age = get_int("enter the age of doctor : ")
    join_date = get_date("enter the join date of doctor (YYYY-MM-DD) : ")
    cur.execute("insert into doctors (name , doctor_id,address, specilise , phone,age,join_date) values (%s, %s, %s,%s, %s, %s, %s)", (name, doctor_id ,address, specilise, phone, age, join_date))
    conn.commit()
    print("doctor added successufully.......")

def view_doctors():
    conn = get_connection()
    cur = conn.cursor()
    print("List of Doctors:")
    cur.execute("select * from doctors")
    doctors = cur.fetchall()
    for doctor in doctors:
        print(doctor)


def delete_doctor():
    conn = get_connection()
    cur = conn.cursor()
    print("\nhow you want to delete a doctor...? ")
    print("1. by a name ")
    print("2. by a id  ")
    choice = input("enter your coice (1 or 2) : ")
    if choice == '1':
        name = get_string("enter the name of doctor to delete : ")
        cur.execute("delete from doctors where name = %s", (name,))
        conn.commit()
        print("doctor deleted successfully.......\n")     
    elif choice == '2':
        doctor_id = get_int("enter the id of doctor to delete : ")
        cur.execute("delete from doctors where doctor_id = %s", (doctor_id,))
        conn.commit()
        print("doctor deleted successfully......\n.") 
    else:
        print("please enter a valid choice .....")

def search_doctor():
    conn = get_connection()
    cur = conn.cursor()
    print("\nhow you want to search a doctor...? ")
    print("1. by a name ")
    print("2. by a id  ")
    choice = input("enter ypue chice (1 or 2) : ")
    if choice =='1':
        name = input("enter the name of doctor to search : ")
        cur.execute("select * from doctors where name = %s", (name,))
        doctors = cur.fetchall()    
        for doctor in doctors:
            print(doctor)   
    elif choice == '2':
        doctor_id = input("enter the id of doctor to search : ")
        cur.execute("select * from doctors where doctor_id = %s", (doctor_id,))
        doctors = cur.fetchall()    
        for doctor in doctors:
            print(doctor)
    else:
        print("Invalid choice.")

        


