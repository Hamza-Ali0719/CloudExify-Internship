# 🧠 Python Quiz Game

A fun and interactive command-line quiz game designed to test and improve your Python knowledge.

---

## 📌 Overview

This project was developed as part of the **CloudExify Summer Internship 2026 (Project 3)**.
The game dynamically selects 10 random questions from a pool of 20+ Python-related questions, ensuring a unique experience each time you play.

It tracks your performance, assigns a grade (A–F), and stores your highest score locally so you can continuously challenge yourself.

---

## 👨‍💻 Author

**Hamza Ali**
📧 [hamzaali.se24@gmail.com](mailto:hamzaali.se24@gmail.com)
📛 Intern ID: CX-INT-2026-PY-0129
🏢 CloudExify Summer Internship 2026 (Month 2)

---

## ✨ Features

* **Extensive Question Bank**
  20+ questions covering Python fundamentals, including loops, functions, and data types.

* **Randomized Gameplay**
  Questions are shuffled every time for a fresh experience.

* **Real-Time Feedback**
  Instant response after each answer.

* **Grading System (A–F)**
  Performance evaluation based on your score.

* **High Score Tracking**
  Automatically saves and loads the highest score using `highscore.txt`.

* **Wrong Answer Review** *(Bonus)*
  Review incorrectly answered questions at the end.

* **Replay Option**
  Play multiple rounds and improve your score.

---

## ⚙️ Tech Stack

* **Python 3.x**
* Built-in Libraries:

  * `random`
  * `os`
  * `datetime`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Hamza-Ali0719/cloudexify-python-p3-hamzaali.git
cd cloudexify-python-p3-hamzaali
```

### 2. Run the Application

```bash
python quiz_game.py
```

### 3. Play the Game

* Enter `A`, `B`, `C`, or `D` to answer questions.
* Press **Enter** to start.
* Type `yes` or `y` to play again.

---

## 📁 Project Structure

```
cloudexify-python-p3-hamzaali/
├── quiz_game.py          # Main application file
├── highscore.txt         # Stores highest score (auto-generated)
├── README.md             # Project documentation
└── screenshots/          # Optional: Add gameplay screenshots
```

---

## 📊 Sample Output

```
🧠 CLOUDEXIFY PYTHON QUIZ GAME
=============================================
📝 Total Questions: 10
🏆 Current High Score: 8
📌 Answer with A, B, C, or D
=============================================

📌 Question 1 of 10
----------------------------------------
What is the output of: print(2 * 3)?

   A) 6
   B) 8
   C) 9
   D) 23

👉 Your answer (A/B/C/D): A
✅ CORRECT! Well done! 🎉

...

🏁 QUIZ COMPLETED!
=============================================
✅ Score        : 8 / 10
📊 Percentage   : 80.0%
🏅 Grade        : B
💬 🎉 Great job! Very good performance!
=============================================
```

---

## 🔮 Future Enhancements

* Add a **timer** (e.g., 30 seconds per question)
* Introduce **difficulty levels** (Easy / Medium / Hard)
* Implement a **leaderboard** for multiple players
* Convert into a **GUI-based application** (Tkinter / Web App)

---

## 📎 License

This project is developed for educational purposes as part of the **CloudExify Summer Internship Program 2026**.
