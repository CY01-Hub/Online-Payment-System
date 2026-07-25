'''
Online Payment System :-
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
print("WELCOME! to Dhrubo's Online Payment System :- ")

user = {}      # Global dictionary to store all registered users (phone -> user details)
transactions = []      # Global list to store all transactions

# Function to register a new user
def register_user():
      print()
      name = input("Enter your Name : ")

      phone = input("Enter your Phone Number (10 Digit) : ")
      if phone in user:
            print("User with the same Phone Number already exists.")
            return

      if len(phone) != 10 or not phone.isdigit():
            print("Invalid! Phone Number.")
            return
      
      pin = input("Enter your unique PIN (4 Digit-PIN) : ")
      if len(pin) != 4 or not pin.isdigit():
            print("Invalid! PIN.")
            return
      
      user[phone] = {
            "Name" : name,
            "Number" : phone,
            "PIN" : pin,
            "Balance" : 0
      }

      print("Registration successful!")
      print("------------------------------------------------")

def update_profile():
      print()
      phone = input("Enter your Phone Number (10 Digit) : ")
      if phone not in user:
            print("User with the given Phone Number does not exist.")
            return

      if len(phone) != 10 or not phone.isdigit():
            print("Invalid! Phone Number.")
            return
      
      pin = input("Enter your Current PIN : ")
      if len(pin) != 4 or not pin.isdigit():
            print("Invalid! PIN.")
            return
      
      if user[phone]["PIN"] == pin:
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
                              if len(new_pin) != 4 or not new_pin.isdigit():
                                    print("Invalid! PIN.")
                              else:
                                    user[phone]["PIN"] = new_pin
                                    print("PIN updated successfully!")

                        # Option 3: Exit the update menu
                        elif choice == 3:
                              print("Exiting...")
                              break

                        else:
                              print("Invalid Choice!")
      else:
            print("Wrong PIN!")
            return

def add_balance():
      print()
      phone = input("Enter your Phone Number (10 Digit) : ")
      if phone not in user:
            print("User with the given Phone Number does not exist.")
            return
            
      if len(phone) != 10 or not phone.isdigit():
            print("Invalid! Phone Number.")
            return
      
      pin = input("Enter your PIN : ")
      if user[phone]["PIN"] != pin:
            print("Wrong PIN!")
            return
      
      amount = int(input("Enter amount to add : "))
      if amount <= 0:
            print("Amount must be positive!")
            return
      
      user[phone]["Balance"] += amount
      print(f"Rs.{amount} added successfully!")
      print("------------------------------------------------")
        
def transfer_money():
      print()
      sender_phone = input("Enter Sender's Phone Number (10 Digit) : ")
      if len(sender_phone) != 10 or not sender_phone.isdigit():
            print("Invalid! Phone Number.")
            return

      if sender_phone not in user:
            print("User with the given Phone Number does not exist.")
            return
      
      receiver_phone = input("Enter Receiver's Phone Number (10 Digit) : ")
      if len(receiver_phone) != 10 or not receiver_phone.isdigit():
            print("Invalid! Phone Number.")
            return

      if receiver_phone not in user:
            print("Receiver with the given Phone Number does not exist.")
            return
      
      if sender_phone == receiver_phone:
            print("You cannot transfer money to yourself.")
            return
      
      pin = input("Enter your Current PIN : ")
      if len(pin) != 4 or not pin.isdigit():
            print("Invalid! PIN.")
            return
      
      if user[sender_phone]["PIN"] != pin:
            print("Wrong PIN!")
            return
      
      amount = int(input("Enter the Amount to be transferred : "))      # Get amount to transfer
      if user[sender_phone]["Balance"] < amount:
            print("Insufficient balance!")
            return
      
      user[sender_phone]["Balance"] -= amount      # Deduct amount from sender's account
      user[receiver_phone]["Balance"] += amount      # Add amount to receiver's account
      transaction_id = str(uuid.uuid4())      # Generate unique transaction ID using UUID

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

def check_balance():
      print()
      phone = input("Enter your Phone Number (10 Digit) : ")
      if phone not in user:
            print("User with the given Phone Number does not exist.")
            return
      if len(phone) != 10 or not phone.isdigit():
            print("Invalid! Phone Number.")
            return
      
      pin = input("Enter your Current PIN : ")
      if len(pin) != 4 or not pin.isdigit():
            print("Invalid! PIN.")
            return
      
      if user[phone]["PIN"] == pin:
            print(f"Your Current Balance: Rs.{user[phone]['Balance']}")
            print("------------------------------------------------")
      else:
            print("Wrong PIN!")
      
def transaction_history():
      print()
      phone = input("Enter your Phone Number (10 Digit) : ")
      if phone not in user:
            print("User with the given Phone Number does not exist.")
            return
      if len(phone) != 10 or not phone.isdigit():
            print("Invalid! Phone Number.")
            return
      
      pin = input("Enter your Current PIN : ")
      if len(pin) != 4 or not pin.isdigit():
            print("Invalid! PIN.")
            return
      
      if user[phone]["PIN"] == pin:
            print(f"\nTransaction History for {user[phone]['Name']}:")
            for transaction in transactions:
                  if transaction["Sender Phone Number"] == phone or transaction["Receiver Phone Number"] == phone:
                        print(f"\nTransaction ID: {transaction['Id']}")
                        print(f"Sender: {transaction['Sender Name']} ({transaction['Sender Phone Number']})")
                        print(f"Receiver: {transaction['Receiver Name']} ({transaction['Receiver Phone Number']})")
                        print(f"Amount: Rs.{transaction['Amount Transferred']}")
                        print(f"Status: {transaction['Status']}")
                        print(f"Timestamp: {transaction['Timestamp']}")
      else:
            print("Wrong PIN!")
      
      print("------------------------------------------------")

while True:
      print("\nMENU :-"
            "\n1. Register User"
            "\n2. Update Profile"
            "\n3. Add Balance"
            "\n4. Transfer Money"
            "\n5. Check Balance"
            "\n6. Transaction History"
            "\n7. Exit...")
      
      choice = int(input("Enter your choice : "))
      match(choice):
            case 1 : 
                  register_user()      # Call function to register new user
            case 2 : 
                  update_profile()      # Call function to update user profile
            case 3 :
                  add_balance()      # Call function to add balance to wallet
            case 4 : 
                  transfer_money()      # Call function to transfer money
            case 5 : 
                  check_balance()      # Call function to check balance
            case 6 : 
                  transaction_history()      # Call function to view transaction history
            case 7 : 
                  print("Thanks for using Dhrubo's Online Payment System.")
                  rate = int(input("Make sure to rate your experience between 0 and 10 : "))
                  if 10 >= rate >= 8:
                        print("Thank you for the great feedback!")
                        break
                  elif 7 >= rate >= 0:
                        print("We appreciate your feedback. We'll work to improve!")
                        break
                  else:
                        print("Invalid rating!")
                        break
            case _ : 
                  print("Invalid Input!")
                  
