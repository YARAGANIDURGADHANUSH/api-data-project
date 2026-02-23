# API Data Retrieval, Processing, and Visualization Project

This repository contains a Python-based data processing project demonstrating REST API integration, SQLite database usage, CSV data ingestion, and data visualization using Matplotlib.

The repository also includes AI/ML trainee assessment work organized into separate folders.

---

## Repository Structure


api-data-project/
│
├── ai-ml-trainee-assessment-1/
│ ├── api_fetch.py
│ ├── complex Python code.py
│ ├── complex database code.py
│ ├── csv_to_db.py
│ ├── users.csv
│ └── visualization.py
│
├── ai-ml-trainee-assessment-2/
│ └── AI_ML_Assessment.pdf
│
├── .gitignore
└── README.md


---

## Project Overview

This project demonstrates basic data engineering and Python automation concepts through practical scripts.

The workflow includes:

- Fetching data from a REST API
- Storing API data in an SQLite database
- Importing CSV data into database tables
- Performing file organization using Python
- Creating simple data visualizations

---

## Assessment 1 – Python Data Processing

Located in:


ai-ml-trainee-assessment-1/


### 1. `api_fetch.py`
- Fetches data from an online API (`jsonplaceholder.typicode.com`)
- Converts JSON response into structured format
- Stores records inside an SQLite database
- Creates table if it does not exist

**Concepts Used**
- HTTP requests
- JSON parsing
- SQLite database operations

---

### 2. `csv_to_db.py`
- Reads user data from `users.csv`
- Creates a database table
- Inserts CSV records into SQLite database

**Concepts Used**
- CSV handling
- Database insertion
- Data persistence

---

### 3. `visualization.py`
- Uses sample student score data
- Calculates average score
- Generates a bar chart using Matplotlib

**Concepts Used**
- Data processing
- Basic analytics
- Visualization

---

### 4. `complex Python code.py`
- Organizes files inside a target folder
- Sorts files based on extensions such as images, documents, videos, and archives

**Concepts Used**
- File handling
- OS operations
- Automation using Python

---

### 5. `complex database code.py`
- Demonstrates database creation and API data storage using SQLite
- Similar workflow combining API fetching and database handling

---

### 6. `users.csv`
Sample dataset containing user names and email addresses used for database insertion.

---

## Assessment 2 – AI/ML Submission

Located in:


ai-ml-trainee-assessment-2/


Contains:

- **AI_ML_Assessment.pdf**  
  Documentation submission including self-rating and AI/ML assessment responses.

---

## Technologies Used

- Python 3
- Requests
- SQLite3
- CSV Module
- Matplotlib

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/YARAGANIDURGADHANUSH/api-data-project.git
cd api-data-project
2. Install Dependencies
pip install requests matplotlib
Running the Scripts

Navigate to the first assessment folder:

cd ai-ml-trainee-assessment-1

Run scripts individually:

python api_fetch.py
python csv_to_db.py
python visualization.py
Learning Outcomes

This project demonstrates understanding of:

REST API integration in Python

SQLite database operations

CSV data ingestion

Python file automation

Basic data visualization

Project organization using GitHub

Author:
Durga Dhanush Yaragani
Post: AI/ML Trainee 
