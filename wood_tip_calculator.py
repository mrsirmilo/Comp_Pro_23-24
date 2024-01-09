# Derek Wood
# 2B
# Janurary 9, 2024

# This program will ask for the users initial bill, then the ammount they'd like to tip in increments or an other option where the user can input a custom tip ammount. After inputting both values the program will calculate the bill with the applied tip then spits out the total bill.

init_bill = float(input("What is your bill ammount? "))
tip_selection = int(input("Select the tip you'd like to leave. (0, 5, 10, 18, 20, 22, 25) "))

def inital_bill():
    print(f"The initial bill ammount is: ${init_bill}")

def tip_selected():
    if tip_selection in [5, 10, 18, 20, 22, 25]:
        tip_percentage = tip_selection / 100
        total_bill = round(init_bill * tip_percentage, 2)
        print(f"The tip you selected was: {tip_selection}% ")
        print(f"The total bill is: ${total_bill}")

    elif tip_selection == 0:
        print(f"The tip you selected was: {tip_selection}% ")
        print(f"The total bill is: ${init_bill}")

    else:
        print(f"You need to make a selection from the list.")

inital_bill()
tip_selected()