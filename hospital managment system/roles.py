
from patien import add_patient, view_patients, delete_patient , search_patient
from doctors import add_doctor, view_doctors, delete_doctor, search_doctor
from appointments import add_appointment ,delete_appointment, view_appointments, search_appointment
from department import add_dept, delete_dept, view_dept
from staff import *

def admin():
    while True :
        print("\nMenu:")
        print("1. add doctor")
        print("2. View Doctors")
        print("3. Delete Doctor")
        print("4. search Doctor ")
        print("5. add department...")
        print("6. view department ")
        print("7. delete department ")
        print("8. add staff : ")
        print("9. delete staff : ")
        print("10. view staff : ")
        print("11. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
           add_doctor()
        elif choice == '2':
            view_doctors()
        elif choice == '3':
            delete_doctor()
        elif choice == '4':
            search_doctor()
        elif choice == '5':
            add_dept()
        elif choice == '6': 
            view_dept()
        elif choice == '7':
            delete_dept()    
        elif choice == '8':
            add_staff()
        elif choice == '9':
            delete_staff()         
        elif choice == '10':        
            view_staff()  
        elif choice == '11':
          print("loging out............")
          return
           

def doctor():
    while True :
        print("\nMenu:")
        
        print("1. View Patients")
        print("2. Delete Patient")
        print("3. search Patient")
        print("4. delete apointment ")
        print("5. view apointment ")
        print("6. search apointment ")
        print("7. Exit")
        choice = input("enter your choice (1-7): ")
        if choice == '1':
            view_patients()
        elif choice == '2':
            delete_patient()
        elif choice == '3':
            search_patient()
        elif choice == '4':        
            delete_appointment()  
        elif choice == '5':
            view_appointments()  
        elif choice == '6':
            search_appointment() 
        elif choice == '7':
          print("loging out............")
          return

def receptionist():
    while True :
        print("\nMenu:")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Delete Patient")
        print("4. search Patient")
        print("5. add apointment ")
        print("6. delete apointment ")
        print("7. view apointment ")
        print("8. search apointment ")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")
        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            delete_patient()
        elif choice == '4':
            search_patient()
        elif choice == '5':
            add_appointment()         
        elif choice == '6':        
            delete_appointment()  
        elif choice == '7':
            view_appointments() 
        elif choice == '8':
            search_appointment()
        elif choice == '9':
            return 