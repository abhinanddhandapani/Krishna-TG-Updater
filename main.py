# Sales,Sales Items,Sales Return,Sales Return Items,Employee Attendance - (Web Interface,API),Draw Balance (Web,API).
# Use sqlite
from flask import Flask, render_template, request, url_for, redirect
from db.core import Employee

app = Flask(__name__)

shop_list = ["Shop 1","Shop 2"] # Add Shops Here

# Add Shop Details Here - This functionality will be replaced in futher update.
details_shop_1 = ["Sales : 5000","Sales Return : 100","Active Employees : 5001,5002","Draw Balance : "]
details_shop_2 = ["Sales : 50000","Sales Return : 100","Active Employees : 5001,5002","Draw Balance : "]

# Add the details to the list
shop_details = [details_shop_1,details_shop_2]

# Employee List
Employee().get_employee_names()
emp_lst = ["Reshma","Shiji","Aswathy"]

# This code deals with the adding the shop and list together as a dictionary, for html parsing
details = {}
i = 0
for shop in shop_list:
    details[shop] = shop_details[i]
    i += 1


# Home Page
@app.route("/",methods=["GET","POST"])
def home():
    return render_template("home.html")

@app.route("/owner",methods=["GET","POST"])
def index():
    if request.method == 'GET': 
        return render_template("index.html",title="HomePage",shops = shop_list,details=details) # Here list of shops is updated , details dictionary is passed.
    elif request.method == 'POST':
        return "Working"

# Employee Page
@app.route("/employee",methods=["GET","POST"])
def employee():
    if request.method == 'GET':
        return render_template("employee.html",employee=emp_lst)
    else:
        return "200 OK"

# List API
@app.route("/api")
def api():
    return "API Active"

# Creator Page :)
@app.route("/abhinand",methods=["GET","POST"])
@app.route("/creator",methods=["GET","POST"])
@app.route("/master",methods=["GET","POST"])
def master():
    return redirect("https://abhinand.xyz")

if __name__ == '__main__':
    app.run(debug="True",host="0.0.0.0")
