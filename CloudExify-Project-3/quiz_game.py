"""
Project 3: Python Quiz Game
Author: Hamza Ali
Intern ID: CX-INT-2026-PY-0129
CloudExify Summer Internship 2026 - Month 2

✨ Features:
- 20+ Python questions
- Random order every game
- Score tracking + Grade (A-F)
- High score saved persistently
- Review wrong answers at the end (BONUS)
"""

import random
import os
from datetime import datetime

# ============================================
# PROFESSIONAL PATHING (Auto-saves in script folder)
# ============================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HIGHSCORE_FILE = os.path.join(SCRIPT_DIR, "highscore.txt")

# ============================================
# QUESTION BANK (20+ Questions on Python Basics)
# ============================================
QUESTIONS = [
    {
        "question": "What is the output of: print(2 * 3)?",
        "options": {"A": "6", "B": "8", "C": "9", "D": "23"},
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {"A": "function", "B": "define", "C": "def", "D": "func"},
        "answer": "C"
    },
    {
        "question": "What data type is: x = [1, 2, 3]?",
        "options": {"A": "tuple", "B": "dict", "C": "string", "D": "list"},
        "answer": "D"
    },
    {
        "question": "How do you get user input in Python?",
        "options": {"A": "get()", "B": "input()", "C": "read()", "D": "scan()"},
        "answer": "B"
    },
    {
        "question": "What does len([1, 2, 3, 4]) return?",
        "options": {"A": "3", "B": "5", "C": "4", "D": "0"},
        "answer": "C"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "options": {"A": "while", "B": "do-while", "C": "for", "D": "repeat"},
        "answer": "C"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": {"A": ".pyth", "B": ".pt", "C": ".py", "D": ".p"},
        "answer": "C"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": {"A": "^", "B": "**", "C": "*", "D": "exp"},
        "answer": "B"
    },
    {
        "question": "What is the output of: print('Hello' + 'World')?",
        "options": {"A": "Hello World", "B": "HelloWorld", "C": "Hello+World", "D": "Error"},
        "answer": "B"
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "options": {"A": "int", "B": "float", "C": "char", "D": "str"},
        "answer": "C"
    },
    {
        "question": "What does the 'if' statement do?",
        "options": {"A": "Loops", "B": "Conditional execution", "C": "Defines function", "D": "Imports module"},
        "answer": "B"
    },
    {
        "question": "How do you create a dictionary in Python?",
        "options": {"A": "{}", "B": "[]", "C": "()", "D": "<>"},
        "answer": "A"
    },
    {
        "question": "What is the output of: 10 // 3?",
        "options": {"A": "3.33", "B": "3", "C": "4", "D": "3.0"},
        "answer": "B"
    },
    {
        "question": "Which keyword is used to exit a loop?",
        "options": {"A": "exit", "B": "stop", "C": "break", "D": "return"},
        "answer": "C"
    },
    {
        "question": "What is the correct syntax to import a module?",
        "options": {"A": "import module", "B": "include module", "C": "using module", "D": "require module"},
        "answer": "A"
    },
    {
        "question": "Which function is used to print to the console?",
        "options": {"A": "print()", "B": "console.log()", "C": "echo()", "D": "write()"},
        "answer": "A"
    },
    {
        "question": "What is the output of: bool(0)?",
        "options": {"A": "True", "B": "False", "C": "0", "D": "Error"},
        "answer": "B"
    },
    {
        "question": "How do you add a comment in Python?",
        "options": {"A": "//", "B": "/*", "C": "#", "D": "--"},
        "answer": "C"
    },
    {
        "question": "What is the result of 2 ** 3?",
        "options": {"A": "6", "B": "8", "C": "9", "D": "5"},
        "answer": "B"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": {"A": "List", "B": "Tuple", "C": "Set", "D": "Dictionary"},
        "answer": "D"
    }
]


# ============================================
# HIGH SCORE FUNCTIONS
# ============================================
def load_high_score():
    """Load the highest score from file."""
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(score):
    """Save the new high score if it beats the current one."""
    current_high = load_high_score()
    if score > current_high:
        with open(HIGHSCORE_FILE, "w") as f:
            f.write(str(score))
        return True
    return False


# ============================================
# GAME LOGIC
# ============================================
def get_grade(score, total):
    """Calculate grade based on percentage."""
    percentage = (score / total) * 100
    if percentage >= 90:
        return "A", "🌟 Excellent! Outstanding performance!"
    elif percentage >= 80:
        return "B", "🎉 Great job! Very good performance!"
    elif percentage >= 70:
        return "C", "👍 Good. You passed with decent marks."
    elif percentage >= 60:
        return "D", "📖 You passed but needs improvement."
    else:
        return "F", "💪 You did not pass. Keep practicing!"


def ask_question(question_data, q_number, total):
    """Display a single question and get user input."""
    print(f"\n📌 Question {q_number} of {total}")
    print("-" * 40)
    print(question_data["question"])
    print()
    
    # Display options
    for letter, option in question_data["options"].items():
        print(f"   {letter}) {option}")
    print()
    
    # Get valid answer
    while True:
        answer = input("👉 Your answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        print("⚠️ Please enter A, B, C, or D only!")
    
    # Check correctness
    correct = question_data["answer"]
    if answer == correct:
        print("✅ CORRECT! Well done! 🎉")
        return True, None
    else:
        correct_text = question_data["options"].get(correct, "Unknown")
        print(f"❌ Wrong! Correct answer was {correct}) {correct_text}")
        return False, question_data["question"]


def play_quiz():
    """Main game function."""
    # Shuffle questions and pick 10
    shuffled_questions = QUESTIONS.copy()
    random.shuffle(shuffled_questions)
    game_questions = shuffled_questions[:10]
    total = len(game_questions)
    
    score = 0
    wrong_review = []  # Track wrong answers for review (BONUS)
    
    high_score = load_high_score()
    
    print("\n" + "=" * 45)
    print("  🧠 CLOUDEXIFY PYTHON QUIZ GAME")
    print("=" * 45)
    print(f"📝 Total Questions: {total}")
    print(f"🏆 Current High Score: {high_score}")
    print("📌 Answer with A, B, C, or D")
    print("=" * 45)
    input("Press Enter to start...")
    
    for i, question in enumerate(game_questions, 1):
        is_correct, q_text = ask_question(question, i, total)
        if is_correct:
            score += 1
        else:
            wrong_review.append(q_text)
    
    # Show results
    print("\n" + "=" * 45)
    print("  🏁 QUIZ COMPLETED!")
    print("=" * 45)
    print(f"✅ Score        : {score} / {total}")
    
    percentage = (score / total) * 100
    print(f"📊 Percentage  : {percentage:.1f}%")
    
    grade, message = get_grade(score, total)
    print(f"🏅 Grade       : {grade}")
    print(f"💬 {message}")
    print("=" * 45)
    
    # --- BONUS: Review Wrong Answers ---
    if wrong_review:
        print("\n📖 REVIEW WRONG ANSWERS (BONUS):")
        for i, q in enumerate(wrong_review, 1):
            print(f"   {i}. {q}")
        print()
    
    # --- High Score ---
    if save_high_score(score):
        print(f"🎉 NEW HIGH SCORE: {score}!")
    else:
        print(f"🏆 Current High Score: {load_high_score()}")
    
    return score


def main():
    """Main menu with play again option."""
    while True:
        play_quiz()
        print("\n" + "-" * 45)
        again = input("🔄 Play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\n👋 Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()