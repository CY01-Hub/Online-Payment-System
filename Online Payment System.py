'''
4. Online Payment System
Build an object-oriented UPI-style payment simulation in Python without a database, 
meaning all data exists only while the program runs. Design it properly using separate classes: 
User (name, phone, PIN, wallet), Wallet (balance with credit/debit methods), 
Transaction (ID, sender, receiver, amount, status, timestamp), and 
PaymentSystem (handles registration, login, sending money, balance check, and transaction history). 
Store users in a dictionary mapping phone numbers to user objects, not raw balances. 
When transferring money, follow a strict flow: validate users, prevent self-transfer, verify PIN, 
check sufficient balance, perform debit and credit safely, generate a unique transaction ID, and 
log the transaction centrally inside the system. Even without a database, 
enforce duplicate phone prevention, basic PIN validation, 
and clean error handling to keep the design strong enough for a second-year level project.
'''

# Import required libraries for unique IDs and timestamps
import uuid
from datetime import datetime

# Display welcome message to the user
print()
print("WELCOME! to Dhrubo's Online Payment System :- ")

# Global dictionary to store all registered users (phone -> user details)
user = {}
# Global list to store all transactions
transactions = []

# Function to register a new user
def register_user():
      print()
      # Get user's full name
      name = input("Enter your Name : ")

      # Get and validate phone number (must be 10 digits)
      phone = input("Enter your Phone Number (10 Digit) : ")
      # Check if phone number already exists in the system
      if phone in user:
            print("User with the same Phone Number already exists.")
            return
      # Validate phone number format
      if len(phone) != 10 or not phone.isdigit():
            print("Invalid! Phone Number.")
            return
      
      # Get and validate PIN (must be 4 digits)
      pin = input("Enter your unique PIN (4 Digit-PIN) : ")
      if len(pin) != 4 or not pin.isdigit():
            print("Invalid! PIN.")
            return
      
      # Create new user account with initial balance of 0
      user[phone] = {
            "Name" : name,
            "Number" : phone,
            "PIN" : pin,
            "Balance" : 0
      }

      print("Registration successful!")
      print("------------------------------------------------")

# Function to update user's profile (name or PIN)
def update_profile():
      print()
      # Get phone number to identify user
      phone = input("Enter your Phone Number (10 Digit) : ")
      # Check if user exists
      if phone not in user:
            print("User with the given Phone Number does not exist.")
            return
      # Validate phone number format
      if len(phone) != 10 or not phone.isdigit():
            print("Invalid! Phone Number.")
            return
      
      # Get and validate current PIN for security verification
      pin = input("Enter your Current PIN : ")
      if len(pin) != 4 or not pin.isdigit():
            print("Invalid! PIN.")
            return
      
      # Check if provided PIN matches the stored PIN
      if user[phone]["PIN"] == pin:
            # If user exists, show update options
            if phone in user:
                  while True:
                        print("Menu :- "
                              "\n1. Change Name"
                              "\n2. Change PIN"
                              "\n3. Exit...")
                        
                        choice = int(input("Enter your Choice : "))
                        # Option 1: Update user's name
                        if choice == 1:
                              name = input("Enter the New Name : ")
                              user[phone]["Name"] = name
                              print("Name updated successfully!")

                        # Option 2: Update user's PIN
                        elif choice == 2:
                              new_pin = input("Enter the New PIN (4 Digit) : ")
                              # Validate new PIN format
                              if len(new_pin) != 4 or not new_pin.isdigit():
                                    print("Invalid! PIN.")
                              else:
                                    user[phone]["PIN"] = new_pin
                                    print("PIN updated successfully!")

                        # Option 3: Exit the update menu
                        elif choice == 3:
                              print("Exiting...")
                              break

                        # Handle invalid menu choice
                        else:
                              print("Invalid Choice!")
      else:
            # If PIN doesn't match, deny access
            print("Wrong PIN!")
            return

# Function to add money to user's wallet
def add_balance():
      print()
      # Get phone number to identify user
      phone = input("Enter your Phone Number (10 Digit) : ")
      # Check if user exists
      if phone not in user:
            print("User with the given Phone Number does not exist.")
            return
      # Validate phone number format
      if len(phone) != 10 or not phone.isdigit():
            print("Invalid! Phone Number.")
            return
      
      # Get and verify PIN for security
      pin = input("Enter your PIN : ")
      if user[phone]["PIN"] != pin:
            print("Wrong PIN!")
            return
      
      # Get amount to add to wallet
      amount = int(input("Enter amount to add : "))
      # Validate that amount is positive
      if amount <= 0:
            print("Amount must be positive!")
            return
      
      # Add amount to user's balance
      user[phone]["Balance"] += amount
      print(f"Rs.{amount} added successfully!")
      print("------------------------------------------------")
        
