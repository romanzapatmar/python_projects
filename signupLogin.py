# Project Name : Signup and Login in Python
# Author : Roman Zapatmar
# Date : 24 June 2025

# Create a simple signup and login system in Python

users = {} #it will save a dictionary of users ie. username:password

#signup
def signup():
    username = input("Enter your username: ")
    if username in users:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Enter your password: ")
    users[username] = password
    print("Signup successful!")

#login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

def show_users():
    for i, username in enumerate(users, start=1):
        print(f"{i}. {username} \n")
    
#menu
def menu():
    while True:
        print("1. Signup")
        print("2. Login")
        print("3. Show users")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        print()

        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            show_users()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
