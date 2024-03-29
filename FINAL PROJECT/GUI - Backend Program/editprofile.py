import tkinter as tk
import database as db

def main2():
    ## Logout Page
    ## Logout Page
    def logout_page():
        window.destroy()
        import login1 as login2
        login2.main2()
        
        
        
        
    ## Add Department Page
    def add_department_page():
        window.destroy()
        import add_department as ad
        ad.main2()
        
        
    ## Add Profile Page
    def add_profile_page():
        window.destroy()
        import add_profile as ap
        ap.main2()



    ## Delete Profile Page
    def delete_profile_page():
        window.destroy()
        import delete_profile as dp
        dp.main2()
        


    ## Edit Department Page
    def edit_department_page():
        window.destroy()
        import edit_department as ep
        ep.main2()

        

    ## Edit Salary Page
    def edit_salary_page():
        window.destroy()
        import edit_salary as es
        es.main2()

        

    ## Edit Profile Page
    def edit_profile_page():
        window.destroy()
        import editprofile as ep
        ep.main2()

    ## Report Page
    def report_page3():
        window.destroy()
        import reports as rs
        rs.main2()           
        
    def custom_show_error(message):
        error_dialog = tk.Toplevel()
        error_dialog.title("Error")
        error_dialog.geometry("300x100")

        error_label = tk.Label(error_dialog, text=message, fg="black", padx=10, pady=10)
        error_label.pack(fill=tk.BOTH, expand=True)

        ok_button = tk.Button(error_dialog, text="OK", command=error_dialog.destroy)
        ok_button.pack()
        
    global em_id
    em_id = ""

    def main_interface():
        global view_firstname, view_lastname, view_age, view_birthday, view_gender, view_address, view_contactnum, view_email, view_jobstatus
        global job_id, salaryid
        # create a frame for the top division
        top_frame = tk.Frame(window, bg='#333333', height=50)
        top_frame.pack(fill=tk.X)

        # create buttons for the top division
        home_button = tk.Button(top_frame, text="Reports", bg="black", fg="white", command = report_page3)
        home_button.pack(side=tk.RIGHT, padx=10)

        


        # Create a frame for the navigation bar
        nav_frame = tk.Frame(window, bg="#353333")
        nav_frame.pack(side="left", fill="y")

        # Create the navigation buttons
        btn_edit_profile = tk.Button(nav_frame, text="EDIT PROFILE", bg="black", fg="white", command = edit_profile_page)
        btn_add_profile = tk.Button(nav_frame, text="ADD PROFILE", bg="black", fg="white", command = add_profile_page)
        btn_delete_profile = tk.Button(nav_frame, text="DELETE PROFILE", bg="black", fg="white", command = delete_profile_page)
        btn_salary = tk.Button(nav_frame, text="EDIT SALARY", bg="black", fg="white", command = edit_salary_page)
        

        # Lay out the navigation buttons with space between them
        btn_edit_profile.pack(fill="x", padx=10, pady=(10, 0))
        btn_add_profile.pack(fill="x", padx=10, pady=5)
        btn_delete_profile.pack(fill="x", padx=10, pady=5)
        btn_salary.pack(fill="x", padx=10, pady=5)
        btn_logout = tk.Button(nav_frame, text="LOG-OUT", bg="BLACK", fg="white", command = logout_page)
        btn_logout.pack(fill="x", padx=10, pady=(5, 10), side= "bottom")
        btn_editdepartment = tk.Button(nav_frame, text="EDIT DEPARTMENT", bg="BLACK", fg="white", command = edit_department_page)
        btn_editdepartment.pack(fill="x", padx=10, pady=5)
        btn_adddepartment = tk.Button(nav_frame, text="ADD DEPARTMENT", bg="BLACK", fg="white", command = add_department_page)
        btn_adddepartment.pack(fill="x", padx=10, pady=5)
        # Create a label for "Reports" text
        text_reports = tk.Label(top_frame, text="Edit Profile", font=("Helvetica", 16), bg='#333333', fg='#ffffff')
        text_reports.pack(side=tk.LEFT, padx=10)

    def add_profile():
        global view_firstname, view_lastname, view_age, view_birthday, view_gender, view_address, view_contactnum, view_email, view_jobstatus
        global job_id, salaryid
        entry = tk.Entry(window, width=30)
        entry.pack(padx = 0, pady= 10)
        entry.place(x=950, y=98)

        search_button = tk.Button(window, text="Add") #, command=print_user_input)
        search_button.pack()
        search_button.place(x = 900, y = 95)
        ## ito lang gamitin pag mag aadjust ng frames (basic info)
        x_axis = 0
        y_axis = -0.05
        
        ## ito naman gamitin pag adjust din ng frame ng deduction part
        
        # NAME
        big_text = tk.Label(window, text= "ADD PROFILE", font=("Helvetica", 12, "bold"), bg="")
        big_text.place(relx=(0.233 + x_axis), rely=0.316 + y_axis, anchor=tk.LEFT)

    def load_profile():
        global em_id, view_firstname, view_lastname, view_age, view_birthday, view_gender, view_address, view_contactnum, view_email, view_jobstatus
        global view_firstname, view_lastname, view_age, view_birthday, view_gender, view_address, view_contactnum, view_email, view_jobstatus
        global job_id, salaryid
        sql = "SELECT * FROM employee WHERE em_id=" + "'" + em_id + "'"
        db.mycursor.execute(sql)

        employee_data = db.mycursor.fetchone()
        if employee_data is not None:
            em_id = employee_data[0]  # emp id
            view_firstname = employee_data[1]  # first name
            view_lastname = employee_data[2]  # last name
            view_age = employee_data[3]  # age
            view_birthday = str(employee_data[4])  # birthday
            view_gender = employee_data[5]  # gender
            view_address = employee_data[6]  # address
            view_contactnum = employee_data[7]  # contact number
            view_email = employee_data[8]  # email
            view_jobstatus = employee_data[9]  # job status
        else:
            # Handle the case where no data is found for the given em_id
            print("No employee found with the provided ID.")

    def input_boxes():
        x_axis = .05
        y_axis = -0.05
        
        global em_id, add_firstname, add_lastname, add_age, add_birthday, add_gender, add_address, add_contactnum, add_email, add_jobstatus
        global job_id, salaryid
        # Employee ID
        add_em_button = tk.Button(window, text="Edit Profile", fg="white", height=2, width=20, command=addprofile_boxbg, background="green")
        add_em_button.pack()
        add_em_button.place(x=980, y=180)
        
        # First Name
        add_firstname_text = tk.Label(window, text="First Name: ", font=("Helvetica", 12, "bold"))
        add_firstname_text.place(relx=0.265 + x_axis, rely=0.37 + y_axis, anchor=tk.CENTER)
        add_firstname = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_firstname.place(relx=0.48 + x_axis, rely=0.365 + y_axis, anchor=tk.CENTER)
        add_firstname.insert(0, view_firstname)

        # Last Name
        add_lastname_text = tk.Label(window, text="Last Name: ", font=("Helvetica", 12, "bold"))
        add_lastname_text.place(relx=0.265 + x_axis, rely=0.42 + y_axis, anchor=tk.CENTER)
        add_lastname = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_lastname.place(relx=0.48 + x_axis, rely=0.416 + y_axis, anchor=tk.CENTER)
        add_lastname.insert(0, view_lastname)

        # Age
        add_age_text = tk.Label(window, text="Age: ", font=("Helvetica", 12, "bold"))
        add_age_text.place(relx=0.285 + x_axis, rely=0.47 + y_axis, anchor=tk.CENTER)
        add_age = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_age.place(relx=0.48 + x_axis, rely=0.467 + y_axis, anchor=tk.CENTER)
        add_age.insert(0, view_age)

        # Birthday
        add_birthday_text = tk.Label(window, text="Birthday: ", font=("Helvetica", 12, "bold"))
        add_birthday_text.place(relx=0.272 + x_axis, rely=0.52 + y_axis, anchor=tk.CENTER)
        add_birthday = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_birthday.place(relx=0.48 + x_axis, rely=0.518 + y_axis, anchor=tk.CENTER)
        add_birthday.insert(0, view_birthday)

        # Gender
        add_gender_text = tk.Label(window, text="Gender: ", font=("Helvetica", 12, "bold"))
        add_gender_text.place(relx=0.275 + x_axis, rely=0.57 + y_axis, anchor=tk.CENTER)
        add_gender = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_gender.place(relx=0.48 + x_axis, rely=0.569 + y_axis, anchor=tk.CENTER)
        add_gender.insert(0, view_gender)

        # Address
        add_address_text = tk.Label(window, text="Address: ", font=("Helvetica", 12, "bold"))
        add_address_text.place(relx=0.273 + x_axis, rely=0.62+ y_axis, anchor=tk.CENTER)
        add_address = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_address.place(relx=0.48 + x_axis, rely=0.62 + y_axis, anchor=tk.CENTER)
        add_address.insert(0, view_address)

        # Contact Number
        add_contactnum_text = tk.Label(window, text="Contact Number: ", font=("Helvetica", 12, "bold"))
        add_contactnum_text.place(relx=0.249 + x_axis, rely=0.67 + y_axis, anchor=tk.CENTER)
        add_contactnum = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_contactnum.place(relx=0.48 + x_axis, rely=0.671 + y_axis, anchor=tk.CENTER)
        add_contactnum.insert(0, view_contactnum)

        # Email Add
        add_email_text = tk.Label(window, text="Email: ", font=("Helvetica", 12, "bold"))
        add_email_text.place(relx=0.282 + x_axis, rely=0.72 + y_axis, anchor=tk.CENTER)
        add_email = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_email.place(relx=0.48 + x_axis, rely=0.722 + y_axis, anchor=tk.CENTER)
        add_email.insert(0, view_email)

        # Job Status
        add_jobstat_text = tk.Label(window, text="Job Status: ", font=("Helvetica", 12, "bold"))
        add_jobstat_text.place(relx=0.266 + x_axis, rely=0.77 + y_axis, anchor=tk.CENTER)
        add_jobstatus = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_jobstatus.place(relx=0.48 + x_axis, rely=0.773 + y_axis, anchor=tk.CENTER)
        add_jobstatus.insert(0, view_jobstatus)
        
        # Job ID
        job_id_text = tk.Label(window, text="Job ID: ", font=("Helvetica", 12, "bold"))
        job_id_text.place(relx=0.266 + x_axis, rely=0.82 + y_axis, anchor=tk.CENTER)
        job_id = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        job_id.place(relx=0.48 + x_axis, rely=0.823 + y_axis, anchor=tk.CENTER)
        
        # Salary ID
        salaryid_text = tk.Label(window, text="Salary ID: ", font=("Helvetica", 12, "bold"))
        salaryid_text.place(relx=0.266 + x_axis, rely=0.87 + y_axis, anchor=tk.CENTER)
        salaryid = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        salaryid.place(relx=0.48 + x_axis, rely=0.873 + y_axis, anchor=tk.CENTER)

    def view_button():
        global em_id_entry

        x_axis = .05
        y_axis = -0.05
        
        ## Entry for Employee ID
        em_id_label = tk.Label(window, text="Employee ID: ", font=("Helvetica", 12, "bold"))
        em_id_label.place(relx=(0.26 + x_axis), rely=0.316 + y_axis, anchor=tk.CENTER)
        
        em_id_entry = tk.Entry(window, highlightbackground="black", highlightthickness=1, width= 35, bd=0, background="white", font=("Arial", 16))
        em_id_entry.place(relx=0.48 + x_axis, rely=0.314 + y_axis, anchor=tk.CENTER)
        
        # Button to trigger loading of profile
        view_button = tk.Button(window, text="View", fg="white", height=1, width=20, command=load_profile_from_entry, background="Black")
        view_button.pack()
        view_button.place(x=980, y=150)

    def load_profile_from_entry():
        global em_id
        em_id = em_id_entry.get()
        load_profile()
        input_boxes()


    def addprofile_boxbg():
        global em_id, add_firstname, add_lastname, add_age, add_birthday, add_gender, add_address, add_contactnum, add_email, add_jobstatus
        global view_firstname, view_lastname, view_age, view_birthday, view_gender, view_address, view_contactnum, view_email, view_jobstatus
        global job_id, salaryid
        # Retrieve the values from the entry widgets
        add_firstname_val = add_firstname.get()
        add_lastname_val = add_lastname.get()
        add_age_val = add_age.get()
        add_birthdate_val = add_birthday.get()
        add_gender_val = add_gender.get()
        add_address_val = add_address.get()
        add_contactnum_val = add_contactnum.get()
        add_email_val = add_email.get()
        add_jobstatus_val = add_jobstatus.get()
        add_jobid_entry = job_id.get()
        add_salaryid_entry = salaryid.get()
                
        # Call the database function to edit the employee information
        db.employee_edit2(em_id, add_firstname_val, add_lastname_val, add_age_val, add_birthdate_val, add_gender_val, add_address_val, add_contactnum_val, add_email_val, add_jobstatus_val)
        db.edit_payroll2(em_id, add_jobid_entry, add_salaryid_entry)
        db.insert_payroll(em_id, add_jobid_entry, add_salaryid_entry)
        
        custom_show_error("Added!")


    def editprofile_box():
        global view_firstname, view_lastname, view_age, view_birthday, view_gender, view_address, view_contactnum, view_email, view_jobstatus
        # Report Slip Name Label na Malaki
        big_text = tk.Label(window, text="Edit Profile", font=("Helvetica", 36, "bold"), bg="lightgrey")
        big_text.place(relx=0.224, rely=0.12, anchor=tk.CENTER)
        


        # yung mismong payslip na border kineme
        frame_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=1000, height=500, bd=0)
        frame_payslip.pack(padx=45, pady=40, side=tk.LEFT)


    def report_page():
        global window
        global windows_x
        global windows_y
        windows_x = 1280
        windows_y = 720
        
        # Create the main window
        window = tk.Tk()
        window.title("Edit Profile")
        window.geometry(f"{windows_x}x{windows_y}")
        window.config(bg="lightgrey")
        
        
        main_interface()
        
        editprofile_box()
        
        view_button()
        window.mainloop()
        
        

    # Call the function to display the GUI

    report_page()

main2()