 # Christopher Smith
 # 16JUNE2025
 # P1HW1
 # This assignment is a program that does some basic math on numbers entered.
print("This program calculates and displays travel expenses")
print()
# enter the amount of budget you have to spend
budget = int(input("Enter budget: "))
print()
# enter where you are going
destination = input("Enter your travel destination: ")
print()
# enter how much gas it will take
gasmoney = int(input("How much do you think you will spend on gas? "))
print()
# enter how much it might cost for housing
accom = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
#enter how much you will spend on food
food = int(input("Last, how much do you need for food? "))
expenses = (gasmoney + accom + food)
#depending on your inputs you will get a breakdown of how much money you will spend in total and how much is left after
print()
print('-------------Travel Expenses------------')
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gasmoney)
print("Accomodation:", accom)
print("Food:", food)
print()
print("Remaining Balance:", budget - expenses)


