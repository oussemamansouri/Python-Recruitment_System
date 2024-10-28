import tkinter as tk
from tkinter import messagebox
from authentication import admin_login, job_seeker_login, register_job_seeker 

# Create the main application window
root = tk.Tk()
root.title("Recruitment System")
root.geometry("400x400")

# Function to handle the admin login
def handle_admin_login():
    password = admin_password_entry.get()
    if admin_login(password):
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        open_admin_dashboard()
    else:
        messagebox.showerror("Login Error", "Incorrect Admin Password")

# Function to handle the job seeker login
def handle_job_seeker_login():
    username = job_seeker_username_entry.get()
    password = job_seeker_password_entry.get()
    if job_seeker_login(username, password):
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        open_job_seeker_dashboard()
    else:
        messagebox.showerror("Login Error", "Incorrect username or password")

# Function to open the registration form for a new job seeker
def open_job_seeker_registration():
    registration_window = tk.Toplevel(root)
    registration_window.title("Job Seeker Registration")
    registration_window.geometry("400x600")

    tk.Label(registration_window, text="Job Seeker Registration", font=("Helvetica", 14)).pack(pady=10)

    # Input fields for job seeker registration
    tk.Label(registration_window, text="Username:").pack()
    username_entry = tk.Entry(registration_window)
    username_entry.pack()

    tk.Label(registration_window, text="Password:").pack()
    password_entry = tk.Entry(registration_window, show="*")
    password_entry.pack()

    tk.Label(registration_window, text="Identity Card:").pack()
    identity_card_entry = tk.Entry(registration_window)
    identity_card_entry.pack()

    tk.Label(registration_window, text="Full Name:").pack()
    fullname_entry = tk.Entry(registration_window)
    fullname_entry.pack()

    tk.Label(registration_window, text="Address:").pack()
    address_entry = tk.Entry(registration_window)
    address_entry.pack()

    tk.Label(registration_window, text="Phone Number:").pack()
    phone_number_entry = tk.Entry(registration_window)
    phone_number_entry.pack()

    tk.Label(registration_window, text="Degree:").pack()
    degree_entry = tk.Entry(registration_window)
    degree_entry.pack()

    tk.Label(registration_window, text="Experience:").pack()
    experience_entry = tk.Entry(registration_window)
    experience_entry.pack()

    tk.Label(registration_window, text="Skills (comma-separated):").pack()
    skills_entry = tk.Entry(registration_window)
    skills_entry.pack()

    # Function to handle job seeker registration
    def register():
        username = username_entry.get()
        password = password_entry.get()
        identity_card = identity_card_entry.get()
        name = fullname_entry.get()
        address = address_entry.get()
        phone_number = phone_number_entry.get()
        degree = degree_entry.get()
        experience = experience_entry.get()
        skills = skills_entry.get().split(",")  # Split skills by comma

        if all([username, password, identity_card, name, address, phone_number, degree, experience]):
            if register_job_seeker(username, password, identity_card, name, address, phone_number, degree, experience, skills):
                messagebox.showinfo("Registration Successful", "Job Seeker registered successfully!")
                registration_window.destroy()
            else:
                messagebox.showerror("Registration Error", "Username already exists!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    # Register button
    tk.Button(registration_window, text="Register", command=register).pack(pady=10)

# Function to open the admin dashboard
def open_admin_dashboard():
    admin_dashboard = tk.Toplevel(root)
    admin_dashboard.title("Admin Dashboard")
    admin_dashboard.geometry("400x400")
    tk.Label(admin_dashboard, text="Admin Dashboard", font=("Helvetica", 16)).pack()

    tk.Button(admin_dashboard, text="Add Job Offer", command=add_job_offer).pack(pady=5)
    tk.Button(admin_dashboard, text="Update Job Offer", command=update_job_offer).pack(pady=5)
    tk.Button(admin_dashboard, text="Delete Job Offer", command=delete_job_offer).pack(pady=5)
    tk.Button(admin_dashboard, text="View Applicants", command=view_applicants).pack(pady=5)

# Function to open the job seeker dashboard
def open_job_seeker_dashboard():
    job_seeker_dashboard = tk.Toplevel(root)
    job_seeker_dashboard.title("Job Seeker Dashboard")
    job_seeker_dashboard.geometry("400x400")
    tk.Label(job_seeker_dashboard, text="Job Seeker Dashboard", font=("Helvetica", 16)).pack()

    tk.Button(job_seeker_dashboard, text="Search Job Offers", command=search_job_offers).pack(pady=5)
    tk.Button(job_seeker_dashboard, text="Apply for Job Offer", command=apply_job_offer).pack(pady=5)
    tk.Button(job_seeker_dashboard, text="Update Profile", command=update_job_seeker_profile).pack(pady=5)

# Placeholder functions
def add_job_offer():
    messagebox.showinfo("Function Placeholder", "Add Job Offer function")

def update_job_offer():
    messagebox.showinfo("Function Placeholder", "Update Job Offer function")

def delete_job_offer():
    messagebox.showinfo("Function Placeholder", "Delete Job Offer function")

def view_applicants():
    messagebox.showinfo("Function Placeholder", "View Applicants function")

def search_job_offers():
    messagebox.showinfo("Function Placeholder", "Search Job Offers function")

def apply_job_offer():
    messagebox.showinfo("Function Placeholder", "Apply for Job Offer function")

def update_job_seeker_profile():
    messagebox.showinfo("Function Placeholder", "Update Profile function")

# Admin login frame
admin_frame = tk.LabelFrame(root, text="Admin Login")
admin_frame.pack(fill="both", expand="yes", padx=20, pady=10)

tk.Label(admin_frame, text="Password:").grid(row=0, column=0, padx=5, pady=5)
admin_password_entry = tk.Entry(admin_frame, show="*")
admin_password_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Button(admin_frame, text="Login as Admin", command=handle_admin_login).grid(row=1, columnspan=2, pady=10)

# Job Seeker login frame
job_seeker_frame = tk.LabelFrame(root, text="Job Seeker Login")
job_seeker_frame.pack(fill="both", expand="yes", padx=20, pady=10)

tk.Label(job_seeker_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
job_seeker_username_entry = tk.Entry(job_seeker_frame)
job_seeker_username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(job_seeker_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
job_seeker_password_entry = tk.Entry(job_seeker_frame, show="*")
job_seeker_password_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(job_seeker_frame, text="Login as Job Seeker", command=handle_job_seeker_login).grid(row=2, columnspan=2, pady=10)

# Registration button for new job seekers
tk.Button(root, text="Register as Job Seeker", command=open_job_seeker_registration).pack(pady=10)

root.mainloop()
