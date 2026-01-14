from getconn import get_connection
from error_handling import *

def add_appointment():
    conn = get_connection()
    cur = conn.cursor() 
    print("\n adding appointment......\n")
    patient_name = get_string("Enter the patient name: ")
    patient_id = get_int("Enter Patient ID: ")
    patient_contact = get_contact("Enter Patient Contact Number: ")
    doctor_name = get_string("Enter the doctor name: ")
    doctor_id = get_int("Enter Doctor ID: ")
    appointment_date = get_date("Enter Appointment Date (YYYY-MM-DD): ")
    appointment_time = input("Enter Appointment Time (HH:MM): ")    
    cur.execute("INSERT INTO appointment (patient_name,patient_id,patient_contact,doctor_name, doctor_id, appointment_date, appointment_time) VALUES (%s,%s,%s, %s,%s, %s, %s)", 
                (patient_name ,patient_id, patient_contact, doctor_name, doctor_id, appointment_date, appointment_time))
    conn.commit()
   
    print("\nAppointment added successfully.")



def delete_appointment():
    conn = get_connection()
    cur = conn.cursor()

    appointment_id = get_int("Enter Appointment ID to delete: ")

    cur.execute("""
        SELECT p.name
        FROM appointment a
        JOIN patients p ON a.patient_id = p.patient_id
        WHERE a.appointment_id = %s
    """, (appointment_id,))
    result = cur.fetchone()

    if not result:
        print(" Appointment not found.")
        return

    patient_name = result[0]
    cur.execute("DELETE FROM appointment WHERE appointment_id = %s", (appointment_id,))
    conn.commit()
    print(f" Appointment for patient '{patient_name}' deleted successfully.")


def view_appointments():
    conn = get_connection()
    cur = conn.cursor()
    print("appointments list ....")   
    cur.execute("select * from appointment")
    appointments = cur.fetchall()
    for appointment in appointments:    
        print(appointment)    



def search_appointment():
    conn  = get_connection()    
    cur = conn.cursor()
    print("how you want to search a appointment...? ")
    print("1. by a patient id ")    
    print("2. by a name of patient")
 
    choice = input("enter your choice ( 1 , 2 ) :     ")
    if choice == '1':
        patient_id = input("enter the patient id to search : ")
        cur.execute("select * from appointment where patient_id = %s", (patient_id,))
        appointments = cur.fetchall()    
        for appointment in appointments:
            print(appointment)
    elif choice == '2':
        patient_name = input("enter the patient name to search : ")
        cur.execute("select * from appointment where patient_name = %s", (patient_name,))
        appointments = cur.fetchall()    
        for appointment in appointments:
            print(appointment)
    
    else:
        print("plese enter a valid choice.....")