"""
Project 4: To-Do List Manager
Author: Hamza Ali
Intern ID: CX-INT-2026-PY-0129
CloudExify Summer Internship 2026 - Month 2

✨ Features:
- Add task (title, priority High/Medium/Low, due date)
- View tasks (sorted by priority)
- Mark task as done
- Delete task with confirmation
- Filter by status (pending/done)
- Filter by priority
- Statistics
- JSON persistence (auto-save after every action)
- Search by keyword (BONUS)
- Edit task (BONUS)
"""

import json
import os
from datetime import datetime

# ============================================
# PROFESSIONAL PATHING (Auto-saves in script folder)
# ============================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "tasks.json")

# Global variables
tasks = []
next_id = 1


# ============================================
# FILE OPERATIONS
# ============================================
def load_tasks():
    """Load tasks from JSON file. Auto-creates if missing."""
    global tasks, next_id
    
    if not os.path.exists(DATA_FILE):
        print("📂 No tasks found. Starting fresh!")
        tasks = []
        next_id = 1
        save_tasks()  # Create empty file
        return
    
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            tasks = data.get("tasks", [])
            next_id = data.get("next_id", 1)
            print(f"📂 Loaded {len(tasks)} tasks from file.")
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Error reading file. Starting with empty list.")
        tasks = []
        next_id = 1


def save_tasks():
    """Save all tasks to JSON file immediately."""
    data = {
        "tasks": tasks,
        "next_id": next_id
    }
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"❌ Error saving tasks: {e}")


