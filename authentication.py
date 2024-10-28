import json
import os
from tkinter import messagebox

# File paths for storing credentials
ADMIN_CREDENTIALS_FILE = "data/admin_credentials.txt"
JOB_SEEKERS_FILE = "data/job_seekers.txt"

# Load data from a file
def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save data to a file
def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file)

# Administrator authentication
def admin_login(password):
    admin_data = load_data(ADMIN_CREDENTIALS_FILE)
    if admin_data.get("password") == password:
        return True
    else:
        messagebox.showerror("Login Error", "Incorrect Admin Password")
        return False

# Register a new administrator (for setup or admin reset purposes)
def register_admin(password):
    admin_data = {"password": password}
    save_data(ADMIN_CREDENTIALS_FILE, admin_data)
    messagebox.showinfo("Admin Registration", "Admin registered successfully")

# Job seeker authentication
def job_seeker_login(username, password):
    job_seekers = load_data(JOB_SEEKERS_FILE)
    if username in job_seekers and job_seekers[username]["password"] == password:
        return True
    else:
        messagebox.showerror("Login Error", "Incorrect username or password")
        return False

# Register a new job seeker
def register_job_seeker(username, password, identity_card, name, address, phone_number, degree, experience, skills):
    job_seekers_file = 'data/job_seekers.txt'

    # Check if the job seekers file exists, if not, create an empty dictionary
    if os.path.exists(job_seekers_file):
        with open(job_seekers_file, 'r') as f:
            job_seekers = json.load(f)
    else:
        job_seekers = {}

    # Check if username already exists
    if username in job_seekers:
        return False  # Username already exists

    # Add new job seeker with all required information
    job_seekers[username] = {
        "password": password,
        "personal_info": {
            "identity_card": identity_card,
            "name": name,
            "address": address,
            "phone_number": phone_number,
            "degree": degree,
            "experience": experience,
            "skills": skills
        }
    }

    # Write updated data back to the file
    with open(job_seekers_file, 'w') as f:
        json.dump(job_seekers, f, indent=4)

    return True
