import csv
def add_expense():

    date = input("Date likho: ")
    category = input("Category likho: ")
    amount = input("Amount likho: ")

    # file open karke data save karna
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense save ho gaya")
def view_expenses():

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row[0], row[1], row[2])

    except:
        print("Abhi koi data nahi hai")
def total_expense():

    total = 0

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                total = total + float(row[2])

        print("Total Expense:", total)

    except:
        print("Abhi koi data nahi hai")

def search_category():

    search = input("Category likho: ")
    found = False
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[1] == search:
                    print(row[0], row[1], row[2])
                    found = True

        if found == False:
            print("Kuch nahi mila")

    except:
        print("Abhi koi data nahi hai")

while True:

    print("\n1 Add Expense")
    print("2 View Expenses")
    print("3 Total Expense")
    print("4 Search Category")
    print("5 Exit")

    choice = input("Choice do: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        search_category()

    elif choice == "5":
        print("Thank you for using the app!")
        break

    else:
        print("Galat choice")