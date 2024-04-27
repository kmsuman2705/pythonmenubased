import os

print("Welcome to my part")
print()
print("Press 1: to see the calendar")
print("Press 2: to run Chrome")
print("Press 3: to open the notebook")

ch = input("Enter your choice: ")
print("You entered:", ch)

if ch == "1":
    print("calender")
    # Code to see the calendar
elif ch == "2":
    print("chrome")
    # Code to open Chrome
    # Replace os.system("chrome") with the appropriate command to run Chrome based on your OS
elif ch == "3":
    print("Opening notebook...")
    # Code to open the notebook
else:
    print("Invalid choice. Please choose a valid option (1, 2, or 3).")