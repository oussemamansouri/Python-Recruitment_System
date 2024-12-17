# Recruitment Information System

## Project Description

This Python project aims to create a recruitment management system for a company. The system is designed for use by both the administrator and job seekers. The administrator manages job offers while job seekers can search for and apply to jobs.

The program uses the `tkinter` module to create a user-friendly graphical interface. All information related to job seekers' applications and job offers is stored in files.

## Features

### **For the Administrator:**

1. **Administrator Login**:
   - The administrator must log in with a password to access the job offer management options.

2. **Add a New Job Offer**:
   - The administrator can add a new job offer by providing a unique ID, company details, profile description, and job mission description.

3. **Update a Job Offer**:
   - The administrator can search for an existing job offer by its ID, modify the offer, and save the updated information.

4. **Delete a Job Offer**:
   - The administrator can delete a job offer by entering its ID. All information related to the offer will be removed from the file.

5. **View Job Seekers**:
   - The administrator can view a list of all job seekers who have applied for a specific job offer.

### **For the Job Seeker:**

1. **Search for a Job Offer**:
   - The job seeker can search for job offers based on the ID, field (e.g., IT, commerce), or location.

2. **Apply for a Job Offer**:
   - The job seeker can apply for a job by selecting from the available job offers. The program prompts the user to enter personal and professional information, including:
     - **Personal Information**: ID card, name, address, phone number.
     - **Education**: University degree, etc.
     - **Professional Information**: Experience, skills, etc.

3. **Update Job Seeker Information**:
   - The job seeker can update their information by entering their ID card number. The system will verify the ID and load the existing information for modification.

## Project Structure

The system has the following structure:
- **Job Seekers**: Information is stored in files and can be modified.
- **Job Offers**: Admin can add, update, or delete offers.
- **Login/Authentication**: Both job seekers and administrators are required to log in using a password.

## Technologies Used

- **Python**: The core programming language for implementing the application logic.
- **Tkinter**: Used for building the graphical user interface (GUI).
- **File Handling**: All data (job offers, job seekers) are stored in text files for simplicity.

## How to Run the Application

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the source code files.
3. Open a terminal or command prompt, navigate to the project directory, and run the following command:
   ```bash
   python main.py
