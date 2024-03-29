import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",   # localhost
    user = "root",        # default user is root
    database = "hatdogdb" # name of database
)
mycursor = mydb.cursor()

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str

def duplicate_checker(em_id):
    em_id = str(em_id)
    mycursor.execute("SELECT em_id FROM employee")
    existing_id = mycursor.fetchall()
    for x in existing_id:
        x = convertTuple(x)
        if x == em_id:
            print("ID already exists!")
            print("Employee edit unsuccessful.")
            return 0
        
def id_exist_checker(em_id):
    em_id = str(em_id)
    mycursor.execute("SELECT em_id FROM employee")
    existing_id = mycursor.fetchall()
    for x in existing_id:
        x = convertTuple(x)
        if x == em_id:
            return -1
    print("ID does not exist.")
    return 0

def admin_login():
    print("==LOGIN SCREEN==")
    while True:
        username=str(input("Username: "))
        password=str(input("Password: "))
        sql = "SELECT password FROM admin_pass WHERE username=" + "'" + username + "'"
        mycursor.execute(sql)
        
        myresult = mycursor.fetchone()
        try:
            if myresult[0] == password:
                print("Welcome! You have successfully logged in! \n")
                break
            else:
                print("Wrong Username or Password!")
        except:
            print("Wrong Username or Password!")
        
def employee_insert():
    print("\n==ENTER NEW EMPLOYEE DATA==")
    em_id = str(input("Enter Employee ID: "))
    if duplicate_checker(em_id) == 0:
        return -1
    add_firstname = str(input("Enter First Name: "))
    add_lastname = str(input("Enter Last Name: "))
    add_age = str(input("Enter Age: "))
    add_birthdate = str(input("Enter Birthday (YYYY/MM/DD): "))
    add_gender = str(input("Enter Gender (Male/Female/Others): "))
    add_address = str(input("Enter Address: "))
    add_contact_num = str(input("Enter Contact Number: "))
    add_email = str(input("Enter Email: "))
    add_status = str(input("Enter Job Status: "))
    
    sql = "INSERT INTO employee (em_id, firstname, lastname, age, birthdate, gender, address, contact_num, email, status) "
    sqlValues = "VALUES ('"+em_id+"','"+add_firstname+"','"+add_lastname+"','"+add_age+"','"+add_birthdate+"','"+add_gender+"','"+add_address+"','"+add_contact_num+"','"+add_email+"','"+add_status+"')"
    mycursor.execute(sql + sqlValues)
    mydb.commit()
    
    print("Employee Successfully Added!")
    
def employee_edit():
    print("\n==EDIT EMPLOYEE DATA==")
    edit_id = str(input("Enter Employee ID to Edit: "))
    if id_exist_checker(edit_id) == 0:
        return -1
    
    sql_show = "SELECT * FROM employee WHERE em_id=" + "'"+edit_id+"'"
    mycursor.execute(sql_show)
    current_em = mycursor.fetchone()
    print("==EMPLOYEE INFORMATION TO EDIT==")
    employee_print(edit_id)
    
    print("\n==EDIT HERE==")
    print("Leave blank to not edit")
    em_id = str(input("Edit Employee ID: "))
    firstname = str(input("Edit First Name: "))
    lastname = str(input("Edit Last Name: "))
    age = str(input("Edit Age: "))
    birthdate = str(input("Edit Birthday (YYYY/MM/DD): "))
    gender = str(input("Edit Gender (Male/Female/Others): "))
    address = str(input("Edit Address: "))
    contact_num = str(input("Edit Contact Number: "))
    email = str(input("Edit Email: "))
    status = str(input("Edit Job Status: "))

    if em_id == "":
        em_id = current_em[0]
    if firstname == "":
        firstname = current_em[1]
    if lastname == "":
        lastname = current_em[2]
    if age == "":
        age = current_em[3]
    if birthdate == "":
        birthdate = str(current_em[4])
    if gender == "":
        gender = current_em[5]
    if address == "":
        address = current_em[6]
    if contact_num == "":
        contact_num = current_em[7]
    if email == "":
        email = current_em[8]
    if status == "":
        status = current_em[9]
    
    confirmation = str(input("Confirm Update? (Y/N): "))
    if confirmation == 'Y':
        if duplicate_checker(em_id) == 0:
            return -1

        update1 = "UPDATE employee SET age=" + "'"+age+"', firstname=" + "'"+firstname+"', lastname=" + "'"+lastname+"', "
        update2 = "birthdate=" + "'"+birthdate+"', gender=" + "'"+gender+"', address=" + "'"+address+"', "
        update3 = "contact_num=" + "'"+contact_num+"', email=" + "'"+email+"', status = " + "'"+status+"', "
        sql_formula = update1 + update2 + update3 + "em_id =" + "'"+em_id+"'" + "WHERE em_id=" + "'"+edit_id+"';"
             
        mycursor.execute(sql_formula)
        mydb.commit()
                
        print("Employee Successfully Edited!")
        print("\n==EDITED INFORMATION==")
        employee_print(em_id)
    else:
        print("Employee edit unsuccessful.")

