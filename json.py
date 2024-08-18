import json
import os

# File to store user data
USER_DATA_FILE = 'user_data.json'

# Function to save data to JSON file
def save_data(data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Function to load data from JSON file
def load_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to sign up a new user
def sign_up():
    data = load_data()
    username = input("Enter Username: ")
    
    if username in data:
        print("Username already exists. Please try another.")
        return
    
    password = input("Enter Password: ")
    mobile_number = input("Enter Mobile Number: ")
    
    # Save the new user data
    data[username] = {'password': password, 'mobile_number': mobile_number}
    save_data(data)
    
    print("Sign-up successful!")

# Function to sign in an existing user
def sign_in():
    data = load_data()
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    # Check if the username exists and the password matches
    if username in data and data[username]['password'] == password:
        print(f"Welcome to the device, {username}!")
        print(f"Your Mobile Number is: {data[username]['mobile_number']}")
    else:
        print("Incorrect credentials. Program terminated.")

# Main program loop
def main():
    while True:
        print("1. Sign Up")
        print("2. Sign In")
        choice = input("Select an option (1 or 2): ")
        
        if choice == '1':
            sign_up()
        elif choice == '2':
            sign_in()
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
