# 📝 CLI Task Manager

A simple command-line to-do application built with Python.  
Track tasks, set due dates and priorities, and save your progress — all from the terminal!

---

## 🚀 Features

- ✅ Add new tasks with title, due date, and priority
- 📋 View all tasks or only completed ones
- ☑️ Mark tasks as completed
- ❌ Delete tasks by ID
- 💾 Saves all tasks to a JSON file for persistence

---

## 🧠 What I Learned Through this Project

- `argparse` for command-line parsing
- JSON file I/O
- Modular Python code
- `datetime` for date handling
- Basic object filtering and formatting

---

## 🛠️ How to Use

### 📦 Requirements
- Python 3.7+

### 📁 File Structure
task_manager/
├── main.py # Entry point - CLI command parsing
├── task_ops.py # Functions to add, list, complete, delete tasks
├── storage.py # Load and save tasks to JSON
├── utils.py # Helper functions: date validation, ID generation
├── tasks.json # The task data file (auto-created)

## 📌 Commands

### ➕ Add a Task
python main.py add "Update Readme" --due 2025-07-03 --priority high

### 📃 List Tasks
python main.py list                # List all tasks
python main.py list --completed   # List only completed tasks

### ✅ Mark Task as Done
python main.py done 2

### 🗑️ Delete a Task
python main.py delete 2

### 🗂 Example Task Format (in tasks.json)
[
    {
        "id": 1,
        "title": "Update Readme",
        "completed": false,
        "created_at": "2025-07-02",
        "due_date": "2025-07-03",
        "priority": "high"
    }
]

---

### ✨ Future Enhancements (Stretch Goals)

- Sort tasks by due date or priority
- Add task categories
- Pretty CLI output with colors using colorama
- Export tasks to CSV
