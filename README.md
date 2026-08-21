# 💸 Online Payment System
Welcome to my Online Payment System — a sleek, terminal-based clone of modern digital wallets and UPI payment gateways.
This is a pure Python project designed to simulate how a real digital wallet handles registration, profile management, wallet top-ups, and fund transfers. To keep things lightning-fast and simple, it runs entirely in-memory (no messy databases to configure) — which means all your data lives and breathes dynamically right in your terminal window while the script runs! ✨

---

# 🚀 Cool Features Packed Inside :-
- Instant Registration: Create a brand new wallet with your name, phone number, and a secure 4-digit secret PIN. (The system automatically blocks anyone trying to sign up with a phone number that’s already taken!)
- Profile Control Room: Need a change? Securely update your display name or switch up your transaction PIN whenever you want (just verify your current PIN first!).
- Digital Wallet Top-Up: Instantly inject mock cash into your wallet balance. Only positive numbers allowed here — no tricking the system!
- Secure Money Transfers: Move funds between users with a bulletproof verification flow:
Makes sure both accounts actually exist, Blocks you from awkwardly sending money to yourself, Demands your 4-digit PIN before touching a single rupee, Checks if you actually have enough money to cover the transfer.
- Centralized Ledger: Every single success story generates a completely unique transaction ID (powered by uuid) and locks in a precise timestamp.
- Transaction History: Pull up your clean statement to see exactly who sent you cash and where your funds went.

---

# 🛠️ The Tech Under the Hood :-
This project was built to flex strong programming fundamentals and strict error-handling habits:
- Language: Written in Python 3.10+ (making full use of clean match-case statements for the main menu).
- State Machine: Uses Python dictionaries to map phone_number -> user_metadata so user details and wallet balances stay tightly bound together.
- Validation Core: Built-in safeguards check that inputs are formatted perfectly (10-digit phone numbers, 4-digit PINs) before processing.
