"""
CloudExify Python Internship - Month 1
Project 2: Student Grade Management System
Author: Hamza Ali
Intern ID: CX-INT-2026-PY-0129

✨ Auto-creates CSV, Auto-saves after every action.
"""

import os
import csv

# ---------- CONSTANTS ----------
# Get the folder where this Python file is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# CSV file path (saves right next to this .py file)
CSV_FILE = os.path.join(SCRIPT_DIR, "students.csv")

# Fixed subjects as per project guide
SUBJECTS = ["Math", "Physics", "English", "Computer", "Urdu"]
PASS_MARK = 40

# Global list to hold all student records
students = []
next_id = 1


# ---------- FILE HANDLING (Auto-Create + Auto-Save) ----------
def load_data():
    """Load students from CSV. Auto-creates the file if missing."""
    global students, next_id

    # If file doesn't exist, CREATE it automatically with headers!
    if not os.path.exists(CSV_FILE):
        print("📂 No previous data found. Creating students.csv...")
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Write header row
            writer.writerow(["ID", "Name"] + SUBJECTS)
        print("✅ students.csv created successfully!")
        return

    # If file exists, load it
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                student = {
                    "id": int(row["ID"]),
                    "name": row["Name"],
                    "grades": {}
                }
                # Load grades for each subject
                for sub in SUBJECTS:
                    student["grades"][sub] = float(row[sub]) if row[sub] else 0.0
                students.append(student)

            # Update next_id based on max ID
            if students:
                next_id = max(s["id"] for s in students) + 1

        print(f"📂 Loaded {len(students)} students from file.")
    except Exception as e:
        print(f"⚠️ Error reading file: {e}. Starting fresh.")


def save_data():
    """Save all students to CSV immediately."""
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Write header
            writer.writerow(["ID", "Name"] + SUBJECTS)
            # Write data rows
            for s in students:
                row = [s["id"], s["name"]]
                for sub in SUBJECTS:
                    row.append(s["grades"].get(sub, 0.0))
                writer.writerow(row)
    except Exception as e:
        print(f"❌ Error saving data: {e}")


# ---------- HELPER FUNCTIONS ----------
def calculate_average(student):
    """Return average grade for a student."""
    grades = student["grades"].values()
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def get_status(student):
    """Return PASS or FAIL based on average."""
    avg = calculate_average(student)
    return "PASS" if avg >= PASS_MARK else "FAIL"


# ---------- CORE FEATURES ----------
def add_student():
    """Add a new student with grades. Auto-saves."""
    global next_id

    print("\n--- ADD NEW STUDENT ---")
    name = input("Student Name: ").strip()

    if not name:
        print("❌ Name cannot be empty!")
        return

    # Check for duplicate name (case-insensitive)
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"❌ Student '{name}' already exists!")
            return

    # Enter grades
    grades = {}
    print(f"\nEnter grades for {name} (0-100):")
    for sub in SUBJECTS:
        while True:
            try:
                grade = float(input(f"  {sub}: "))
                if 0 <= grade <= 100:
                    grades[sub] = grade
                    break
                else:
                    print("❌ Grade must be between 0 and 100!")
            except ValueError:
                print("❌ Please enter a valid number!")

    # Create student record
    student = {
        "id": next_id,
        "name": name,
        "grades": grades
    }

    students.append(student)
    next_id += 1

    # 🔥 AUTO-SAVE IMMEDIATELY!
    save_data()

    avg = calculate_average(student)
    print(f"✅ Student '{name}' added! (ID: {student['id']}) | Avg: {avg:.1f} | {get_status(student)} (Auto-saved)")


def view_all_students():
    """Display all students in a formatted table."""
    if not students:
        print("\n📭 No students yet. Add some first!")
        return

    print("\n--- ALL STUDENTS ---")
    # Print header
    header = f"{'ID':<5} {'Name':<15}"
    for sub in SUBJECTS:
        header += f" {sub:<8}"
    header += f" {'Avg':<6} {'Status'}"
    print(header)
    print("-" * (len(header) + 20))

    for s in students:
        avg = calculate_average(s)
        status = get_status(s)
        row = f"{s['id']:<5} {s['name']:<15}"
        for sub in SUBJECTS:
            row += f" {s['grades'].get(sub, 0):<8.1f}"
        row += f" {avg:<6.1f} {status}"
        print(row)


