# Week 04 Lab & Quiz - Savings Goal Planner

This folder contains the solution for the Week 04 Lab assignment: ⁠ lab04_savings_planner.py ⁠.

## Overview
The program is a Python-based savings planner that simulates a savings account growth month-by-month. It validates user inputs, calculates monthly interest followed by monthly deposits, prints a detailed month-by-month table, and stops when either the savings goal is reached or a 60-month limit is hit.


## Assignment Submission Details

•⁠  ⁠*AI Tool Used:* Gemini (AI Collaborator)
•⁠  ⁠*Prompt Used:* Create a Python console script for a savings goal planner that asks for a starting balance, a monthly deposit, a monthly interest rate (%), and a savings goal, with input validation, monthly simulation, a 60-month limit, and specific acceptance checks.
•⁠  ⁠*What did you change?* 
  - Adjusted the calculation sequence so that interest is added to the current balance before the monthly deposit is added, matching the exact lab requirements.
  - Added robust input validation (⁠ try-except ⁠ blocks and ⁠ while ⁠ loops) to re-prompt the user if negative numbers or non-numeric values are entered.
•⁠  ⁠*What does break do in your program?* 
  The ⁠ break ⁠ statement immediately terminates the monthly ⁠ for ⁠ loop as soon as the savings balance reaches or exceeds the target goal, ending the simulation early and proceeding to the final summary report.

## Testing and Results

### Test Scenario Run
•⁠  ⁠*Starting Balance:* 1000
•⁠  ⁠*Monthly Deposit:* 500
•⁠  ⁠*Monthly Interest Rate (%):* 1
•⁠  ⁠*Savings Goal:* 3000

*Result:* The goal was successfully reached in *4 months* with a final balance of *$3070.80* and a total interest earned of *$70.80*, matching the acceptance criteria precisely.

## How to Run
1.⁠ ⁠Make sure you have Python installed on your machine.
2.⁠ ⁠Navigate to your repository folder where ⁠ lab04_savings_planner.py ⁠ is saved (⁠ week04/lab-quiz/ ⁠).
3.⁠ ⁠Open your terminal or command prompt and run the script:
   ```bash
   python lab04_savings_planner.py
