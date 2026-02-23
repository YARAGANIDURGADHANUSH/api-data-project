# API Data Retrieval, Processing, and Visualization Project

## 📌 Project Overview

This project demonstrates an end-to-end data engineering workflow using Python.
It covers REST API data retrieval, local database storage using SQLite, CSV data ingestion, data processing, and visualization.

The implementation simulates real-world backend and data processing tasks commonly performed in software development and data engineering roles.

---

## 🎯 Problem Statement Implementation

### 1️⃣ API Data Retrieval and Storage

* Fetches structured JSON data from an external REST API.
* Parses API responses using Python.
* Stores retrieved records into a local SQLite database.
* Displays stored data for verification.

**File:** `api_fetch.py`

**Concepts Used**

* REST API integration (Requests library)
* JSON parsing
* SQLite database connectivity
* Table creation and data insertion

---

### 2️⃣ Data Processing and Visualization

* Processes student score data.
* Calculates average score.
* Generates a bar chart visualization.

**File:** `visualization.py`

**Concepts Used**

* Data processing in Python
* Statistical calculation
* Data visualization using Matplotlib

---

### 3️⃣ CSV Data Import to Database

* Reads structured user data from a CSV file.
* Inserts records into SQLite database tables.
* Verifies successful database insertion.

**File:** `csv_to_db.py`

**Concepts Used**

* CSV file handling
* Database schema creation
* Parameterized SQL queries
* Data persistence

---

## 🧰 Technologies Used

* Python 3
* SQLite3
* Requests
* Matplotlib
* VS Code
* Git & GitHub

---

## 📁 Project Structure

```
api-data-project/
│
├── api_fetch.py        # API data retrieval & storage
├── csv_to_db.py        # CSV to database import
├── visualization.py    # Data visualization
├── users.csv           # Sample dataset
├── database.db         # SQLite database
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/YARAGANIDURGADHANUSH/api-data-project.git
cd api-data-project
```

### 2. Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install requests matplotlib
```

---

## ▶️ How to Run

Run the scripts in the following order:

```
python api_fetch.py
python csv_to_db.py
python visualization.py
```

---

## ✅ Expected Outputs

* API data stored in SQLite database (`posts` table)
* CSV data inserted into database (`users` table)
* Bar chart visualization of student scores
* Database viewable using SQLite Viewer extension

---

## 📚 Learning Outcomes

* REST API handling using Python
* Database operations with SQLite
* CSV data ingestion workflow
* Data visualization techniques
* Version control using GitHub
* Project structuring for real-world applications

---

## 👨‍💻 Author

**Durga Dhanush Yaragani**
Final Year B.Tech Student
Position: AI/ML Trainee
---

## 🔗 Repository Link

https://github.com/YARAGANIDURGADHANUSH/api-data-project
