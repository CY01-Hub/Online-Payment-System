# 💸 **Online Payment System**

A lightweight and interactive **Python CLI Payment Application** that simulates the core functionality of modern digital wallets and UPI-style payment systems directly through the terminal.

The system allows users to register wallets, manage profiles, add funds, transfer money, and view transaction history — all while running entirely **in-memory**, without requiring an external database.

Designed with structured control flow, dictionary-based data management, input validation, and transaction tracking, this project provides a practical demonstration of Python programming fundamentals and real-world payment workflows.

---

## 🚀 *Cool Features Packed Inside :-*

* 👤 **Instant Registration**
  Create a new digital wallet using a name, phone number, and secure 4-digit transaction PIN. The system automatically prevents duplicate phone numbers from being registered.

* 🔐 **Profile Control Room**
  Update your display name or change your transaction PIN securely by first verifying your existing PIN.

* 💰 **Digital Wallet Top-Up**
  Add mock funds to your wallet instantly. The system validates the entered amount and accepts only positive values.

* 💸 **Secure Money Transfers**
  Transfer funds between registered users through a multi-step verification process:

  * Verifies that both accounts exist.
  * Prevents users from transferring money to themselves.
  * Requires the sender's 4-digit transaction PIN.
  * Checks whether the sender has sufficient funds.
  * Updates both wallet balances after a successful transaction.

* 🧾 **Centralized Transaction Ledger**
  Every successful transfer generates a unique transaction ID using Python's `uuid` module and records the exact transaction timestamp.

* 📜 **Transaction History**
  View a personalized transaction statement showing incoming and outgoing payments along with relevant transaction details.

* 🛡️ **Input Validation**
  Built-in validation ensures that phone numbers, PINs, and payment amounts follow the required format before any transaction is processed.

---

## 🚀 *How It Works :-*

```text
              Start Program
                   │
                   ▼
          Display Payment Menu
                   │
        ┌──────────┼───────────┐
        ▼          ▼           ▼
    Register    Top-Up      Transfer
      Wallet     Wallet       Money
        │          │           │
        └──────────┼───────────┘
                   │
                   ▼
           Profile Management
                   │
                   ▼
          Transaction History
                   │
                   ▼
             Continue / Exit
```

### Step-by-Step

1. The program initializes an empty in-memory wallet system.
2. The user selects an operation from the payment menu.
3. During registration, the system validates the phone number and creates a wallet with a 4-digit PIN.
4. Users can add mock funds to their wallet through the top-up feature.
5. Before transferring money, the system verifies both users and prevents self-transfers.
6. The sender must provide the correct transaction PIN.
7. The system checks whether the sender has sufficient wallet balance.
8. After a successful transfer, both wallet balances are updated.
9. A unique transaction ID and timestamp are generated for the transaction.
10. Users can access their transaction history to review previous payments.

---

## 🛠️ *The Tech Under the Hood :-*

| Category           | Technology / Concept                 |
| ------------------ | ------------------------------------ |
| 🐍 Language        | Python 3.10+                         |
| 💾 Data Storage    | In-Memory Dictionaries               |
| 🧠 Data Management | Dictionary-Based User Records        |
| 🔀 Control Flow    | `match-case`, Loops & Conditions     |
| 🛡️ Validation     | Input Validation & Error Handling    |
| 🔐 Security        | PIN Verification                     |
| 🆔 Transactions    | Python `uuid`                        |
| ⏱️ Timestamping    | Python `datetime`                    |
| 💸 Payment Logic   | Wallet Balance & Transfer Management |

---

## 🧠 *Data Architecture :-*

The application uses Python dictionaries to maintain user profiles and wallet information.

```text
users
  │
  ├── phone_number
  │       │
  │       └── user_metadata
  │              ├── name
  │              ├── PIN
  │              ├── balance
  │              └── transactions
  │
  └── phone_number
          │
          └── user_metadata
                 ├── name
                 ├── PIN
                 ├── balance
                 └── transactions
```

The phone number acts as the unique identifier for each wallet.

For example:

```text
users["9876543210"]
        │
        ├── name      → Dhrubo Das
        ├── PIN       → ****
        ├── balance   → ₹5000
        └── history   → Transaction Records
```

This structure keeps each user's profile information, wallet balance, and transaction records tightly associated without requiring a database.

---

## 🔐 *Transaction Flow :-*

A money transfer follows a controlled verification process:

```text
Select Transfer
      │
      ▼
Check Receiver
      │
      ▼
Prevent Self Transfer
      │
      ▼
Enter Transaction PIN
      │
      ▼
Verify PIN
      │
      ▼
Check Wallet Balance
      │
      ▼
Process Transfer
      │
      ▼
Generate Transaction ID
      │
      ▼
Record Timestamp
      │
      ▼
Update Transaction History
```

This ensures that a transfer is processed only after all required validation checks have passed.

---

## ▶️ *Running the Application :-*

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/online-payment-system.git
```

### 2. Navigate to the project

```bash
cd online-payment-system
```

### 3. Run the application

```bash
python payment.py
```

> Make sure **Python 3.10 or later** is installed on your system.

---

## 🎯 *Project Objective :-*

This project was created to practice Python programming concepts by building a realistic simulation of a digital payment and wallet system.

### Concepts Practiced

* Variables and data types
* Dictionaries
* Lists
* Functions
* Loops
* Conditional statements
* `match-case` statements
* User input
* Exception handling
* Input validation
* Dictionary-based data modeling
* PIN verification
* Financial transaction logic
* UUID generation
* Timestamp management
* Menu-driven CLI applications

---
<footer align="center">

**© 2026 Dhrubo Dey • CY01-Hub**

**Online Payment System** — Designed to simplify digital payments with a structured, reliable and user-friendly transaction experience.

`BUILD → UNDERSTAND → IMPROVE`

</footer>

