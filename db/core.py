import mysql.connector
from db.private import DB_HOST,DB_PASSWORD,DB_USERNAME # Add db.private when working outside

sql = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database="krishna"
)

# Deals with Employee Management
class Employee():
    def add_employee(*args,emp_id,emp_name,emp_phone,payment_amnt):
        "The Purpose of this function is to add a employee to the db"
        try:
            cursor = sql.cursor()
            cursor.execute(f"INSERT INTO employees VALUES ({emp_id},'{emp_name}','{emp_phone}',{payment_amnt});")
            sql.commit()
            cursor.close()
            return "Successfully Added"
        except:
            return "Failed - Employee exist"

    def modify_employee(*args,emp_id):
        pass
    
    def delete_employee(self,emp_id):
        try:
            cursor = sql.cursor()
            cursor.execute(f"DELETE FROM employees WHERE emp_id={emp_id};")
            sql.commit()
            cursor.close()
            return "Deleted Successfully"
        except:
            return f"{emp_id} is not found"

    def get_employee_names(self):
        "This fuction helps you with getting the employee names"
        emp_id_lst = []
        emp_name_lst = []
        cursor = sql.cursor()
        cursor.execute("SELECT emp_id,emp_name FROM employees;")
        for emps in cursor.fetchall():
            emp_id_lst.append(emps[0])
            emp_name_lst.append(emps[1])
        cursor.close()
        return emp_id_lst,emp_name_lst
        
    # Reminder: Add in time and outime management systme (Multi In & Out)

# Employee().add_employee(emp_id=1,emp_name="Abhinand", emp_phone="7306466576", payment_amnt=5000)

class Sale():
    def add_sale():
        pass
    def modify_sale():
        pass
    def delete_sale():
        pass