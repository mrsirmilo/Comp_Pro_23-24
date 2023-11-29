# Derek Wood
# 2B
# November 28, 2023

# The code will print John because the variable "name" is set to John, and we coded it to print(name).
name = ("John")
print(name)

# The code will print the variable "gpt_response" after printing the variable "name" because it comes before it in the code
gpt_response = ("The flamingo danced the salsa with a top hat on its beak!")
print(gpt_response)

# The code sets four names to four different variables, we used "name#" so the name isnt replaced by the name on line 17
name1 = "Axl"
name2 = "Slash"
name3 = "Duff"
name4 = "Izzy"
print(f"{name1} and {name2} and {name3} and {name4}")

# This code is going to ask for a user input, input(), the prompt for this input is "Hi! What is your name?" After a user inputs a resposne to the prompt the code is going to assign it to the user_name variable. After the user completes the input and the input is assigned to the user_name variable the code is going to print "Hello (user_name)! Where (user_name) would be replaced with what the user inputed at the begining of the program."
user_name = input("Hi! What is your name? ")
print("Hello " + user_name + "!")
food = input("What is your favorite food?")
print(f"Awesome! I really like {food} too!")
print("We want to know if you like programming!")
print("Do you like programming " + user_name + "?"); answer = input()
print("Great! You said " + answer + "!")

def ask_for_name():
    cb_name = input("Welcome! What is your full name?")
    print(f"Hello {cb_name}, welcome to (company name). I'm going to collect some contact information before we start.")
    return cb_name

def ask_for_phone():
    phone_number = input("What is a good phone number that a customer support agent could contact you at?")

    confirm = input(f"Is {phone_number} the correct phone number? (Yes/No): ")
    if confirm.lower() == 'yes':
        return phone_number
    elif confirm.lower() == 'no':
        print("Let's try again.")
    else:
        print("Please enter 'Yes' or 'No'.")

def ask_for_email():
    email = input("Please enter your email address: ")
    return email

# Usage
cb_name = ask_for_name()
print(f"Your full name is: {cb_name}")

phone = ask_for_phone()
print(f"Great, your phone number is: {phone}")

email = ask_for_email()
print(f"Your email is: {email}")

print(f"Wonderful! Here is your information:\n")
print(f"Full name: {cb_name}")
print(f"Phone number: {phone}")
print(f"Email: {email}")