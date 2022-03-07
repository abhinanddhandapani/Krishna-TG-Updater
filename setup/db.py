import mysql.connector
from private import DB_HOST,DB_PASSWORD,DB_USERNAME

sql = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD
)

db_name = "krishna"

# Sql Commands
# Check Existing DBs
def check_db():
    try:
        cursor = sql.cursor()
        cursor.execute("SHOW DATABASES;")
        lst_dbs = []
        for i in cursor.fetchall():
            lst_dbs.append(i[0])
        cursor.close()
        if db_name in lst_dbs:
            return "Database Found"
        else:
            return "No Database Found"

    except:
        return "Server Unreachable"

# Creating Database
def create_db():
    db = check_db()
    if db == "Database Found":
        return "Database Already Exist"
    elif db == "No Database Found":
        try:
            cursor = sql.cursor()
            cursor.execute("CREATE DATABASE krishna;")
            cursor.commit()
            cursor.close()
            return "Created New Database"
        except:
            return "Creation Failed"
    else:
        return "Server Error"

# Creating Tables
