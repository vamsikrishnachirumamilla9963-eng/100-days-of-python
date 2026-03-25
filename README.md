🚀 100 Days of Python

Welcome to my #100DaysOfCode journey 👨‍💻
I’m learning Python by building projects every day and improving my problem-solving skills.

📌 About This Repository

This repository contains my daily progress, projects, and learnings from the 100 Days of Python Bootcamp.

🟢 Day 1 – Band Name Generator
Learned Python basics
Worked with user input and variables
Built a simple fun project
🟢 Day 2 – Tip Calculator
Practiced calculations and type conversion
Improved logic building
Built a real-world mini project
🟢 Day 3 – Treasure Island Game
Learned conditionals (if-elif-else)
Built a decision-based game
Improved logical thinking
🟢 Day 4 – Rock-Paper-Scissors 🎮
Learned lists and indexing
Used random module
Built a game using logic and randomization
🟢 Day 5 – Password Generator 🔐
Used lists for storing characters
Applied random.choice() & random.shuffle()
Generated strong and secure passwords
# 🚀 Day 6 – Maze Solver (Reeborg World)

## 📌 Problem
Build a program to guide a robot through a maze and reach the goal.

## 🧠 Approach
I used the **Right Wall Following Algorithm**:
- If the right path is clear → turn right and move
- Else if the front is clear → move forward
- Else → turn left

This method ensures the robot eventually finds the exit.

## 💻 Code

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
# 🎯 Day 7 – Hangman Game (Python)

## 📌 Project Overview
Today’s project is a **Hangman Game** built using Python.  
The game randomly selects a word, and the player must guess it letter by letter before running out of lives.

---

## 🚀 Features
- Random word selection using `random`
- Tracks player lives (6 attempts)
- Displays word progress with `_`
- Prevents repeated guesses
- Shows win/lose messages
- Visual hangman stages for each wrong guess

---

## 🧠 Concepts Practiced
- Python loops (`while`, `for`)
- Conditional statements (`if-else`)
- Lists and string manipulation
- Importing modules/files
- Game logic building

---
