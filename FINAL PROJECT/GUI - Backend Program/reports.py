import tkinter as tk
import database as db







def main2():
    global salary_gross
    user_id = None  # Declare entry as a global variable
    entry = None  # Declare entry as a global variable

    user_id = db.employee_id(entry)

    salary_gross = db.employee_salaryGet(user_id)



    ## Logout Page
    def logout_page():
        window.destroy()
        window.quit()
        import login1 as login2
        login2.main2()
        
    ## Report Page
    def report_page3():
        window.destroy()
        import reports as rs
        rs.main2()        
        
        
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

        




    def sss_salarygross(net_salary):
        sss_deductions = 0.0
        
        if net_salary < 4250.0:
            sss_deductions = 390.0
        elif 4250 <= net_salary <= 4749.99:
            sss_deductions = 437.5
        elif 4750 <= net_salary <= 5249.99:
            sss_deductions = 485.0
        elif 5250 <= net_salary <= 5749.99:
            sss_deductions = 532.5
        elif 5750 <= net_salary <= 6249.99:
            sss_deductions = 580.0
        elif 6250 <= net_salary <= 6749.99:
            sss_deductions = 627.5
        elif 6750 <= net_salary <= 7249.99:
            sss_deductions = 675.0
        elif 7250 <= net_salary <= 7749.99:
            sss_deductions = 722.5
        elif 7750 <= net_salary <= 8249.99:
            sss_deductions = 770.0
        elif 8250 <= net_salary <= 8749.99:
            sss_deductions = 817.5
        elif 8750 <= net_salary <= 9249.99:
            sss_deductions = 865.0
        elif 9250 <= net_salary <= 9749.99:
            sss_deductions = 912.5
        elif 9750 <= net_salary <= 10249.99:
            sss_deductions = 960.0
        elif 10250 <= net_salary <= 10749.99:
            sss_deductions = 1007.5
        elif 10750 <= net_salary <= 11249.99:
            sss_deductions = 1055.0
        elif 11250 <= net_salary <= 11749.99:
            sss_deductions = 1102.5
        elif 11750 <= net_salary <= 12249.99:
            sss_deductions = 1150.0
        elif 12250 <= net_salary <= 12749.99:
            sss_deductions = 1197.5
        elif 12750 <= net_salary <= 13249.99:
            sss_deductions = 1245.0
        elif 13250 <= net_salary <= 13749.99:
            sss_deductions = 1292.5
        elif 13750 <= net_salary <= 14249.99:
            sss_deductions = 1340.0
        elif 14250 <= net_salary <= 14749.99:
            sss_deductions = 1387.5
        elif 14750 <= net_salary <= 15249.99:
            sss_deductions = 1455.0
        elif 15250 <= net_salary <= 15749.99:
            sss_deductions = 1502.5
        elif 15750 <= net_salary <= 16249.99:
            sss_deductions = 1550.0
        elif 16250 <= net_salary <= 16749.99:
            sss_deductions = 1597.5
        elif 16750 <= net_salary <= 17249.99:
            sss_deductions = 1645.0
        elif 17250 <= net_salary <= 17749.99:
            sss_deductions = 1692.5
        elif 17750 <= net_salary <= 18249.99:
            sss_deductions = 1740.0
        elif 18250 <= net_salary <= 18749.99:
            sss_deductions = 1787.5
        elif 18750 <= net_salary <= 19249.99:
            sss_deductions = 1835.0
        elif 19250 <= net_salary <= 19749.99:
            sss_deductions = 1882.5
        elif 19750 <= net_salary <= 20249.99:
            sss_deductions = 1930.0
        elif 20250 <= net_salary <= 20749.99:
            sss_deductions = 1977.5
        elif 20750 <= net_salary <= 21249.99:
            sss_deductions = 2025.0
        elif 21250 <= net_salary <= 21749.99:
            sss_deductions = 2072.5
        elif 21750 <= net_salary <= 22249.99:
            sss_deductions = 2120.0
        elif 22250 <= net_salary <= 22749.99:
            sss_deductions = 2167.5
        elif 22750 <= net_salary <= 23249.99:
            sss_deductions = 2215.0
        elif 23250 <= net_salary <= 23749.99:
            sss_deductions = 2262.5
        elif 23750 <= net_salary <= 24249.99:
            sss_deductions = 2310.0
        elif 24250 <= net_salary <= 24749.99:
            sss_deductions = 2357.5
        elif 24750 <= net_salary <= 25249.99:
            sss_deductions = 2405.0
        elif 25250 <= net_salary <= 25749.99:
            sss_deductions = 2452.5
        elif 25750 <= net_salary <= 26249.99:
            sss_deductions = 2500.0
        elif 26250 <= net_salary <= 26749.99:
            sss_deductions = 2547.5
        elif 26750 <= net_salary <= 27249.99:
            sss_deductions = 2595.0
        elif 27250 <= net_salary <= 27749.99:
            sss_deductions = 2642.5
        elif 27750 <= net_salary <= 28249.99:
            sss_deductions = 2690.0
        elif 28250 <= net_salary <= 28749.99:
            sss_deductions = 2737.5
        elif 28750 <= net_salary <= 29249.99:
            sss_deductions = 2785.0
        elif 29250 <= net_salary <= 29749.99:
            sss_deductions = 2832.5
        elif 29750 <= net_salary:
            sss_deductions = 2880.0

        return sss_deductions

    def ph_salarygross(net_salary):
        max_philhealth_deduction = 550.0
        philhealth_rate = 0.0275  # PhilHealth premium contribution rate

        if net_salary < 10000:
            deduction = net_salary * philhealth_rate
        elif 10000.01 <= net_salary <= 99999.99:
            deduction = net_salary * philhealth_rate
        elif net_salary > 100000:
            deduction = max_philhealth_deduction
        else:
            deduction = net_salary * philhealth_rate

        return deduction

    def pagibig_salarygross(gross_salary):
        max_pagibig_deduction = 100.0
        pagibig_rate = 0.02  # Pag-IBIG contribution rate

        if gross_salary >= 5000:
            deduction = min(gross_salary * pagibig_rate, max_pagibig_deduction)
        else:
            deduction = 0.0  # No Pag-IBIG deduction for those earning less than PHP 5,000

        return deduction

    def withholdingtax_salarygross(income):
        if income <= 20833:
            return 0.00
        elif 20833 < income <= 33332:
            return 0.00 + 0.15 * (income - 20833)
        elif 33333 < income <= 66666:
            return 1875.00 + 0.20 * (income - 33333)
        elif 66667 < income <= 166666:
            return 8541.80 + 0.25 * (income - 66667)
        elif 166667 < income <= 666666:
            return 33541.80 + 0.30 * (income - 166667)
        else:
            return 183541.80 + 0.35 * (income - 666667)

    ## Code for the Main Interface
    def main_interface():
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
        text_reports = tk.Label(top_frame, text="Report Slip", font=("Helvetica", 16), bg='#333333', fg='#ffffff')
        text_reports.pack(side=tk.LEFT, padx=10)
        

    ## Code of the text - inside payslip box
    def user_outputs():
        
        ## ito lang gamitin pag mag aadjust ng frames (basic info)
        x_axis = 0.02
        y_axis = -0.05
        
        ## ito naman gamitin pag adjust din ng frame ng deduction part
        
        # NAME
        big_text = tk.Label(window, text="Name: ", font=("Helvetica", 12, "bold"), bg="lightgray")
        big_text.place(relx=(0.233 + x_axis), rely=0.316 + y_axis, anchor=tk.CENTER)
        
        # Employee Position
        big_text = tk.Label(window, text="Employee Position: ", font=("Helvetica", 12, "bold"), bg="lightgray")
        big_text.place(relx=0.1967 + x_axis, rely=0.37 + y_axis, anchor=tk.CENTER)
        
        # Employee Status
        big_text = tk.Label(window, text="Employee Status: ", font=("Helvetica", 12, "bold"), bg="lightgray")
        big_text.place(relx=0.202 + x_axis, rely=0.42 + y_axis, anchor=tk.CENTER)
        
        # Gross Salary
        big_text = tk.Label(window, text="Gross Salary: ", font=("Helvetica", 12, "bold"), bg="lightgray")
        big_text.place(relx=0.213 + x_axis, rely=0.47 + y_axis, anchor=tk.CENTER)
        
        # Net Salary
        big_text = tk.Label(window, text="Net Salary: ", font=("Helvetica", 12, "bold"), bg="lightgray")
        big_text.place(relx=0.22 + x_axis, rely=0.52 + y_axis, anchor=tk.CENTER)
        
        # Deductions (under netsalary)
        big_text = tk.Label(window, text="Deductions ", font=("Helvetica", 16, "bold", "underline"), bg="lightgray")
        big_text.place(relx=0.25, rely=0.56, anchor=tk.CENTER)
        
        # SSS (under Deductions)
        big_text = tk.Label(window, text="SSS: ", font=("Helvetica", 12, "bold"), bg="lightgray")
        big_text.place(relx=0.2658, rely=0.62, anchor=tk.CENTER)
        
        # Philhealth (under Deductions)
        big_text = tk.Label(window, text="Philhealth: ", font=("Helvetica", 12, "bold"), bg="lightgray")
        big_text.place(relx=0.252, rely=0.67, anchor=tk.CENTER)
        
        # Pagibig (under Deductions)
        big_text = tk.Label(window, text="Pagibig: ", font=("Helvetica", 12, "bold"), bg="lightgray")
        big_text.place(relx=0.257, rely=0.72, anchor=tk.CENTER)
        
        # Withholding Tax (under Deductions)
        big_text = tk.Label(window, text="Withholding Tax: ", font=("Helvetica", 12, "bold"), bg="lightgray")
        big_text.place(relx=0.235, rely=0.77, anchor=tk.CENTER)

    ## Code for the box - inside payslip box
    def salary_boxbg():
        
        ## ito lang gamitin pag mag aadjust ng frames (basic info)
        x_axis = 0
        y_axis = -0.05
        
        # NAME
        name_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
        name_payslip.place(relx=0.48 + x_axis, rely=0.314 + y_axis, anchor=tk.CENTER)
        
        # Employee Position
        EP_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
        EP_payslip.place(relx=0.48 + x_axis, rely=0.365 + y_axis, anchor=tk.CENTER)

        # Employee Status
        ES_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
        ES_payslip.place(relx=0.48 + x_axis, rely=0.416 + y_axis, anchor=tk.CENTER)
        
        # Gross Salary
        GS_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
        GS_payslip.place(relx=0.48 + x_axis, rely=0.467 + y_axis, anchor=tk.CENTER)
        
        # Net Salary
        NS_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
        NS_payslip.place(relx=0.48 + x_axis, rely=0.518 + y_axis, anchor=tk.CENTER)
        
        # SSS Deduction
        SssD_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
        SssD_payslip.place(relx=0.51, rely=0.616, anchor=tk.CENTER)
        
        # PHIL Deduction
        PhilD_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
        PhilD_payslip.place(relx=0.51, rely=0.666, anchor=tk.CENTER)

        # Pagibig Deduction
        PgID_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
        PgID_payslip.place(relx=0.51, rely=0.716, anchor=tk.CENTER)
        
        # Witholding Tax Deduction
        WhTaxD_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
        WhTaxD_payslip.place(relx=0.51, rely=0.766, anchor=tk.CENTER)

    ## Code for the payslip box
    def payslip_box():
        # Report Slip Name Label na Malaki
        big_text = tk.Label(window, text="Report Slip", font=("Helvetica", 36, "bold"), bg="lightgrey")
        big_text.place(relx=0.224, rely=0.12, anchor=tk.CENTER)
        


        # yung mismong payslip na border kineme
        frame_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=1000, height=500, bd=0)
        frame_payslip.pack(padx=45, pady=40, side=tk.LEFT)


    def search_bar():
        x_axis = 0
        y_axis = -0.05
        
        ## search bar:
        global entry
        global user_id
        entry = tk.Entry(window, width=30)
        entry.pack(padx = 0, pady= 10)
        entry.place(x=950, y=98)

        def print_user_input():
            global user_id  # Declare user_id as a global variable
            user_id = entry.get()
            if db.id_exist_checker(user_id) == 0:
                return -1
            sql = "SELECT * FROM employee WHERE em_id=" + "'" + user_id + "'"
            db.mycursor.execute(sql)
            employee_data = db.mycursor.fetchone()
            salary = db.employee_salaryGet(employee_data[0])
            
            sql = "SELECT job_id FROM payroll WHERE em_id='" + user_id + "'"
            db.mycursor.execute(sql)
            job_id = db.mycursor.fetchone()

            sql = "SELECT job_name FROM department WHERE job_id='" + job_id[0] + "'"
            db.mycursor.execute(sql)
            job_name = db.mycursor.fetchone()
            job_name = job_name[0]

            sql = "SELECT salary_id FROM payroll WHERE em_id='" + user_id + "'"
            db.mycursor.execute(sql)
            salary_id = db.mycursor.fetchone()

            sql = "SELECT monthly_salary FROM salary WHERE salary_id='" + salary_id[0] + "'"
            db.mycursor.execute(sql)
            monthly_salary = db.mycursor.fetchone()
            monthly_salary = monthly_salary[0]
            
            
    

            ## NAME SLOT
            employee_name_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
            employee_name_payslip.place(relx=0.48 + x_axis, rely=0.314 + y_axis, anchor=tk.CENTER)

            employee_id = tk.Label(window, text=employee_data[1] + " " + employee_data[2] , font=("Helvetica", 12, "bold"), bg="white")
            employee_id.place(relx=0.288 + x_axis, rely=0.3148 + y_axis, anchor=tk.W)


            
            ## EMPLOYEE POSITION
            employee_pos_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
            employee_pos_payslip.place(relx=0.48 + x_axis, rely=0.365 + y_axis, anchor=tk.CENTER)

            employee_id = tk.Label(window, text=job_name, font=("Helvetica", 12, "bold"), bg="white")
            employee_id.place(relx=0.288 + x_axis, rely=0.367 + y_axis, anchor=tk.W)
            
            
            
            ## EMPLOYEE STATUS
            employee_status_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
            employee_status_payslip.place(relx=0.48 + x_axis, rely=0.416 + y_axis, anchor=tk.CENTER)

            employeestatus_id = tk.Label(window, text=employee_data[9], font=("Helvetica", 12, "bold"), bg="white")
            employeestatus_id.place(relx=0.288 + x_axis, rely=0.4187 + y_axis, anchor=tk.W)
            
            
            
            ## GROSS SALARY
            employee_gs_payslip = tk.Frame(window, highlightbackground="BLACK", highlightthickness=1, width=500, height=29, bd=0, background="white")
            employeegs_id = tk.Label(window, text=monthly_salary, font=("Helvetica", 12, "bold"), bg="white")
            employeegs_id.place(relx=0.288 + x_axis, rely=0.468 + y_axis, anchor=tk.W)

            ## NET SALARY
            net_salary_payslip = tk.Label(window, text=(db.employee_salaryGet(employee_data[0]) - (sss_salarygross(salary) + ph_salarygross(salary) + pagibig_salarygross(salary) + withholdingtax_salarygross(salary))), font=("Helvetica", 12, "bold"), bg="white")
            net_salary_payslip.place(relx=0.288 + x_axis, rely=0.519 + y_axis, anchor=tk.W)

            ## SSS SALARY
            employeesss_id = tk.Label(window, text=sss_salarygross(salary), font=("Helvetica", 12, "bold"), bg= "white")
            employeesss_id.place(relx=0.32 + x_axis, rely=0.668 + y_axis, anchor=tk.W)
            
            ## PHILHEALTH SALARY
            employeeph_id = tk.Label(window, text=ph_salarygross(salary), font=("Helvetica", 12, "bold"), bg= "white")
            employeeph_id.place(relx=0.32 + x_axis, rely=0.7185 + y_axis, anchor=tk.W)

            ## PAGIBIG SALARY
            employeepg_id = tk.Label(window, text=pagibig_salarygross(salary), font=("Helvetica", 12, "bold"), bg= "white")
            employeepg_id.place(relx=0.32 + x_axis, rely=0.7685 + y_axis, anchor=tk.W)

            ## WITHHOLDING TAX
            employeepg_wdt = tk.Label(window, text=withholdingtax_salarygross(salary), font=("Helvetica", 12, "bold"), bg= "white")
            employeepg_wdt.place(relx=0.32 + x_axis, rely=0.8185 + y_axis, anchor=tk.W)
            user_id = entry.get()
            
        ## yung button pang search
        search_button = tk.Button(window, text="Search", command=print_user_input)
        search_button.pack()
        search_button.place(x = 900, y = 95)




    def report_page():
        global window

        windows_x = 1280
        windows_y = 720

        # Create the main window
        window = tk.Tk()
        window.title("Employee Pay Slip Report")
        window.geometry(f"{windows_x}x{windows_y}")
        window.config(bg="lightgrey")
        

        
        main_interface()
        
        search_bar()
        payslip_box()
        user_outputs()
        salary_boxbg()
        window.mainloop()


        # Start the main loop
        window.mainloop()
    report_page()
main2()