# ============================================
# CORE FEATURES
# ============================================
def add_task():
    """Add a new task with validation."""
    global next_id
    
    print("\n--- ADD NEW TASK ---")
    
    # Title validation
    title = input("📝 Task title: ").strip()
    if not title:
        print("❌ Title cannot be empty!")
        return
    
    # Priority selection
    priority_map = {"1": "High", "2": "Medium", "3": "Low"}
    print("Priority: 1) High  2) Medium  3) Low")
    while True:
        choice = input("Select (1-3): ").strip()
        if choice in priority_map:
            priority = priority_map[choice]
            break
        print("⚠️ Please enter 1, 2, or 3!")
    
    # Due date
    due_date = input("📅 Due date (YYYY-MM-DD) or press Enter to skip: ").strip()
    if not due_date:
        due_date = "No due date"
    
    # Create task dictionary
    task = {
        "id": next_id,
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "status": "Pending",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    tasks.append(task)
    next_id += 1
    save_tasks()
    print(f"✅ Task added! ID: {task['id']} (Auto-saved)")


def view_tasks(filter_status=None, filter_priority=None):
    """Display tasks in a formatted table, sorted by priority."""
    display = tasks
    
    if filter_status:
        display = [t for t in tasks if t["status"] == filter_status]
    
    if filter_priority:
        display = [t for t in tasks if t["priority"] == filter_priority]
    
    if not display:
        print("\n📭 No tasks found matching the criteria!")
        return
    
    # Sort: High priority first
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    display = sorted(display, key=lambda t: priority_order.get(t["priority"], 4))
    
    print("\n" + "=" * 75)
    print(f"{'ID':<5} {'Title':<30} {'Priority':<10} {'Status':<10} {'Due Date'}")
    print("=" * 75)
    
    for t in display:
        status_icon = "✅ Done" if t["status"] == "Done" else "⏳ Pending"
        print(f"{t['id']:<5} {t['title'][:29]:<30} {t['priority']:<10} {status_icon:<10} {t['due_date']}")
    
    print("=" * 75)


def mark_done():
    """Mark a pending task as done."""
    pending_tasks = [t for t in tasks if t["status"] == "Pending"]
    if not pending_tasks:
        print("\n🎉 All tasks are done!")
        return
    
    view_tasks(filter_status="Pending")
    
    try:
        task_id = int(input("\n✅ Enter task ID to mark as done: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "Done":
                print("⚠️ Task is already done!")
                return
            task["status"] = "Done"
            save_tasks()
            print(f"✅ Task '{task['title']}' marked as done!")
            return
    
    print(f"❌ No task found with ID {task_id}")


def delete_task():
    """Delete a task with confirmation."""
    if not tasks:
        print("\n📭 No tasks to delete!")
        return
    
    view_tasks()
    
    try:
        task_id = int(input("\n🗑️ Enter task ID to delete: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return
    
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            confirm = input(f"⚠️ Delete '{task['title']}'? (yes/no): ").strip().lower()
            if confirm in ["yes", "y"]:
                tasks.pop(i)
                save_tasks()
                print("✅ Task deleted successfully!")
            else:
                print("❌ Deletion cancelled!")
            return
    
    print(f"❌ No task found with ID {task_id}")


def show_stats():
    """Display task statistics."""
    if not tasks:
        print("\n📭 No tasks to show stats for!")
        return
    
    total = len(tasks)
    done = sum(1 for t in tasks if t["status"] == "Done")
    pending = total - done
    high_pending = sum(1 for t in tasks if t["priority"] == "High" and t["status"] == "Pending")
    medium_pending = sum(1 for t in tasks if t["priority"] == "Medium" and t["status"] == "Pending")
    low_pending = sum(1 for t in tasks if t["priority"] == "Low" and t["status"] == "Pending")
    
    print("\n" + "=" * 40)
    print("📊 TASK STATISTICS")
    print("=" * 40)
    print(f"📌 Total Tasks      : {total}")
    print(f"✅ Completed        : {done}")
    print(f"⏳ Pending          : {pending}")
    print(f"   └─ High Priority : {high_pending}")
    print(f"   └─ Medium Priority: {medium_pending}")
    print(f"   └─ Low Priority  : {low_pending}")
    
    if total > 0:
        pct = (done / total) * 100
        print(f"\n📈 Completion Rate : {pct:.1f}%")
    
    # Progress bar (visual)
    bar_length = 20
    filled = int((done / total) * bar_length) if total > 0 else 0
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"   [{bar}] {pct:.0f}%")
    print("=" * 40)


# ============================================
# BONUS FEATURES (Extra Polish)
# ============================================
def search_tasks():
    """Search tasks by keyword in title."""
    if not tasks:
        print("\n📭 No tasks to search!")
        return
    
    keyword = input("\n🔍 Enter keyword to search: ").strip().lower()
    if not keyword:
        print("❌ Please enter a keyword!")
        return
    
    results = [t for t in tasks if keyword in t["title"].lower()]
    
    if not results:
        print(f"❌ No tasks found with '{keyword}'")
        return
    
    print(f"\n🔎 Found {len(results)} task(s) with '{keyword}':")
    for t in results:
        status_icon = "✅" if t["status"] == "Done" else "⏳"
        print(f"   {status_icon} [{t['id']}] {t['title']} ({t['priority']})")


def edit_task():
    """Edit an existing task's title or priority."""
    if not tasks:
        print("\n📭 No tasks to edit!")
        return
    
    view_tasks()
    
    try:
        task_id = int(input("\n✏️ Enter task ID to edit: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            print(f"\n📌 Editing: '{task['title']}'")
            print("Press Enter to keep current value.")
            
            # Edit title
            new_title = input(f"  New title (current: {task['title']}): ").strip()
            if new_title:
                task["title"] = new_title
            
            # Edit priority
            priority_map = {"1": "High", "2": "Medium", "3": "Low"}
            print("  Priority: 1) High  2) Medium  3) Low")
            choice = input(f"  New priority (current: {task['priority']}): ").strip()
            if choice in priority_map:
                task["priority"] = priority_map[choice]
            
            # Edit due date
            new_due = input(f"  New due date (current: {task['due_date']}): ").strip()
            if new_due:
                task["due_date"] = new_due
            
            save_tasks()
            print("✅ Task updated successfully!")
            return
    
    print(f"❌ No task found with ID {task_id}")


# ============================================
# MAIN MENU
# ============================================
def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 45)
    print("  📋 CLOUDEXIFY TO-DO LIST MANAGER")
    print("=" * 45)
    print("1.  Add Task")
    print("2.  View All Tasks")
    print("3.  View Pending Tasks")
    print("4.  View High Priority Tasks")
    print("5.  Mark Task as Done")
    print("6.  Delete Task")
    print("7.  Show Statistics")
    print("8.  Search Tasks (🔍 BONUS)")
    print("9.  Edit Task (✏️ BONUS)")
    print("10. Exit (Auto-saves)")
    print("=" * 45)


def main():
    """Main program loop."""
    print("\n🚀 Welcome to CloudExify To-Do List Manager!")
    load_tasks()
    
    while True:
        show_menu()
        choice = input("Choose (1-10): ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks(filter_status="Pending")
        elif choice == "4":
            view_tasks(filter_priority="High")
        elif choice == "5":
            mark_done()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            show_stats()
        elif choice == "8":
            search_tasks()  # BONUS
        elif choice == "9":
            edit_task()     # BONUS
        elif choice == "10":
            save_tasks()
            print("\n👋 Goodbye! All tasks saved.")
            break
        else:
            print("❌ Invalid choice! Please enter 1-10.")


if __name__ == "__main__":
    main()