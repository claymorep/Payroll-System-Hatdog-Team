import tkinter as tk
import database as db

def main2():
    global add_salaryrange
    add_salaryrange = "n/a"

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
        
    global job_id
    job_id = ""
    def custom_show_error(message):
        error_dialog = tk.Toplevel()
        error_dialog.title("Error")
        error_dialog.geometry("300x100")

        error_label = tk.Label(error_dialog, text=message, fg="black", padx=10, pady=10)
        error_label.pack(fill=tk.BOTH, expand=True)

        ok_button = tk.Button(error_dialog, text="OK", command=error_dialog.destroy)
        ok_button.pack()

    def main_interface():
        global em_id, add_jobid, add_jobdpt, add_jobname, add_jobdesc, add_salaryrange
        global job_id, job_dpt, job_name, job_desc, salary_range    
        # create a frame for the top division
        top_frame = tk.Frame(window, bg='#333333', height=50)
        top_frame.pack(fill=tk.X)

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
        text_reports = tk.Label(top_frame, text="Edit Department", font=("Helvetica", 16), bg='#333333', fg='#ffffff')
        text_reports.pack(side=tk.LEFT, padx=10)

    def add_profile():
        global em_id, add_jobid, add_jobdpt, add_jobname, add_jobdesc, add_salaryrange
        global job_id, job_dpt, job_name, job_desc, salary_range 
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

    ## def load_profile():
    def load_department_data():
        global em_id, add_jobid, add_jobdpt, add_jobname, add_jobdesc, add_salaryrange
        global job_id, job_dpt, job_name, job_desc, salary_range    
        
        sql = "SELECT * FROM department where job_id='" +job_id+ "'"
        db.mycursor.execute(sql)
        department_info = db.mycursor.fetchone()
        
        if department_info is not None:
            job_id = department_info[0]  # job id
            job_dpt = department_info[1]  # job department
            job_name = department_info[2]  # job name
            job_desc = department_info[3]  # job desc
            salary_range =  department_info[4]  # salary range

        else:
            # Handle the case where no data is found for the given em_id
            custom_show_error("JOB ID not found with the provided ID.\nPlease Visit Add Department Tab\nAnd Insert a New Data")
            print("No JOB ID found with the provided ID.")

    def input_boxes():
        global em_id, add_jobid, add_jobdpt, add_jobname, add_jobdesc, add_salaryrange
        global job_id, job_dpt, job_name, job_desc, salary_range
        
        global job_dpt  # Add this line to declare job_dpt as a global variable
        
        x_axis = .05
        y_axis = 0

        # Employee ID
        add_em_button = tk.Button(window, text="Edit Department", fg="white", height=2, width=20, command=add_department_boxbg, background="green")
        add_em_button.pack()
        add_em_button.place(x=980, y=180)

        # Job ID
        add_jobid_text = tk.Label(window, text="Edit Job ID: ", font=("Helvetica", 12, "bold"))
        add_jobid_text.place(relx=0.265 + x_axis, rely=0.37 + y_axis, anchor=tk.CENTER)
        add_jobid = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_jobid.place(relx=0.48 + x_axis, rely=0.365 + y_axis, anchor=tk.CENTER)
        add_jobid.insert(0, job_id)

        # Job Department
        add_jobdpt_text = tk.Label(window, text="Job Department: ", font=("Helvetica", 12, "bold"))
        add_jobdpt_text.place(relx=0.250 + x_axis, rely=0.42 + y_axis, anchor=tk.CENTER)
        add_jobdpt = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_jobdpt.place(relx=0.48 + x_axis, rely=0.416 + y_axis, anchor=tk.CENTER)
        add_jobdpt.insert(0, job_dpt)

        # Job Name
        add_jobname_text = tk.Label(window, text="Job Name: ", font=("Helvetica", 12, "bold"))
        add_jobname_text.place(relx=0.267 + x_axis, rely=0.47 + y_axis, anchor=tk.CENTER)
        add_jobname = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_jobname.place(relx=0.48 + x_axis, rely=0.467 + y_axis, anchor=tk.CENTER)
        add_jobname.insert(0, job_name)

        # Job Description
        add_jobdesc_text = tk.Label(window, text="Job Description: ", font=("Helvetica", 12, "bold"))
        add_jobdesc_text.place(relx=0.250 + x_axis, rely=0.52 + y_axis, anchor=tk.CENTER)
        add_jobdesc = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_jobdesc.place(relx=0.48 + x_axis, rely=0.518 + y_axis, anchor=tk.CENTER)
        add_jobdesc.insert(0, job_desc)

        #Salary Range
        add_salaryrange_text = tk.Label(window, text="Salary: ", font=("Helvetica", 12, "bold"))
        add_salaryrange_text.place(relx=0.278 + x_axis, rely=0.57 + y_axis, anchor=tk.CENTER)
        add_salaryrange = tk.Entry(window, highlightbackground="black", highlightthickness=1, width=35, bd=0, background="white", font=("Arial", 16))
        add_salaryrange.place(relx=0.48 + x_axis, rely=0.569 + y_axis, anchor=tk.CENTER)
        add_salaryrange.insert(0, salary_range)


    def view_button():
        global em_id_entry

        x_axis = .05
        y_axis = -0.05
        
        ## Entry for Employee ID
        em_id_label = tk.Label(window, text="Job ID: ", font=("Helvetica", 12, "bold"))
        em_id_label.place(relx=(0.26 + x_axis), rely=0.316 + y_axis, anchor=tk.CENTER)
        
        em_id_entry = tk.Entry(window, highlightbackground="black", highlightthickness=1, width= 35, bd=0, background="white", font=("Arial", 16))
        em_id_entry.place(relx=0.48 + x_axis, rely=0.314 + y_axis, anchor=tk.CENTER)
        
        # Button to trigger loading of profile
        view_button = tk.Button(window, text="View", fg="white", height=1, width=20, command=load_profile_from_entry, background="Black")
        view_button.pack()
        view_button.place(x=980, y=150)

    def load_profile_from_entry():
        global job_id  # Add job_dpt to the list of global variables
        job_id = em_id_entry.get()
        load_department_data()
        input_boxes()


    def add_department_boxbg():
        global em_id, add_jobid, add_jobdpt, add_jobname, add_jobdesc, add_salaryrange
        global job_id, job_dpt, job_name, job_desc, salary_range    
        
        # Retrieve the values from the entry widgets
        add_jobid_val = add_jobid.get()
        add_jobdpt_val = add_jobdpt.get()
        add_jobname_val = add_jobname.get()
        add_jobdesc_val = add_jobdesc.get()
        add_salaryrange_val = add_salaryrange.get()
        
        # Call the database function to edit the employee information
        db.add_department(add_jobid_val, add_jobdpt_val, add_jobname_val, add_jobdesc_val, add_salaryrange_val)

        
        


    def editprofile_box():
        global em_id, add_jobid, add_jobdpt, add_jobname, add_jobdesc, add_salaryrange
        global job_id, job_dpt, job_name, job_desc, salary_range  
        # Report Slip Name Label na Malaki
        big_text = tk.Label(window, text="Edit Department", font=("Helvetica", 36, "bold"), bg="lightgrey")
        big_text.place(relx=0.28, rely=0.12, anchor=tk.CENTER)
        


        # yung mismong payslip na border kineme
        frame_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=1000, height=500, bd=0)
        frame_payslip.pack(padx=45, pady=40, side=tk.LEFT)


    def report_page():
        global window

        windows_x = 1280
        windows_y = 720

        # Create the main window
        window = tk.Tk()
        window.title("Edit Department")
        window.geometry(f"{windows_x}x{windows_y}")
        window.config(bg="lightgrey")

        main_interface()
        
        editprofile_box()
        view_button()
        window.mainloop()

    # Call the function to display the GUI
    report_page()
main2()