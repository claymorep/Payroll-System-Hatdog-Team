import tkinter as tk
from tkinter import messagebox
import database as db

error = 0
def main2():
    global bg_image
    bg_image = None

    # function na nag chcheck kung ano yung gitna ng screen mo ngayon 
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_coordinate = (screen_width - width) // 2
        y_coordinate = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")



    def switch_main2_page():
        import reports
        root.destroy()
        reports.main2()
    
    def employeeview_page():
        import employee_view
        root.destroy()
        employee_view.main2()

    def validate_login():
        global error
        username = username_entry.get()
        password = password_entry.get()
        
        # Temporary na login credentials (icoconnect pa to using mySQL)
        if db.admin_credentials(username, password):
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            switch_main2_page()
            
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            error = error + 1
        
        if error == 3:
            messagebox.showerror("Login Failed", "Exceeded number of Logins")
            root.destroy()




    # Size of the window



    def report_page():
        global root
        global username_entry, password_entry
        windows_x = 1280
        windows_y = 720
        root = tk.Tk()
        root.title("Employee Payroll System - Login")
        root.geometry(f"{windows_x}x{windows_y}")

        # Opening window in middle screen
        center_window(root, windows_x, windows_y)








        # Location ng background mo lagay full path
        bg_image = tk.PhotoImage(file=r"background3.png")

        # Create a Canvas covering the entire window
        canvas = tk.Canvas(root, width=windows_x, height=windows_y)
        canvas.place(x=0, y=0)


        # Parang transparency
        #canvas.create_rectangle(0, 0, windows_x, windows_y, fill="white", outline="")
        #canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

        # Label ng bacground
        background_label = tk.Label(root, image=bg_image)
        background_label.place(relwidth=1, relheight=1)





        # Login text na malaki (adjust yung rely para sa location ng height)
        big_text = tk.Label(root, text="Login", font=("Helvetica", 36))
        big_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        big_text = tk.Label(root, text="Employee Payroll System", font=("Helvetica", 16))
        big_text.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        
        admin_view = tk.Label(root, text="Admin Credentials", font=("Helvetica", 9))
        admin_view.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        # Username - yung text at yung textbox
        username_label = tk.Label(root, text="Username:", font=("Helvetica", 14))
        username_label.place(relx=0.47, rely=0.45, anchor=tk.E)
        username_entry = tk.Entry(root, font=("Helvetica", 14))
        username_entry.place(relx=0.5, rely=0.45, anchor=tk.W)

        # Password - yung text at yung textbox
        password_label = tk.Label(root, text="Password:", font=("Helvetica", 14))
        password_label.place(relx=0.47, rely=0.5, anchor=tk.E)
        password_entry = tk.Entry(root, show="*", font=("Helvetica", 14))
        password_entry.place(relx=0.5, rely=0.5, anchor=tk.W)


        # Login Button
        login_button = tk.Button(root, text="Login", font=("Helvetica", 12), command=validate_login)
        login_button.place(relx=0.47, rely=0.6, anchor=tk.CENTER)
        
        employee_view = tk.Button(root, text="Employee View", font=("Helvetica", 12), command=employeeview_page)
        employee_view.place(relx=0.56, rely=0.6, anchor=tk.CENTER)

        root.mainloop()

    report_page()
main2()