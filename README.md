# hospital-management-system-python-mysql
console based Hospital Management System Using Python and MySQL
Hospital Management System (HMS)

This is a console-based Hospital Management System developed using Python and MySQL.
The project is designed to handle basic hospital operations in an organized and secure manner.
It focuses on backend logic, database connectivity, role-based access, and input validation.

--------------------------------------------------

Project Description :

The Hospital Management System allows hospital staff to manage patients, doctors,
appointments, departments, and staff records efficiently through a menu-driven
console interface.,,,,,,

The system uses PyMySQL to connect Python with a MySQL database.
All major operations are handled using modular Python files and functions.
Proper input validation and error handling are implemented using try-except blocks
to prevent invalid data entry.

--------------------------------------------------

Features :

1. Role Based Login System
- Admin login
- Receptionist login
- Doctor login
- Each role has restricted access based on permissions

2. Patient Management
- Add new patient
- Search patient by ID or name
- Delete patient record
- View all patients

3. Doctor Management
- Add doctor details
- Search doctor
- Delete doctor record
- View all doctors

4. Appointment Management
- Add appointment
- Search appointment
- Delete appointment
- View all appointments

5. Department Management
- Add doctors to departments
- View department-wise doctors
- Delete department records

6. Staff Management
- Add staff details
- Delete staff records

7. Input Validation and Error Handling
- Prevents numeric values in name fields
- Validates age and contact number
- Handles invalid inputs gracefully
- Uses try-except blocks to avoid runtime crashes

--------------------------------------------------

Technologies Used :

- Programming Language: Python
- Database: MySQL
- Database Connector: PyMySQL
- Environment: Console / Terminal

--------------------------------------------------

Project Structure :

main.py               - Main menu and program flow  
login.py              - Role-based authentication  
patient.py            - Patient related operations  
doctor.py             - Doctor related operations  
appointment.py        - Appointment management  
department.py         - Department handling  
staff.py              - Staff management  
db_connection.py      - MySQL database connection  
validation.py         - Input validation functions  

--------------------------------------------------

Database Details :

The project uses a MySQL database with tables such as:
- patients
- doctors
- appointments
- departments
- staff
- users (for login and roles)

All database operations are performed using parameterized queries
to avoid SQL injection.

--------------------------------------------------

How to Run the Project :

1. Install Python on your system
2. Install MySQL and create the required database
3. Install PyMySQL using:
   pip install pymysql
4. Update database credentials in db_connection.py
5. Run the project using:
   python main.py

--------------------------------------------------

Future Enhancements

- GUI version using Tkinter or Web framework
- Password encryption
- Advanced appointment scheduling
- Report generation
- Logging system

--------------------------------------------------

project Type: Academic / Learning Project