def employee_delete():
    print("\n==DELETE EMPLOYEE DATA==")
    em_id = str(input("Enter Employee ID to Delete: "))
    if id_exist_checker(em_id) == 0:
        return -1
    sql = "DELETE FROM employee WHERE em_id=" + "'"+em_id+"'"
    mycursor.execute(sql)
    mydb.commit()
    
    print("Employee Successfully Deleted!")

def employee_request_data():
    print("\n==REQUEST EMPLOYEE DATA==")
    em_id = str(input("Enter Employee ID to View: "))
    if id_exist_checker(em_id) == 0:
        return -1
    sql = "SELECT * FROM employee WHERE em_id=" + "'"+em_id+"'"
    mycursor.execute(sql)

    employee_data = mycursor.fetchone()

    print("Employee ID: " + employee_data[0])
    print("First Name: " + employee_data[1])
    print("Last Name: " + employee_data[2])
    print("Age: " + employee_data[3])
    print("Birthday: " + str(employee_data[4]))
    print("Gender: " + employee_data[5])
    print("Address: " + employee_data[6])
    print("Contact Number: " + employee_data[7])
    print("Email: " + employee_data[8])
    print("Job Status: " + employee_data[9])

def employee_print(em_id):
    if id_exist_checker(em_id) == 0:
        return -1
    sql = "SELECT * FROM employee WHERE em_id=" + "'"+em_id+"'"
    mycursor.execute(sql)

    employee_data = mycursor.fetchone()

    print("Employee ID: " + employee_data[0])
    print("First Name: " + employee_data[1])
    print("Last Name: " + employee_data[2])
    print("Age: " + employee_data[3])
    print("Birthday: " + str(employee_data[4]))
    print("Gender: " + employee_data[5])
    print("Address: " + employee_data[6])
    print("Contact Number: " + employee_data[7])
    print("Email: " + employee_data[8])
    print("Job Status: " + employee_data[9])

def employee_print_age(em_id):
    if id_exist_checker(em_id) == 0:
        return -1
    sql = "SELECT * FROM employee WHERE em_id=" + "'"+em_id+"'"
    mycursor.execute(sql)

    employee_data = mycursor.fetchone()

    age = employee_data[9]
    print(age)
    # print("Employee ID: " + employee_data[0])
    # print("First Name: " + employee_data[1])
    # print("Last Name: " + employee_data[2])
    # print("Age: " + employee_data[3])
    # print("Birthday: " + str(employee_data[4]))
    # print("Gender: " + employee_data[5])
    # print("Address: " + employee_data[6])
    # print("Contact Number: " + employee_data[7])
    # print("Email: " + employee_data[8])
    # print("Job Status: " + employee_data[9])


def employee_salaryGet(em_id):
    if id_exist_checker(em_id) == 0:
        return None  # Return None if employee ID doesn't exist
    sql = "SELECT salary_id FROM payroll WHERE em_id=%s"
    mycursor.execute(sql, (em_id,))
    payroll_data = mycursor.fetchone()

    if payroll_data:
        salary_id = payroll_data[0]
        mycursor.execute("SELECT monthly_salary FROM hatdogdb.salary WHERE salary_id=%s", (salary_id,))
        salary = mycursor.fetchone()
        if salary:
            return salary[0]  # Return the annual salary directly
    return None  # Return None if salary information is not found

