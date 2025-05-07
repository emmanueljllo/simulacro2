🧾 simulacro1.py
This is a basic student management system written in Python. It allows you to store, search, update, delete, and analyze student academic information through a simple command-line interface.

📋 Features
Add student: Register a new student with validations for unique ID, positive age, and grades between 0.0 and 5.0.

Search by ID: Find a student using their ID number.

Search by name: Perform partial name matching to find students.

Update student: Modify a student's age and/or grade.

Delete student: Remove a student from the system using their ID.

Calculate average: Compute the average grade of all registered students.

List students with low grades: Show students with grades below a specified threshold (default: 3.0).

Interactive menu: A simple text-based interface to choose actions.

🛠️ Requirements
Python 3.x

▶️ How to Use
Save the script as simulacro1.py.

Run it from the terminal or any Python environment:

bash
Copiar
Editar
python simulacro1.py
Follow the on-screen menu to manage students.

💡 Notes
Student data is stored in-memory (not saved to disk).

The script includes basic input validation to avoid user errors.

Data will be lost after the program ends unless persistence is added.

📦 Example Student
python
Copiar
Editar
{
    "id": "5001",
    "name": "luciana florez",
    "age": "19",
    "grades": "3.5"
}
🚧 Possible Future Improvements
Save/load students from a JSON or CSV file.

Add a graphical user interface (GUI) using Tkinter or a web interface using Flask.

Include user authentication to secure access.

