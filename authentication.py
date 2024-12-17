import os
import json
from tkinter import messagebox
from database_manager import load_data, save_data

# File paths for storing credentials
ADMIN_CREDENTIALS_FILE = "data/admin_credentials.txt"
JOB_SEEKERS_FILE = "data/job_seekers.txt"

# Global variable to store the logged-in job seeker's username
logged_in_job_seeker = None  # Initially, no job seeker is logged in


# Administrator authentication
def admin_login(password):
    admin_data = load_data(ADMIN_CREDENTIALS_FILE)
    if admin_data.get("password") == password:
        return True
    else:
        messagebox.showerror("Login Error", "Incorrect Admin Password")
        return False


# Job seeker authentication
def job_seeker_login(username, password):
    global logged_in_job_seeker  # Reference the global variable to store the logged-in user
    job_seekers = load_data(JOB_SEEKERS_FILE)
    if username in job_seekers and job_seekers[username]["password"] == password:
        logged_in_job_seeker = username  # Set the logged-in job seeker's username
        return True
    else:
        messagebox.showerror("Login Error", "Incorrect username or password")
        return False


# Helper function to get the logged-in job seeker's username
def get_logged_in_job_seeker_username():
    return logged_in_job_seeker if logged_in_job_seeker else None


# Register a new job seeker
def register_job_seeker(username, password, identity_card, name, address, phone_number, degree, experience, skills):
    # Load existing job seekers
    job_seekers = load_data(JOB_SEEKERS_FILE)

    # Check if username already exists
    if username in job_seekers:
        messagebox.showerror("Registration Error", "Username already exists")
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

    # Save updated data back to the file
    save_data(JOB_SEEKERS_FILE, job_seekers)
    return True


