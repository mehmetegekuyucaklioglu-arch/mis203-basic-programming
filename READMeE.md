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
