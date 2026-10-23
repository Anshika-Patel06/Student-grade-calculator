
# Student Grade Calculator

A simple command-line mini project in Python that calculates a student's total marks, percentage and grade from the marks of five subjects.

## Features

- Takes the student's name and marks for 5 subjects as input
- Calculates total marks (out of 500)
- Calculates percentage
- Assigns a grade based on the percentage
- Displays a clean final result

## Grading Scale

| Percentage | Grade |
|------------|-------|
| 90 and above | A+ |
| 80 – 89.99 | A |
| 70 – 79.99 | B |
| 60 – 69.99 | C |
| 40 – 59.99 | D |
| Below 40 | Fail |

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Anshika-Patel06/Student-grade-calculator.git
   cd Student-grade-calculator
   ```
2. Run the program:
   ```bash
   python grade_calculator.py
   ```
3. Enter the student's name and the marks for each of the 5 subjects when prompted.

## Example

```
Enter student name: Anshika
Enter marks for subject1: 85
Enter marks for subject2: 78
Enter marks for subject3: 92
Enter marks for subject4: 88
Enter marks for subject5: 80

--- STUDENT NAME ---
Name: Anshika
Total marks: 423.0 /500
Percentage: 84.6 %
Grade: A

--- RESULT DECLARED---
```

## How It Works

The program is built from three small functions:

- `calculate_total(marks)` – adds up the marks of all subjects
- `calculate_percentage(total)` – converts the total into a percentage out of 500
- `calculate_grade(percentage)` – returns the grade using the grading scale above

## Possible Improvements

- Validate that marks are between 0 and 100
- Support a variable number of subjects
- Handle many students and save results to a file

## Author

**Anshika Patel**
B.Tech CSE (AI/ML), Quad AI School of Technology and Management
[GitHub](https://github.com/Anshika-Patel06) · [LinkedIn](https://www.linkedin.com/in/anshika-patel-6a51bb401)
