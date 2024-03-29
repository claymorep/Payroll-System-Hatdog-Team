import tkinter as tk
from tkinter import messagebox
import database as db
import editprofile as ep
import edit_salary as es
import edit_department as ed
import delete_profile as dp
import add_profile as ap
import add_department as ad
import reports as reports1
import login1 as logout

## Logout Page
def logout_page():
    import login1
    login1()
    
    
    
    
## Add Department Page
def add_department_page():
    import add_department
    add_department()
    
    
## Add Profile Page
def add_profile_page():
    import add_profile
    add_profile()



## Delete Profile Page
def delete_profile_page():
    import delete_profile
    delete_profile()
    


## Edit Department Page
def edit_department_page():
    import edit_department
    edit_department()

    

## Edit Salary Page
def edit_salary_page():
    import edit_salary
    edit_salary()

    

## Edit Profile Page
def edit_profile_page():
    import editprofile
    editprofile()