import math

# Simple in-memory storage
users = {}
loans = {}

# EMI Calculation Function
def calculate_emi(principal, rate, time):
    monthly_rate = rate / (12 * 100)
    emi = (principal * monthly_rate * math.pow(1 + monthly_rate, time)) / \
          (math.pow(1 + monthly_rate, time) - 1)
    return round(emi, 2)

# Register User
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
   
    if username in users:
        print("User already exists!")
    else:
        users[username] = password
        print("Registration successful!")

# Login User
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
   
    if users.get(username) == password:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials!")
        return None

# Apply for Loan
def apply_loan(username):
    loan_type = input("Enter loan type (Personal/Home/Auto/Education): ")
    amount = float(input("Enter loan amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = int(input("Enter time (months): "))
   
    emi = calculate_emi(amount, rate, time)
   
    loans[username] = {
        "type": loan_type,
        "amount": amount,
        "rate": rate,
        "time": time,
        "emi": emi,
        "status": "Pending"
    }
   
    print(f"Loan applied successfully! EMI = {emi}")

# View Loan Details
def view_loan(username):
    if username in loans:
        loan = loans[username]
        print("\nLoan Details:")
        for key, value in loan.items():
            print(f"{key}: {value}")
    else:
        print("No loan found!")

# Approve Loan (Admin simulation)
def approve_loan(username):
    if username in loans:
        loans[username]["status"] = "Approved"
        print("Loan Approved!")
    else:
        print("No loan found!")

# Main Menu
def main():
    while True:
        print("\n--- Bank Loan Management System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
       
        choice = input("Enter choice: ")
       
        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user:
                while True:
                    print("\n1. Apply Loan")
                    print("2. View Loan")
                    print("3. Logout")
                   
                    user_choice = input("Enter choice: ")
                   
                    if user_choice == '1':
                        apply_loan(user)
                    elif user_choice == '2':
                        view_loan(user)
                    elif user_choice == '3':
                        break
                    else:
                        print("Invalid choice!")
        elif choice == '3':
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")

# Run the system
main()

