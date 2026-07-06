"""
CloudExify Python Internship - Month 1
Project: Personal Expense Tracker
Author: Hamza Ali
Intern ID: CX-INT-2026-PY-0129

✨ UPDATED: Auto-save after every action. JSON file auto-creates.
"""

import json
import os

# File to store expenses
import os

# Get the folder where this Python file is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Create the full path to the JSON file in the SAME folder
DATA_FILE = os.path.join(SCRIPT_DIR, "expenses.json")

# Predefined categories
CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Other"]

# Global list to hold all expenses
expenses = []
next_id = 1


def load_expenses():
    """Load expenses from JSON file. Auto-creates if missing."""
    global expenses, next_id

    # If file doesn't exist, CREATE it automatically!
    if not os.path.exists(DATA_FILE):
        print("📂 No previous data found. Creating new expenses.json...")
        default_data = {"expenses": [], "next_id": 1}
        with open(DATA_FILE, "w") as f:
            json.dump(default_data, f, indent=4)
        print("✅ expenses.json created successfully!")
        return

    # If file exists, load it
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            expenses = data.get("expenses", [])
            next_id = data.get("next_id", 1)
            print(f"📂 Loaded {len(expenses)} expenses from file.")
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Error reading file. Starting with empty list.")


def save_expenses():
    """Save all expenses to JSON file."""
    data = {
        "expenses": expenses,
        "next_id": next_id
    }
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"❌ Error saving: {e}")


def add_expense():
    """Add a new expense with validation and AUTO-SAVE."""
    global next_id

    print("\n--- ADD NEW EXPENSE ---")

    # Get description
    description = input("Description: ").strip()
    if not description:
        print("❌ Description cannot be empty!")
        return

    # Get amount with validation
    while True:
        try:
            amount = float(input("Amount (PKR): "))
            if amount <= 0:
                print("❌ Amount must be greater than 0!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")

    # Show categories and get choice
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choice = int(input("Select category (1-5): "))
            if 1 <= choice <= len(CATEGORIES):
                category = CATEGORIES[choice - 1]
                break
            print("❌ Please select 1-5!")
        except ValueError:
            print("❌ Please enter a number!")

    # Create expense dictionary
    expense = {
        "id": next_id,
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    next_id += 1

    # 🔥 AUTO-SAVE IMMEDIATELY!
    save_expenses()
    print(f"✅ Expense added! ID: {expense['id']} (Auto-saved)")


def view_expenses():
    """Display all expenses in a formatted table."""
    if not expenses:
        print("\n📭 No expenses yet. Add some first!")
        return

    print("\n--- ALL EXPENSES ---")
    print(f"{'ID':<5} {'Description':<20} {'Category':<12} {'Amount':>10}")
    print("-" * 50)

    total = 0
    for exp in expenses:
        print(f"{exp['id']:<5} {exp['description']:<20} {exp['category']:<12} PKR {exp['amount']:>8.2f}")
        total += exp['amount']

    print("-" * 50)
    print(f"{'TOTAL':<38} PKR {total:>8.2f}")


def category_summary():
    """Show total spending per category with percentages."""
    if not expenses:
        print("\n📭 No expenses to summarize!")
        return

    # Calculate totals per category
    summary = {}
    for exp in expenses:
        cat = exp['category']
        summary[cat] = summary.get(cat, 0) + exp['amount']

    total = sum(exp['amount'] for exp in expenses)

    print("\n--- CATEGORY SUMMARY ---")
    for cat, amount in summary.items():
        percentage = (amount / total) * 100
        print(f"{cat:<12}: PKR {amount:>8.2f} ({percentage:.1f}%)")

    print(f"\nTotal Spending: PKR {total:.2f}")


def filter_by_category():
    """Filter and display expenses by category."""
    if not expenses:
        print("\n📭 No expenses to filter!")
        return

    print("\n--- FILTER BY CATEGORY ---")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choice = int(input("Select category (1-5): "))
            if 1 <= choice <= len(CATEGORIES):
                selected_cat = CATEGORIES[choice - 1]
                break
            print("❌ Please select 1-5!")
        except ValueError:
            print("❌ Please enter a number!")

    # Filter expenses
    filtered = [e for e in expenses if e['category'] == selected_cat]

    if not filtered:
        print(f"\n📭 No expenses found in category: {selected_cat}")
        return

    print(f"\n--- EXPENSES IN '{selected_cat}' ---")
    print(f"{'ID':<5} {'Description':<20} {'Amount':>10}")
    print("-" * 40)

    total = 0
    for exp in filtered:
        print(f"{exp['id']:<5} {exp['description']:<20} PKR {exp['amount']:>8.2f}")
        total += exp['amount']

    print("-" * 40)
    print(f"Total in '{selected_cat}': PKR {total:.2f}")


def delete_expense():
    """Delete an expense by ID with confirmation and AUTO-SAVE."""
    if not expenses:
        print("\n📭 No expenses to delete!")
        return

    # Show current expenses first
    view_expenses()

    try:
        exp_id = int(input("\nEnter the ID of expense to delete: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return

    # Find the expense
    found = None
    for exp in expenses:
        if exp['id'] == exp_id:
            found = exp
            break

    if not found:
        print(f"❌ No expense found with ID: {exp_id}")
        return

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete '{found['description']}'? (y/n): ").lower()
    if confirm != 'y':
        print("❌ Deletion cancelled!")
        return

    expenses.remove(found)

    # 🔥 AUTO-SAVE IMMEDIATELY!
    save_expenses()
    print(f"✅ Expense ID {exp_id} deleted successfully! (Auto-saved)")


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 45)
    print("     CLOUDEXIFY EXPENSE TRACKER")
    print("=" * 45)
    print("1.  Add Expense")
    print("2.  View All Expenses")
    print("3.  Category Summary")
    print("4.  Filter by Category")
    print("5.  Delete Expense")
    print("6.  Exit (Auto-saves on close)")  # Updated label
    print("=" * 45)


def main():
    """Main program loop."""
    print("\n🚀 Welcome to CloudExify Expense Tracker!")
    
    # This will auto-create the file if missing
    load_expenses()

    while True:
        show_menu()
        choice = input("Select option (1-6): ").strip()

        if choice == "1":
            add_expense()  # Auto-saves inside
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            delete_expense()  # Auto-saves inside
        elif choice == "6":
            save_expenses()  # Final safety save
            print("\n👋 Goodbye! All data saved.")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")


if __name__ == "__main__":
    main()
