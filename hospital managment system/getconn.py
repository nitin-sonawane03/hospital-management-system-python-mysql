import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="***",      # Replace with your actual username
        password="*******",        # Replace with your actual password
        database="hospital_db"
    )
# print("connection created successfully...")