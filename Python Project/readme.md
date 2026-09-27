# Student Expense Tracker

## About the Project

Student Expense Tracker is a simple Python project made to keep track of daily expenses.

As a student, it can be difficult to remember where money is being spent. This project helps to record expenses and check the total amount spent. Expenses can also be viewed according to their categories.

I made this project using basic Python concepts like functions, loops, conditions, file handling and CSV files.

## Features

The project has the following options:

1. Add Expense
2. View Expenses
3. Calculate Total Expense
4. View Category Summary
5. Delete Expense
6. Exit

### Add Expense

The user can enter:

* Date
* Expense name
* Category
* Amount

The information is saved in a CSV file.

### View Expenses

This option displays all the expenses that have been added to the file.

### Total Expense

This option calculates the total amount spent on all recorded expenses.

### Category Summary

Expenses are grouped according to their category, such as Food, Travel, Study, Shopping, etc.

### Delete Expense

If an expense was added by mistake, it can be deleted by entering its number.

## Technologies Used

* Python
* CSV file
* Basic file handling

No external Python libraries are required for this project.

## How to Run

### Step 1

Install Python on your computer.

### Step 2

Download or clone this project.

### Step 3

Open the project folder in VS Code or any Python editor.

### Step 4

Run the following command:

```bash
python student_expense_tracker.py
```

The program will create an `expenses.csv` file automatically when it is run for the first time.

## Project Files

```text
StudentExpenseTracker/
│
├── student_expense_tracker.py
├── expenses.csv
└── README.md
```

`student_expense_tracker.py` contains the main Python program.

`expenses.csv` stores the expense information.

`README.md` contains the information about the project.

## Example

When the program starts, it shows a menu like this:

```text
==============================
     STUDENT EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Total Expense
4. Category Summary
5. Delete Expense
6. Exit
==============================
```

For example, I can add an expense like:

```text
Date: 27-09-2026
Expense: Lunch
Category: Food
Amount: 120
```

The expense is then stored in the CSV file.

## Learning From This Project

While making this project, I learned how to use functions in Python and how different functions can be connected through a menu. I also learned how to read and write data in a CSV file.

The project helped me understand basic file handling and also gave me practice with conditions, loops and dictionaries.

## Future Improvements

Some features that can be added later are:

* Monthly expense reports
* A budget limit
* A graphical user interface
* Expense charts
* Search option for expenses

## Conclusion

Student Expense Tracker is a basic Python project for managing daily expenses. It is simple to use and can be improved with more features in the future.
