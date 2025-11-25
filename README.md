Student Result Management System (Python + Flask)

A lightweight web-based application built using Python and Flask that allows admins/teachers to manage student details, upload marks, and view results. This project is beginner-friendly and ideal for learning Flask, routing, templates, and basic CRUD operations.

📌 Features
👩‍🏫 Admin/Teacher Features

Add new student details

Update or delete student records

Add subject-wise marks

Update student marks

View complete student results

🎓 Student Features

Check results using Register Number / Roll Number

View detailed subject-wise marks

Automatically calculate total & grade

🛠️ Tech Stack
Component	Technology
Backend	Python, Flask
Frontend	HTML, CSS, Bootstrap
Database	SQLite (default)
Server	Flask Development Server
📂 Project Structure
student-result-management/
│
├── app.py                  # Main Flask application
├── static/                 # CSS, images
│   └── styles.css
├── templates/              # HTML templates
│   ├── index.html
│   ├── add_student.html
│   ├── add_marks.html
│   ├── view_result.html
│   └── students_list.html
├── database/
│   └── students.db         # SQLite database
└── README.md

⚙️ How to Run the Project
1️⃣ Install required packages
pip install flask

2️⃣ Run the Flask app
python app.py

3️⃣ Open the app in browser
http://127.0.0.1:5000/

🧮 Functions Implemented
📘 Student Management

Add student

List all students

Edit details

Delete student

📝 Marks Management

Add marks

Edit marks

Auto calculate: Total, Percentage, Grade

📊 Result View

Search results by Roll No./Register No.

Clean UI for easy reading

🌟 Key Learning Outcomes

Basics of Flask routing

Template rendering with Jinja2

Form handling (POST / GET)

Working with SQLite database

CRUD operations

Building a simple, clean UI

📄 Future Enhancements

User authentication (Admin login)

Export results as PDF

Graphical performance reports (charts)

API endpoints for mobile apps
