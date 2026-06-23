# banking-system

# 📌 Project Description

The **Billionaire Bank Management System** is a console-based application that demonstrates how OOP concepts can be used to build a banking application.

Users can:

* Create a bank account
* Deposit money
* Withdraw money
* Select a payment method (Cash, UPI, or Other)
* View updated account balance

This project is intended for beginners learning Python OOP and inheritance.

---

# ✨ Features

* 🏦 Bank account creation
* 💰 Deposit money
* 💸 Withdraw money
* 💳 Multiple payment methods

  * Cash
  * UPI
  * Other
* 💲 Displays transaction charges
* 👤 Displays account information
* 🖥 Console-based interface

---



# 📚 OOP Concepts Used

* Classes
* Objects
* Constructors (`__init__`)
* Inheritance
* Method Overriding
* Instance Variables
* Class Variables
* String Representation (`__str__`)

---


# ⚙ Classes

## 1. Bank

Base class containing:

* Bank Name
* Customer Name
* Account Balance

Methods:

* `__init__()`
* `__str__()`

---

## 2. pay_mode

Handles payment method selection.

Supported methods:

* Cash
* UPI
* Other

Displays transaction charges according to the selected payment mode.

---

## 3. deposit

Inherits from `pay_mode`.

Functions:

* Accepts deposit amount
* Updates account balance
* Displays successful deposit message

---

## 4. withdraw

Inherits from `pay_mode`.

Functions:

* Accepts withdrawal amount
* Checks sufficient balance
* Deducts amount
* Displays remaining balance

---



# 💻 Sample Output

```text
Billionaire bank

enter type(cash,upi,other): upi
no charges
payment successfully deposited

Name: meer, Balance: 90200

enter withdraw type(cash,upi,other): cash
0.1% charges
withdraw successful
balance remaining 85200
```

---

# 🚀 Future Improvements

* Account number generation
* PIN authentication
* Transaction history
* Balance enquiry menu
* Money transfer between accounts
* Interest calculation
* File handling for permanent data storage
* Database integration (SQLite/MySQL)
* Graphical User Interface (Tkinter)

---

# 🎯 Learning Outcomes

This project helped in understanding:

* Object-Oriented Programming in Python
* Class inheritance
* Constructors
* Method overriding
* User input handling
* Basic banking operations

---



# 📄 License

This project is created for educational purposes and is free to use and modify.

⭐ If you like this project, consider giving the repository a star on GitHub!