def employee_id(em_id):
    if id_exist_checker(em_id) == 0:
        return -1
    sql = "SELECT * FROM payroll WHERE em_id=" + "'"+em_id+"'"
    mycursor.execute(sql)

    employeedata = mycursor.fetchone()

    employee_id = employeedata[0]
    return employee_id

def employee_insert2(em_id1, firstname, lastname, age, birthdate, gender, address, contactnum, email, emstatus):
    em_id = em_id1
    add_firstname = firstname
    add_lastname = lastname
    add_age = age
    add_birthdate = birthdate
    add_gender = gender
    add_address = address
    add_contact_num = contactnum
    add_email = email
    add_status = emstatus
    
    # Insert the record into the database
    sql = "INSERT INTO employee (em_id, firstname, lastname, age, birthdate, gender, address, contact_num, email, status) "
    sqlValues = "VALUES ('"+em_id+"','"+add_firstname+"','"+add_lastname+"','"+add_age+"','"+add_birthdate+"','"+add_gender+"','"+add_address+"','"+add_contact_num+"','"+add_email+"','"+add_status+"')"
    mycursor.execute(sql + sqlValues)
    mydb.commit()
    
    print("Employee Successfully Added!")





def employee_edit2(em_id, firstname, lastname, age, birthdate, gender, address, contactnum, email, emstatus):
    sql_show = "SELECT * FROM employee WHERE em_id=" + "'"+em_id+"'"
    mycursor.execute(sql_show)
    current_em = mycursor.fetchone()
    print("==EMPLOYEE INFORMATION TO EDIT==")

    edit2_firstname = str(firstname)
    edit_lastname = str(lastname)
    edit_age = str(age)
    edit_birthdate = str(birthdate)
    edit_gender = str(gender)
    edit_address = str(address)
    edit_contact_num = str(contactnum)
    edit_email = str(email)
    edit_status = str(emstatus)


    if em_id == "":
        em_id = current_em[0]
    if edit2_firstname == "":
        edit2_firstname = current_em[1]
    if edit_lastname == "":
        edit_lastname = current_em[2]
    if edit_age == "":
        edit_age = current_em[3]
    if edit_birthdate == "":
        edit_birthdate = str(current_em[4])
    if edit_gender == "":
        edit_gender = current_em[5]
    if edit_address == "":
        edit_address = current_em[6]
    if edit_contact_num == "":
        edit_contact_num = current_em[7]
    if edit_email == "":
        edit_email = current_em[8]
    if edit_status == "":
        edit_status = current_em[9]
    
    update1 = "UPDATE employee SET age=" + "'"+edit_age+"', firstname=" + "'"+edit2_firstname+"', lastname=" + "'"+edit_lastname+"', "
    update2 = "birthdate=" + "'"+edit_birthdate+"', gender=" + "'"+edit_gender+"', address=" + "'"+edit_address+"', "
    update3 = "contact_num=" + "'"+edit_contact_num+"', email=" + "'"+edit_email+"', status = " + "'"+edit_status+"', "
    sql_formula = update1 + update2 + update3 + "em_id =" + "'"+em_id+"'" + "WHERE em_id=" + "'"+em_id+"';"
    
    employee_print(em_id)        
    mycursor.execute(sql_formula)
    mydb.commit()
    
    print("Employee Successfully Updated!")

      
        
def admin_credentials(username, password):
    sql = "SELECT password FROM admin_pass WHERE username=%s"
    mycursor.execute(sql, (username,))
    myresult = mycursor.fetchone()
    
    if myresult and myresult[0] == password:
        return True
    else:
        return False
    
## edit department to:
def add_department(job_id, job_dpt, job_name, job_desc, salary_range):
    if job_id == job_id:
        sql = "UPDATE department SET job_dept='"+ job_dpt +"', job_name='"+ job_name +"', job_desc='"+ job_desc +"', salary_range='"+ str(salary_range) +"' WHERE job_id='" +job_id+"'"
    else:
        sql = "UPDATE department SET job_id='" +job_id+ "', job_dept='"+ job_dpt +"', job_name='"+ job_name +"', job_desc='"+ job_desc +"', salary_range='"+ str(salary_range) +"' WHERE job_id='" +job_id+"'"
    mycursor.execute(sql)
    mydb.commit()

    print("Department Edited!")

