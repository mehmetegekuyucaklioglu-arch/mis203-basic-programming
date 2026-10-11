 Week 03

AI Tool Used:Gemini
Prompt Used:"His week you will combine everything you have learned so far: input, type conversion, f-strings, loops, and this week's new topic conditions.
What did you change? : I adjusted the base prices to 250 TRY for weekdays and 300 TRY for weekends, and added `.lower()` to input strings to handle case-insensitivity.

 Tests:

1.Input: Name: Zeynep | Age: 22 | Day: weekday | Student: yes
Result:`Zeynep: 175.00 TRY (Student)`
2.Input: Name: Ali | Age: 5 (Boundary Age) | Day: weekend | Student: no
Result:`Ali: 0.00 TRY (Free)`
3.Input: Name: Ahmet | Age: 130
Result:`Invalid age.`
4.Input: Name: Ayşe | Age: 70 | Day: weekday | Student: no
Result:`Ayşe: 125.00 TRY (Senior)`
5.Input: Name: Mehmet | Age: 10 | Day: weekend | Student: no
Result:`Mehmet: 180.00 TRY (Child)`
6.Input: Name: Elif | Age: 30 | Day: weekday | Student: no
Result:`Elif: 250.00 TRY (Standard)`
7.nput: Name: Can | Age: 20 | Day: holiday | Student: yes
Result:`Invalid day.`
8.Input: Name: Deniz | Age: 20 | Day: weekday | Student: maybe
Result:`Please answer yes or no.`
9.Input: Name: Ece | Age: 5 (Boundary Age) | Day: weekday | Student: yes
Result:`Ece: 0.00 TRY (Free)`
10.Input: `q`
Result: Program ends and displays the ticket summary.











WEEK 04:
# Campus Cafe Order Automation ☕

A robust Python console application developed for managing a campus cafe's ordering process, calculating discounts, handling validation safely, and generating daily cash register reports.

## Repository & Course Info
- **Repository Name:** `mis203-basic-programming`
- **Script File:** `campus_cafe.py`
- **Course:** Management Information Systems (MIS) Python Laboratory

## Features

- **Interactive Order Management:** Allows entering customer names, selecting products, and processing orders dynamically using a `while` loop.
- **Robust Input Validation:** Prevents crashes from empty names or invalid product choices using conditional statements and flow control (`continue`).
- **Student Discount Policy:** Automatically applies a 25% discount for students.
- **Built-in Python Libraries:**
  - `random`: Integrates a 10% chance for a lucky surprise 50% discount draw.
  - `math`: Rounds up final pricing neatly using `math.ceil()`.
- **Daily Executive Report:** Tracks total items sold, lucky draw winners, and total revenue upon quitting (`q`).

## Menu & Pricing

| Product ID | Product Name | Base Price (TL) |
| :---: | :--- | :---: |
| **1** | Coffee | 80 TL |
| **2** | Sandwich | 120 TL |
| **3** | Dessert | 90 TL |

## Week 04 Assignment Submission Details

- **AI Tool Used:** None
- **Prompt Used:** Create a Python console script for a campus cafe order system using a `while` loop, conditionals (`if-elif-else`), `input()`, `print()`, and at least two built-in libraries (`random` and `math`) without using advanced functions (`def`).
- **What did you change?** Added robust input validation (`.strip()`, `.lower()`, and empty string checks) to prevent the program from crashing on unexpected user entries. Integrated `random` for a surprise discount draw and `math.ceil()` for clean price rounding.
- **What does break do in your program?** The `break` statement immediately terminates the `while` loop when the user types `'q'`, exiting the ordering process and safely triggering the final daily revenue report.

## How to Run

1. Make sure you have Python installed on your machine.
2. Clone the repository `mis203-basic-programming` or download the `campus_cafe.py` file.
3. Open your terminal or command prompt and run the script:
   ```bash
   python campus_cafe.py






