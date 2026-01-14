create database if not exists hospital_db;
use hospital_db;

CREATE TABLE if not exists patient (
patient_id int auto_increment primary key , 
name varchar(100) ,
age int ,
gender varchar(10), 
contact varchar(15), 
address varchar(200), 
admit_date date ,
daises text);

create table if not exists doctors (
patient_id int auto_increment primary key , 
name varchar(100) ,
age int ,
gender varchar(10) ,
contact varchar(15) ,
address varchar(200) ,
admit_date date ,
daises text
);


create table if not exists department(
dept_id int primary key , 
dept_name varchar(100) ,
doctors_id int
);

CREATE TABLE if not exists appointment (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    patient_name VARCHAR(100) NOT NULL,
    doctor_id INT NOT NULL,
    doctor_name VARCHAR(100) NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    patient_contact VARCHAR(15),
    status ENUM('Scheduled','Completed','Cancelled') DEFAULT 'Scheduled',
    
    CONSTRAINT fk_patient FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    CONSTRAINT fk_doctor FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);


CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(100),
    role VARCHAR(20)
);

create table staff(
name varchar(100),
id int primary key auto_increment,
work varchar(100),
working_houres varchar(10)
);