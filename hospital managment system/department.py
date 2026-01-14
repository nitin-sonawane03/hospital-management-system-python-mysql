from getconn import get_connection
from error_handling import *


def add_dept():
    conn = get_connection()
    cur = conn.cursor()
    name = get_string("enter the dpartment name : ")
    id = get_int('enter the department id : ')
    cur.execute("INSERT INTO department VALUES (%s, %s)", (id, name))
    conn.commit()
    conn.close()

def delete_dept():
    conn =  get_connection()
    cur = conn.cursor()
    print("1. delete department by id ")
    print("2. delete department by name ")
    choice = input("enter your choice (1 or 2): ")
    if choice == '1':
        dept_id = get_int("enter department id to delete: ")
        cur.execute("DELETE FROM department WHERE dept_id = %s", (dept_id,))
    elif choice == '2':
        dept_name = get_string("enter department name to delete: ")
        cur.execute("DELETE FROM department WHERE dept_name = %s", (dept_name,))
    conn.commit()
    conn.close()

def view_dept():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM department")
    departments = cur.fetchall()
    for dept in departments:
        print(dept)
    conn.close()      
