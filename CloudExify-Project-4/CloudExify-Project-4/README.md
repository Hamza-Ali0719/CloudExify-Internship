# 📋 To-Do List Manager

A feature-rich command-line task manager designed to help you stay organized and boost productivity.

---

## 📌 Overview

This project was developed as part of the **CloudExify Summer Internship 2026 (Project 4)**.
It enables users to efficiently manage daily tasks by adding, viewing, filtering, updating, and deleting tasks with priorities and due dates.

All data is stored persistently in a structured JSON file, ensuring that tasks remain محفوظ (saved) even after the application is closed.

---

## 👨‍💻 Author

**Hamza Ali**
📧 [hamzaali.se24@gmail.com](mailto:hamzaali.se24@gmail.com)
📛 Intern ID: CX-INT-2026-PY-0129
🏢 CloudExify Summer Internship 2026 (Month 2)

---

## ✨ Features

* **Task Creation**
  Add tasks with title, priority (High / Medium / Low), and due date.

* **Task Viewing**
  Display all tasks sorted by priority (High → Low).

* **Filtering Options**

  * Filter by status (Pending / Completed)
  * Filter by priority (e.g., High priority only)

* **Task Completion**
  Mark tasks as done quickly.

* **Safe Deletion**
  Delete tasks with confirmation prompts.

* **Statistics Dashboard**
  View total, completed, pending, and priority-wise breakdown with a visual progress bar.

* **Persistent Storage**
  Automatic saving using `tasks.json`.

* **Search Functionality (Bonus)**
  Find tasks instantly using keywords.

* **Task Editing (Bonus)**
  Update task title, priority, and due date.

---

## ⚙️ Tech Stack

* **Python 3.x**
* Built-in Libraries:

  * `json`
  * `datetime`
  * `os`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash id="clone-repo"
git clone https://github.com/Hamza-Ali0719/cloudexify-python-p4-hamzaali.git
cd cloudexify-python-p4-hamzaali
```

### 2. Run the Application

```bash id="run-app"
python todo_manager.py
```

### 3. Use the Application

* Select options from the menu (e.g., `1–10`)
* Follow on-screen prompts
* Tasks are automatically saved in `tasks.json`

---

## 📸 Screenshots

> Add screenshots of your application interface below:

* `screenshots/main_menu.png`
* `screenshots/view_tasks.png`

---

## 📁 Project Structure

```
cloudexify-python-p4-hamzaali/
├── todo_manager.py       # Main application logic
├── tasks.json            # Persistent task storage (auto-generated)
├── README.md             # Project documentation
└── screenshots/          # Optional screenshots
```

---

## 🧩 Data Structure (JSON)

Each task is stored as an object inside a list:

```json id="json-example"
{
  "tasks": [
    {
      "id": 1,
      "title": "Complete Python project",
      "priority": "High",
      "due_date": "2026-08-15",
      "status": "Pending",
      "created": "2026-07-28 14:30"
    }
  ],
  "next_id": 2
}
```

---

## 📊 Sample Output (Statistics)

```
📊 TASK STATISTICS
========================================
📌 Total Tasks       : 5
✅ Completed         : 2
⏳ Pending           : 3
   └─ High Priority  : 1
   └─ Medium Priority: 1
   └─ Low Priority   : 1

📈 Completion Rate   : 40.0%
   [████████░░░░░░░░░░░░] 40%
========================================
```

---

## 🔮 Future Enhancements

* Highlight **overdue tasks** automatically
* Add **task categories** (Work / Study / Personal)
* Export tasks to **CSV format** for reporting
* Build a **GUI or web-based interface**

---

## 📎 License

This project is developed for educational purposes as part of the **CloudExify Summer Internship Program 2026**.
