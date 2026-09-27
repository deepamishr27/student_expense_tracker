import csv
import os

file_name = "expenses.csv"
def create_file():
    if not os.path.exists(file_name):
        file = open(file_name, "w", newline="")
        writer = csv.writer(file)
        writer.writerow(["Date", "Expense", "Category", "Amount"])
        file.close()


def add_expense():
    print("\n--- Add Expense ---")

    date = input("Enter date: ")
    name = input("Enter expense name: ")
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount should be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    file = open(file_name, "a", newline="")
    writer = csv.writer(file)
    writer.writerow([date, name, category, amount])
    file.close()

    print("Expense added successfully.")


def view_expenses():
    print("\n--- All Expenses ---")

    file = open(file_name, "r")
    reader = csv.reader(file)

    rows = list(reader)
    file.close()

    if len(rows) <= 1:
        print("No expenses found.")
        return

    print("\nNo.  Date         Expense          Category       Amount")
    print("-" * 60)

    number = 1

    for row in rows[1:]:
        print(
            number,
            row[0],
            row[1],
            row[2],
            "Rs.", row[3]
        )
        number += 1


def total_expense():
    total = 0

    file = open(file_name, "r")
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        total = total + float(row[3])

    file.close()

    print("\n--- Total Expense ---")
    print("Total amount spent: Rs.", total)


def category_summary():
    categories = {}

    file = open(file_name, "r")
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        category = row[2]
        amount = float(row[3])

        if category in categories:
            categories[category] = categories[category] + amount
        else:
            categories[category] = amount

    file.close()

    if len(categories) == 0:
        print("\nNo expenses found.")
        return

    print("\n--- Category Summary ---")

    for category in categories:
        print(category, ":", "Rs.", categories[category])


def delete_expense():
    file = open(file_name, "r")
    reader = csv.reader(file)

    rows = list(reader)
    file.close()

    if len(rows) <= 1:
        print("\nNo expenses found.")
        return

    print("\n--- Delete Expense ---")

    for i in range(1, len(rows)):
        print(
            i,
            rows[i][0],
            rows[i][1],
            rows[i][2],
            "Rs.", rows[i][3]
        )

    try:
        number = int(input("Enter expense number to delete: "))

        if number < 1 or number >= len(rows):
            print("Invalid number.")
            return

        deleted = rows.pop(number)

        file = open(file_name, "w", newline="")
        writer = csv.writer(file)
        writer.writerows(rows)
        file.close()

        print("Deleted:", deleted[1])

    except ValueError:
        print("Please enter a valid number.")


def main():
    create_file()

    while True:
        print("\n==============================")
        print("     STUDENT EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            print("Thank you for using Student Expense Tracker.")
            break

        else:
            print("Please enter a valid choice.")


main()