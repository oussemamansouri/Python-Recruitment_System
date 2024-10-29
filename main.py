import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from authentication import admin_login, job_seeker_login, register_job_seeker 
from admin import add_job_offer 
from database_manager import load_data, save_data


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

    tk.Button(admin_dashboard, text="Add Job Offer", command=open_add_job_offer).pack(pady=5)
    tk.Button(admin_dashboard, text="View All Job Offers", command=view_all_job_offers).pack(pady=5)
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


def open_add_job_offer():
    add_job_window = tk.Toplevel(root)
    add_job_window.title("Add Job Offer")
    add_job_window.geometry("500x600")

    tk.Label(add_job_window, text="Add New Job Offer", font=("Helvetica", 14)).pack(pady=10)

    # Input fields for job offer details
    tk.Label(add_job_window, text="Job ID:").pack()
    job_id_entry = tk.Entry(add_job_window)
    job_id_entry.pack()

    tk.Label(add_job_window, text="Company Name:").pack()
    company_name_entry = tk.Entry(add_job_window)
    company_name_entry.pack()

    tk.Label(add_job_window, text="Address:").pack()
    address_entry = tk.Entry(add_job_window)
    address_entry.pack()

    tk.Label(add_job_window, text="Phone Number:").pack()
    phone_number_entry = tk.Entry(add_job_window)
    phone_number_entry.pack()

    tk.Label(add_job_window, text="Email:").pack()
    email_entry = tk.Entry(add_job_window)
    email_entry.pack()

    tk.Label(add_job_window, text="Degree Required:").pack()
    degree_required_entry = tk.Entry(add_job_window)
    degree_required_entry.pack()

    tk.Label(add_job_window, text="Qualifications:").pack()
    qualifications_entry = tk.Entry(add_job_window)
    qualifications_entry.pack()

    tk.Label(add_job_window, text="Experience Required:").pack()
    experience_required_entry = tk.Entry(add_job_window)
    experience_required_entry.pack()

    tk.Label(add_job_window, text="Mission Description:").pack()
    mission_description_entry = tk.Entry(add_job_window)
    mission_description_entry.pack()

    # Function to handle adding the job offer
    def add_job():
        job_id = job_id_entry.get()
        company_name = company_name_entry.get()
        address = address_entry.get()
        phone_number = phone_number_entry.get()
        email = email_entry.get()
        degree_required = degree_required_entry.get()
        qualifications = qualifications_entry.get()
        experience_required = experience_required_entry.get()
        mission_description = mission_description_entry.get()

        # Check if all fields are filled
        if all([job_id, company_name, address, phone_number, email, degree_required, qualifications, experience_required, mission_description]):
            # Add job offer and display result
            if add_job_offer(job_id, company_name, address, phone_number, email, degree_required, qualifications, experience_required, mission_description):
                messagebox.showinfo("Success", "Job offer added successfully!")
                add_job_window.destroy()
            else:
                messagebox.showerror("Error", "Job ID already exists!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    # Add button
    tk.Button(add_job_window, text="Add Job Offer", command=add_job).pack(pady=10)



def view_all_job_offers():
    # Create a new window to display job offers
    view_jobs_window = tk.Toplevel(root)
    view_jobs_window.title("View All Job Offers")
    view_jobs_window.geometry("800x400")

    # Load job offers from the file
    job_offers = load_data('data/job_offers.txt')

    # Style configuration for the Treeview
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background="#d3d3d3")
    style.configure("Treeview", rowheight=25)
    style.map("Treeview", background=[("selected", "#7696d8")])

    # Create the Treeview table with columns
    columns = ("Job ID", "Company Name", "Address", "Phone", "Email", "Degree", "Qualifications", "Experience", "Mission")
    tree = ttk.Treeview(view_jobs_window, columns=columns, show="headings", selectmode="browse", style="Treeview")

    # Define column headers
    for col in columns:
        tree.heading(col, text=col, anchor="w")
        tree.column(col, width=100, anchor="w")

    # Add job offers to the table with alternating row colors
    for idx, (job_id, details) in enumerate(job_offers.items()):
        company_info = details["company_info"]
        job_details = details["job_details"]

        # Insert job details into the Treeview with 'even' and 'odd' tags
        tree.insert(
            "",
            "end",
            iid=job_id,
            values=(
                job_id,
                company_info["company_name"],
                company_info["address"],
                company_info["phone_number"],
                company_info["email"],
                job_details["degree_required"],
                job_details["qualifications"],
                job_details["experience_required"],
                job_details["mission_description"]
            ),
            tags=("even" if idx % 2 == 0 else "odd",)
        )

    # Configure tag colors for alternating rows
    tree.tag_configure("even", background="#f0f0f0")
    tree.tag_configure("odd", background="#ffffff")

    # Pack the Treeview into the window
    tree.pack(fill="both", expand=True)

    # Button frame for Update and Delete
    button_frame = tk.Frame(view_jobs_window)
    button_frame.pack(fill="x")

    def update_selected_job():
        selected_job_id = tree.selection()
        if selected_job_id:
            job_id = selected_job_id[0]
            open_update_job_offer_form(job_id)

    def delete_selected_job():
        selected_job_id = tree.selection()
        if selected_job_id:
            job_id = selected_job_id[0]
            
            # Show confirmation dialog
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this job offer?")
            if confirm:
                # Remove from the Treeview
                tree.delete(job_id)

                # Remove from the data structure and save to file
                if job_id in job_offers:
                    del job_offers[job_id]
                    save_data('data/job_offers.txt', job_offers)

                # Show success message
                messagebox.showinfo("Deleted", "Job offer deleted successfully.")

    # Add Update and Delete buttons
    tk.Button(button_frame, text="Update Selected Job Offer", command=update_selected_job).pack(side="left", padx=5, pady=5)
    tk.Button(button_frame, text="Delete Selected Job Offer", command=delete_selected_job).pack(side="left", padx=5, pady=5)

