import mysql.connector
from db.private import DB_HOST,DB_PASSWORD,DB_USERNAME

sql = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database="krishna"
)

# Deals with Employee Management
class Employee():
    def add_employee(emp_id,emp_name,emp_phone,payment_amnt):
        "The Purpose of this function is to add a employee to the db"
        print("ool")
    def modify_employee():
        pass
    def delete_employee():
        pass
    # Reminder: Add in time and outime management systme (Multi In & Out)


class Sale():
    def add_sale():
        pass
    def modify_sale():
        pass
    def delete_sale():
        pass