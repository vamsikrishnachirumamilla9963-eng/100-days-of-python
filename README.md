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
🔐 Day 8 — Caesar Cipher
📌 Project Description

Today I built a Caesar Cipher program that can encrypt and decrypt messages by shifting letters in the alphabet.

🚀 Features
Encode (encryption)
Decode (decryption)
Handles spaces, numbers, and symbols
Supports large shift values using modulo (%)
🧠 Concepts Used
Functions
Loops
Conditionals
Lists
String manipulation
Modulo operator (%)
💡 How It Works
Each letter is shifted by a given number
Encoding → shift forward
Decoding → shift backward
Wrap-around handled using % 26
🔍 Example
Input: hello
Shift: 3
Output: khoor
📂 File
caesar_cipher.py
🎯 What I Learned
Writing reusable functions
Handling edge cases (symbols, spaces)
Using modulo for circular logic
Building interactive programs
🏷️ Day 9 – Secret Auction Program
📌 Project Overview

This project is a Secret Auction Program built using Python.
It allows multiple users to place bids, and the program determines the highest bidder without revealing other bids.

💡 What I Learned
Using dictionaries to store key-value data (name → bid)
Writing functions to organize and reuse code
Iterating through data using loops
Applying conditional logic to find the highest value
⚙️ How It Works
Users enter their name and bid amount
The program stores each bid in a dictionary
It asks if there are more bidders
Once bidding ends, it calculates the highest bid
Displays the winner and their bid
🧠 Key Concepts Used
Python Dictionaries
Functions
Loops (for, while)
Conditional Statements (if-elif-else)
▶️ Example Output
What is your name?: Vamsi
What is your bid?: $100
Are there any other bidders? yes

What is your name?: John
What is your bid?: $150
Are there any other bidders? no

The winner is John with a bid of $150
🧮 Day 10 – Calculator Program
📌 Project Overview

This project is a Calculator Program built using Python.
It performs basic arithmetic operations and allows users to continue calculations using previous results.

💡 What I Learned
Writing reusable functions
Using dictionaries to map operations to functions
Managing program flow with loops
Handling user input in interactive programs
⚙️ How It Works
User enters the first number
Program displays available operations: +, -, *, /
User selects an operation
User enters the next number
Program calculates and displays the result
User can continue with the result or start a new calculation
🧠 Key Concepts Used
Functions
Dictionaries
Loops (while)
Conditional statements
User input handling
▶️ Example Output
What is the first number?: 10
+
-
*
/
Pick an operation: +
What is the next number?: 5
10.0 + 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculatio
