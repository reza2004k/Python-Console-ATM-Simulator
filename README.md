# 🏧 Python Console ATM System Simulator
\
This project is a simple, text-based ATM simulation developed in **Python 3**. It is designed to demonstrate core programming concepts, including loops, conditional logic, functions, and the use of the `datetime` module for tracking transactions.

## ✨ Features

* **Fixed Authentication:** Requires a hardcoded password (e.g., `5604` based on the code) for access. The card is blocked after **three failed attempts**.
* **Basic Transactions:** Supports the three core ATM services:
    * **Withdrawal:** Subtracts amount, validates funds, and checks for a minimum remaining balance.
    * **Deposit:** Adds funds to the account.
    * **Balance Inquiry:** Displays the current account balance.
* **Transaction Receipt:** Outputs a detailed summary of the transaction, including the **current date and time**.
* **Interactive Menu:** A loop runs the service menu until the user chooses to quit or retrieve their card.

## 🛠️ Technologies Used

* **Language:** Python 3
* **Libraries:** `datetime` (for date/time tracking)
* **Interface:** Console/Terminal

## 🚀 Getting Started

To run the ATM system on your local machine, follow these steps.

### Prerequisites

* Python 3 installed on your system.

### Installation and Running

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Python-Console-ATM-Simulator.git](https://github.com/YOUR_USERNAME/Python-Console-ATM-Simulator.git)
    cd Python-Console-ATM-Simulator
    ```
2.  **Run the application:**
    Execute the Python script from your terminal:
    ```bash
    python "ATM system.py"
    ```

### Usage Instructions

1.  The system will first prompt you to **enter your password**. (The default password is `5604`).
2.  If the password is correct, you will be shown the main menu:
    ```
    -----------Please choose your service--------------
              1.Withdraw         2.Deposit
              3.Get balance      4.Quit
    ```
3.  Enter the corresponding number for the service you require.
4.  After each transaction, you will be given the option to take your card or choose another service.

> **⚠️ Note:** This is a simulation. The balance is not permanently saved and resets every time the script is executed. The account starts with a fixed balance (e.g., $500).

---