# Function to transfer money from one user to another
def transfer_money():
      print()
      # Get and validate sender's phone number
      sender_phone = input("Enter Sender's Phone Number (10 Digit) : ")
      if len(sender_phone) != 10 or not sender_phone.isdigit():
            print("Invalid! Phone Number.")
            return
      # Check if sender exists
      if sender_phone not in user:
            print("User with the given Phone Number does not exist.")
            return
      
      # Get and validate receiver's phone number
      receiver_phone = input("Enter Receiver's Phone Number (10 Digit) : ")
      if len(receiver_phone) != 10 or not receiver_phone.isdigit():
            print("Invalid! Phone Number.")
            return
      # Check if receiver exists
      if receiver_phone not in user:
            print("Receiver with the given Phone Number does not exist.")
            return
      
      # Prevent user from sending money to themselves
      if sender_phone == receiver_phone:
            print("You cannot transfer money to yourself.")
            return
      
      # Get and validate sender's PIN
      pin = input("Enter your Current PIN : ")
      if len(pin) != 4 or not pin.isdigit():
            print("Invalid! PIN.")
            return
      
      # Verify PIN matches with stored PIN
      if user[sender_phone]["PIN"] != pin:
            print("Wrong PIN!")
            return
      
      # Get amount to transfer
      amount = int(input("Enter the Amount to be transferred : "))
      
      # Check if sender has sufficient balance
      if user[sender_phone]["Balance"] < amount:
            print("Insufficient balance!")
            return
      
      # Deduct amount from sender's account
      user[sender_phone]["Balance"] -= amount
      # Add amount to receiver's account
      user[receiver_phone]["Balance"] += amount

      # Generate unique transaction ID using UUID
      transaction_id = str(uuid.uuid4())
      # Log the transaction with all details
      transactions.append({
            "Id" : transaction_id,
            "Sender Name" : user[sender_phone]["Name"],
            "Sender Phone Number" : sender_phone,
            "Receiver Name" : user[receiver_phone]["Name"],
            "Receiver Phone Number" : receiver_phone,
            "Amount Transferred" : amount,
            "Status" : "Success",
            "Timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      })

      print("Money transferred successfully!")
      print("Transaction Id :", transaction_id)
      print("------------------------------------------------")

# Function to display user's current balance
def check_balance():
      print()
      # Get phone number to identify user
      phone = input("Enter your Phone Number (10 Digit) : ")
      # Check if user exists
      if phone not in user:
            print("User with the given Phone Number does not exist.")
            return
      # Validate phone number format
      if len(phone) != 10 or not phone.isdigit():
            print("Invalid! Phone Number.")
            return
      
      # Get and validate PIN for security
      pin = input("Enter your Current PIN : ")
      if len(pin) != 4 or not pin.isdigit():
            print("Invalid! PIN.")
            return
      
      # Display balance if PIN is correct
      if user[phone]["PIN"] == pin:
            print(f"Your Current Balance: Rs.{user[phone]['Balance']}")
            print("------------------------------------------------")
      else:
            # Deny access if PIN is incorrect
            print("Wrong PIN!")
      
# Function to display transaction history of a user
def transaction_history():
      print()
      # Get phone number to identify user
      phone = input("Enter your Phone Number (10 Digit) : ")
      # Check if user exists
      if phone not in user:
            print("User with the given Phone Number does not exist.")
            return
      # Validate phone number format
      if len(phone) != 10 or not phone.isdigit():
            print("Invalid! Phone Number.")
            return
      
      # Get and validate PIN for security
      pin = input("Enter your Current PIN : ")
      if len(pin) != 4 or not pin.isdigit():
            print("Invalid! PIN.")
            return
      
      # Display transactions if PIN is correct
      if user[phone]["PIN"] == pin:
            print(f"\nTransaction History for {user[phone]['Name']}:")
            # Loop through all transactions
            for transaction in transactions:
                  # Check if user was involved as sender or receiver
                  if transaction["Sender Phone Number"] == phone or transaction["Receiver Phone Number"] == phone:
                        print(f"\nTransaction ID: {transaction['Id']}")
                        print(f"Sender: {transaction['Sender Name']} ({transaction['Sender Phone Number']})")
                        print(f"Receiver: {transaction['Receiver Name']} ({transaction['Receiver Phone Number']})")
                        print(f"Amount: Rs.{transaction['Amount Transferred']}")
                        print(f"Status: {transaction['Status']}")
                        print(f"Timestamp: {transaction['Timestamp']}")
      else:
            # Deny access if PIN is incorrect
            print("Wrong PIN!")
      
      print("------------------------------------------------")

# Main menu loop - continues until user exits
while True:
      # Display main menu options
      print("\nMENU :-"
            "\n1. Register User"
            "\n2. Update Profile"
            "\n3. Add Balance"
            "\n4. Transfer Money"
            "\n5. Check Balance"
            "\n6. Transaction History"
            "\n7. Exit...")
      
      # Get user's choice
      choice = int(input("Enter your choice : "))
      
      # Handle user's choice using match-case statement
      match(choice):
            case 1 : 
                  # Call function to register new user
                  register_user()
            case 2 : 
                  # Call function to update user profile
                  update_profile()
            case 3 :
                  # Call function to add balance to wallet
                  add_balance()
            case 4 : 
                  # Call function to transfer money
                  transfer_money()
            case 5 : 
                  # Call function to check balance
                  check_balance()
            case 6 : 
                  # Call function to view transaction history
                  transaction_history()
            case 7 : 
                  # Exit the program with rating feedback
                  print("Thanks for using Dhrubo's Online Payment System.")
                  rate = int(input("Make sure to rate your experience between 0 and 10 : "))
                  # Show appropriate message based on rating
                  if 10 >= rate >= 8:
                        print("Thank you for the great feedback!")
                        break  # Exit program
                  elif 7 >= rate >= 0:
                        print("We appreciate your feedback. We'll work to improve!")
                        break  # Exit program
                  else:
                        # Invalid rating
                        print("Invalid rating!")
                        break  # Exit program
            case _ : 
                  # Handle invalid menu choice
                  print("Invalid Input!")