# Function to open a form pre-filled with selected job offer details for updating
def open_update_job_offer_form(job_id):
    job_offers = load_data('data/job_offers.txt')
    job_details = job_offers.get(job_id)

    if not job_details:
        messagebox.showerror("Error", "Job offer not found.")
        return

    # Create a new window for updating
    update_window = tk.Toplevel(root)
    update_window.title("Update Job Offer")
    update_window.geometry("500x600")

    tk.Label(update_window, text="Update Job Offer", font=("Helvetica", 14)).pack(pady=10)

    # Fields for job offer details, pre-filled with current data
    fields = {
        "Company Name": job_details["company_info"]["company_name"],
        "Address": job_details["company_info"]["address"],
        "Phone Number": job_details["company_info"]["phone_number"],
        "Email": job_details["company_info"]["email"],
        "Degree Required": job_details["job_details"]["degree_required"],
        "Qualifications": job_details["job_details"]["qualifications"],
        "Experience Required": job_details["job_details"]["experience_required"],
        "Mission Description": job_details["job_details"]["mission_description"],
    }

    entries = {}
    for label_text, value in fields.items():
        tk.Label(update_window, text=label_text).pack()
        entry = tk.Entry(update_window)
        entry.insert(0, value)
        entry.pack()
        entries[label_text] = entry

    # Function to handle update and save to file
    def save_updated_job():
        updated_details = {
            "company_info": {
                "company_name": entries["Company Name"].get(),
                "address": entries["Address"].get(),
                "phone_number": entries["Phone Number"].get(),
                "email": entries["Email"].get(),
            },
            "job_details": {
                "degree_required": entries["Degree Required"].get(),
                "qualifications": entries["Qualifications"].get(),
                "experience_required": entries["Experience Required"].get(),
                "mission_description": entries["Mission Description"].get(),
            }
        }

        job_offers[job_id] = updated_details
        save_data('data/job_offers.txt', job_offers)
        messagebox.showinfo("Update Successful", "Job offer updated successfully!")
        update_window.destroy()

    # Save button to save the updated job offer
    tk.Button(update_window, text="Save Changes", command=save_updated_job).pack(pady=10)


# Placeholder functions
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
