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
🃏 Day 11 – Blackjack Game
📌 Project Overview

This project is a Blackjack game built using Python.
The player competes against the computer, and the winner is determined based on standard Blackjack rules.

💡 What I Learned
Writing reusable functions
Managing game flow using loops
Applying conditional logic
Working with lists and random module
Handling special cases like Blackjack (21) and Ace values
⚙️ How It Works
Both the user and computer are dealt two cards
The user can choose to:
Take another card (hit)
Stop (stand)
The computer draws cards until its score is at least 17
Scores are compared
The winner is displayed
🧠 Key Concepts Used
Functions
Lists
Loops (while)
Conditional statements
Random module
▶️ Example Output
Do you want to play a game of Blackjack? Type 'y' or 'n': y

Your cards: [10, 7], current score: 17
Computer's first card: 9

Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 7], final score: 17
Computer's final hand: [9, 8], final score: 17
Draw 🙃
# 🎯 Day 12 – Number Guessing Game

## 📌 Project Overview
This project is a Number Guessing Game built using Python.  
The player tries to guess a randomly chosen number between 1 and 100 within a limited number of attempts.

---

## 💡 What I Learned
- Writing reusable functions
- Using random number generation
- Managing attempts with variables
- Applying loops and conditional logic
- Building interactive command-line games

---

## ⚙️ How It Works
1. The program selects a random number between 1 and 100
2. The user chooses a difficulty:
   - Easy → 10 attempts
   - Hard → 5 attempts
3. The user enters guesses
4. The program gives hints:
   - Too high
   - Too low
5. The game ends when:
   - The user guesses correctly
   - Attempts run out

---

## 🧠 Key Concepts Used
- Functions
- Loops (`while`)
- Conditional statements
- Random module

---

## ▶️ Example Output
```python
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too low.
Guess again.
# 🐞 Day 13 – Debugging

## 📌 Overview
Today I focused on learning debugging techniques instead of building a project.

---

## 💡 What I Learned
- How to identify and describe problems in code  
- Reproducing bugs step by step  
- Tracing code execution line by line  
- Using print statements to debug  
- Introduction to debugging tools  

---

## 🧠 Key Takeaway
Debugging is an essential skill in programming.  
It helps in understanding code deeply and improving problem-solving ability.

---

## 🚀 Summary
Even without writing new code, today improved my logical thinking and ability to fix errors efficiently.
# 🎮 Day 14 – Higher Lower Game

## 📌 Overview
This project is a Higher Lower game where the user guesses which account has more followers.

---

## 💡 What I Learned
- Using dictionaries and lists
- Writing reusable functions
- Managing game loops
- Implementing scoring systems
- Handling user input and validation

---

## ⚙️ How It Works
1. Two accounts are displayed
2. User guesses which has more followers
3. If correct → score increases
4. If wrong → game ends

---

## 🧠 Key Concepts
- Functions
- Loops
- Conditionals
- Random module

---

# ☕ Coffee Machine Project (Day 15)

This project is a simple Coffee Machine simulation built using Python.  
It allows users to select drinks, insert coins, and receive coffee based on available resources.

---

## 🚀 Features
- Select drinks: Espresso, Latte, Cappuccino  
- Checks if enough ingredients are available  
- Accepts coin input from user  
- Validates payment and returns change  
- Tracks total profit  
- Displays a report of remaining resources  

---

## 🧠 Concepts Used
- Functions (modular programming)  
- Dictionaries for structured data  
- Conditional statements (if/elif/else)  
- While loops  
- User input handling  

---

## ⚙️ How It Works
1. User selects a drink  
2. Machine checks available resources  
3. User inserts coins  
4. Machine verifies payment  
5. Coffee is prepared  
6. Resources and profit are updated  

---

## ▶️ How to Run
Make sure Python is installed, then run:

```bash
python coffee_machine.py
# ☕ Day 16: OOP Coffee Machine

This project is an Object-Oriented Programming (OOP) version of the Coffee Machine built in Day 15 of the **100 Days of Code: The Complete Python Pro Bootcamp**.

## 🚀 Project Overview
The coffee machine simulation allows users to order drinks, process payments, and manage resources. In this version, the application is structured using classes to improve modularity, readability, and scalability.

## 🧠 OOP Concepts Applied
- **Classes and Objects** – Structured the program into reusable components.
- **Encapsulation** – Managed machine resources within class methods.
- **Abstraction** – Simplified complex operations like payment and drink preparation.
- **Modularity** – Separated responsibilities across different classes.

## 🏗️ Project Structure
The system is divided into the following classes:

- **MenuItem** – Represents a drink with its ingredients and cost.
- **Menu** – Manages available drinks and retrieves menu items.
- **CoffeeMaker** – Handles resource management and drink preparation.
- **MoneyMachine** – Processes coins, validates transactions, and tracks profit.
- **main.py** – Controls the program flow and user interaction.
# 🧠 Day 17 – True/False Quiz Game (OOP in Python)

This project is part of my **#100DaysOfCode** challenge.  
On Day 17, I built an interactive **True/False Quiz Game** using **Object-Oriented Programming (OOP)** in Python.

## 🚀 Features
- ✅ Interactive command-line quiz
- ✅ True/False question format
- ✅ Real-time feedback after each question
- ✅ Score tracking throughout the quiz
- ✅ Final score display at the end
- ✅ Clean and modular OOP-based design

## 🧠 Concepts Practiced
- Object-Oriented Programming (OOP)
- Classes and Objects
- Method creation and interaction
- Loops and Conditional Statements
- User Input Handling
- Working with Lists and Dictionaries