## add department to:
def insert_department(job_id, job_dpt, job_name, job_desc, salary_range):
    sql = "INSERT INTO department (job_id, job_dept, job_name, job_desc, salary_range) "
    sqlValues = "VALUES ('"+job_id+"','"+job_dpt+"','"+job_name+"','"+job_desc+"','"+salary_range+"')"
    mycursor.execute(sql + sqlValues)
    mydb.commit()

    print("New Department Added!")
    
def new_salarydata(salary_id, job_id, monthly, bonus):
    monthly
    annual = monthly*12
    
    sql = "INSERT INTO salary (salary_id, job_id, monthly_salary, annual_salary, bonus) "
    sqlValues = "VALUES ('"+salary_id+"','"+job_id+"',"+monthly+","+annual+","+bonus+")"
    mycursor.execute(sql + sqlValues)
    mydb.commit()

    print("New Salary Data Added")
    
def employee_delete2(em_id):
    sql = "DELETE FROM employee WHERE em_id=" + "'"+em_id+"'"
    mycursor.execute(sql)
    mydb.commit()
        
def update_salarydata(salary_id, job_id, monthly, bonus):
    # Convert float values to strings
    
    # Construct the SQL query with converted values
    if salary_id == salary_id:
        sql = "UPDATE salary SET salary_id='"+ salary_id +"', job_id='"+ job_id +"', monthly_salary="+ monthly +", annual_salary="+ (monthly*12) +", bonus=" + bonus +" WHERE salary_id='" +salary_id+"'"
    else:
        sql = "UPDATE salary SET salary_id='"+ salary_id +"', job_id='"+ job_id +"', monthly_salary="+ monthly +", annual_salary="+ (monthly*12) +", bonus=" + bonus +" WHERE salary_id='" +salary_id+"'"
    mycursor.execute(sql)
    mydb.commit()

    print("Salary Edited!")

def get_department_jobname(em_id):
    sql = "SELECT job_id FROM payroll WHERE em_id='" + em_id + "'"
    mycursor.execute(sql)
    job_id = mycursor.fetchone()

    sql = "SELECT job_name FROM department WHERE job_id='" + job_id[0] + "'"
    mycursor.execute(sql)
    job_name = mycursor.fetchone()

    return job_name[0]

def insert_payroll(em_id, job_id, salary_id):
    sql = "INSERT INTO payroll(em_id, job_id, salary_id, date, report) VALUES ('"+em_id+"','"+job_id+"','"+salary_id+"',now(),'report1')"
    mycursor.execute(sql)
    mydb.commit()

def edit_payroll():
    edit_em_id = str(input("enter em_id to edit = "))
    em_id = str(input("enter em_id = "))
    job_id =str(input("enter job_id = "))
    salary_id =str(input("enter job_id = "))
    sql = "UPDATE payroll SET em_id='"+em_id+"', job_id='"+job_id+"', salary_id='"+salary_id+"', date=now(), report='report' WHERE em_id='"+edit_em_id+"'"
    mycursor.execute(sql)
    mydb.commit()

def edit_payroll2(em_id, job_id, salary_id):
    if em_id == em_id:
        sql = "UPDATE payroll SET em_id='"+em_id+"', job_id='"+job_id+"', salary_id='"+salary_id+"', date=now(), report='report' WHERE em_id='"+em_id+"'"
    else:
        sql = "UPDATE payroll SET em_id='"+em_id+"', job_id='"+job_id+"', salary_id='"+salary_id+"', date=now(), report='report' WHERE em_id='"+em_id+"'"
    mycursor.execute(sql)
    mydb.commit()
# just remove the comment for the command you want to run
#admin_login() #login is just admin-password
#employee_insert()
#employee_edit()
#employee_delete()
#employee_request_data()
#employee_salaryGet("101")
#employee_print_age("101")