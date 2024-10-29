import json
import os
from database_manager import load_data, save_data

def add_job_offer(job_id, company_name, address, phone_number, email, degree_required, qualifications, experience_required, mission_description):
    job_offers_file = 'data/job_offers.txt'

    # Check if the job offers file exists and is non-empty
    if os.path.exists(job_offers_file) and os.path.getsize(job_offers_file) > 0:
        with open(job_offers_file, 'r') as f:
            job_offers = json.load(f)  # Load existing data
    else:
        job_offers = {}  # Initialize as an empty dictionary if file doesn't exist or is empty

    # Ensure the job ID is unique
    if job_id in job_offers:
        return False  # Job ID already exists

    # Add new job offer with all required information
    job_offers[job_id] = {
        "company_info": {
            "company_name": company_name,
            "address": address,
            "phone_number": phone_number,
            "email": email
        },
        "job_details": {
            "degree_required": degree_required,
            "qualifications": qualifications,
            "experience_required": experience_required,
            "mission_description": mission_description
        }
    }

    # Write updated data back to the file
    save_data('data/job_offers.txt', job_offers)

    return True