def class_report():
    """Show rankings, highest, lowest, class average."""
    if not students:
        print("\n📭 No students to report!")
        return

    # Calculate averages for ranking
    ranked = []
    for s in students:
        avg = calculate_average(s)
        ranked.append((s["name"], avg, s["id"]))

    # Sort by average descending (highest first)
    ranked.sort(key=lambda x: x[1], reverse=True)

    # Overall stats
    all_avgs = [r[1] for r in ranked]
    class_avg = sum(all_avgs) / len(all_avgs)
    highest = max(all_avgs)
    lowest = min(all_avgs)

    passed = sum(1 for avg in all_avgs if avg >= PASS_MARK)
    failed = len(all_avgs) - passed

    print("\n=== 📊 CLASS REPORT ===")
    print(f"Total Students   : {len(students)}")
    print(f"Class Average    : {class_avg:.2f}")
    print(f"Highest Average  : {highest:.2f}")
    print(f"Lowest Average   : {lowest:.2f}")
    print(f"Passed           : {passed}")
    print(f"Failed           : {failed}")

    print("\n--- 🏆 RANKINGS ---")
    for rank, (name, avg, s_id) in enumerate(ranked, 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"{rank}."
        print(f" {medal} {name:<15} (ID: {s_id}) | Avg: {avg:.2f}")


def search_student():
    """Search by name and show full grade card."""
    if not students:
        print("\n📭 No students to search!")
        return

    name = input("\nEnter student name to search: ").strip().lower()
    if not name:
        print("❌ Name cannot be empty!")
        return

    found = None
    for s in students:
        if s["name"].lower() == name:
            found = s
            break

    if not found:
        print(f"❌ Student '{name}' not found!")
        return

    # Display grade card
    print(f"\n--- GRADE CARD: {found['name']} (ID: {found['id']}) ---")
    total = 0
    for sub in SUBJECTS:
        grade = found["grades"].get(sub, 0)
        print(f"  {sub:<10}: {grade:.1f}")
        total += grade

    avg = total / len(SUBJECTS)
    print("-" * 25)
    print(f"  Average    : {avg:.1f}")
    print(f"  Status     : {get_status(found)}")


def edit_grades():
    """Edit grades for an existing student. Auto-saves."""
    if not students:
        print("\n📭 No students to edit!")
        return

    view_all_students()

    try:
        s_id = int(input("\nEnter Student ID to edit: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return

    found = None
    for s in students:
        if s["id"] == s_id:
            found = s
            break

    if not found:
        print(f"❌ No student found with ID: {s_id}")
        return

    print(f"\nEditing grades for: {found['name']} (ID: {found['id']})")
    print("Current grades:")
    for sub in SUBJECTS:
        print(f"  {sub}: {found['grades'].get(sub, 0):.1f}")

    # Update grades
    print("\nEnter new grades (0-100). Press Enter to keep current value:")
    for sub in SUBJECTS:
        while True:
            current = found["grades"].get(sub, 0)
            new_val = input(f"  {sub} (current: {current:.1f}): ").strip()
            if new_val == "":
                break  # Keep current
            try:
                grade = float(new_val)
                if 0 <= grade <= 100:
                    found["grades"][sub] = grade
                    break
                else:
                    print("❌ Must be 0-100!")
            except ValueError:
                print("❌ Enter a valid number!")

    # 🔥 AUTO-SAVE IMMEDIATELY!
    save_data()

    avg = calculate_average(found)
    print(f"✅ Grades updated for {found['name']}! New Avg: {avg:.1f} | {get_status(found)} (Auto-saved)")


def delete_student():
    """Delete a student by ID. Auto-saves."""
    if not students:
        print("\n📭 No students to delete!")
        return

    view_all_students()

    try:
        s_id = int(input("\nEnter Student ID to delete: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return

    found = None
    for i, s in enumerate(students):
        if s["id"] == s_id:
            found = i
            break

    if found is None:
        print(f"❌ No student found with ID: {s_id}")
        return

    confirm = input(f"Are you sure you want to delete '{students[found]['name']}'? (y/n): ").lower()
    if confirm != 'y':
        print("❌ Deletion cancelled!")
        return

    deleted_name = students[found]["name"]
    del students[found]

    # 🔥 AUTO-SAVE IMMEDIATELY!
    save_data()
    print(f"✅ Student '{deleted_name}' deleted successfully! (Auto-saved)")


# ---------- MENU ----------
def show_menu():
    print("\n" + "=" * 50)
    print("     CLOUDEXIFY GRADE MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1.  Add Student")
    print("2.  View All Students")
    print("3.  Class Report (Rankings)")
    print("4.  Search Student")
    print("5.  Edit Grades")
    print("6.  Delete Student")
    print("7.  Exit (Auto-saves)")
    print("=" * 50)


def main():
    print("\n🚀 Welcome to CloudExify Grade Management System!")
    load_data()

    while True:
        show_menu()
        choice = input("Select option (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            class_report()
        elif choice == "4":
            search_student()
        elif choice == "5":
            edit_grades()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            save_data()
            print("\n👋 Goodbye! All data saved.")
            break
        else:
            print("❌ Invalid choice! Please enter 1-7.")


if __name__ == "__main__":
    main()
      
