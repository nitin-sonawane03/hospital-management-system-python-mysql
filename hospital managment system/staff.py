from getconn import get_connection
from error_handling import *


def add_staff():
    conn = get_connection()
    cur = conn.cursor()
    name = get_string("enter the staff name :")
    id = get_int("enter the staff id : ")
    work = input("enter the staff work : ")
    working_houres = input("enter the staff working hours : ")
    cur.execute("INSERT INTO staff (id, name, work, working_houres) VALUES (%s, %s, %s, %s)", (id, name, work, working_houres))
    conn.commit()
    conn.close()

def delete_staff():
    conn = get_connection()
    cur = conn.cursor()
    print("1. delete staff by id : ")
    print("2. delete staff by name : ")
    choice =  input("enter your choice (1 or 2) : ")
    if choice == '1':
        staff_id = get_int("enter staff id to delete :")
        cur.execute("DELETE FROM staff WHERE staff_id = %s", (staff_id,))
        conn.commit()
        conn.close()
    elif choice == '2':         
        staff_name = get_string("enter staff name to delete :")
        cur.execute("DELETE FROM staff WHERE staff_name = %s", (staff_name,))   
        conn.commit()
        conn.close()
    else :
        print("invalid choice : ")
def view_staff():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM staff")
    staffs = cur.fetchall()
    for staff in staffs:
        print(staff)        