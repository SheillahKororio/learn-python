from abc import ABC, abstractmethod
# Imports ABC for creating abstract classes and abstractmethod for defining methods that child classes must implement.


# ==================================
# 1. ABSTRACTION
# ==================================

class MpesaPayment(ABC):
    # Creates an abstract class called MpesaPayment that inherits from ABC.

    @abstractmethod
    # Declares that the method below must be implemented by a concrete child class.
    def make_payment(self, amount):
        # Defines a method that accepts an amount to be paid.
        pass
        # pass means the method has no implementation here; it will be implemented in a child class.


# ==================================
# 2. CLASS AND ENCAPSULATION
# ==================================

class MpesaAccount(MpesaPayment):
    # Creates MpesaAccount, which inherits the abstract payment structure from MpesaPayment.

    def __init__(self, name, phone, balance):
        # Constructor that automatically runs when a new MpesaAccount object is created.
        self.name = name
        # Stores the customer's name in the object.
        self.phone = phone
        # Stores the customer's phone number in the object.

        self.__balance = balance
        # Stores the account balance using double underscores to trigger name mangling and restrict direct access.

    def check_balance(self):
        # Defines a method for checking the customer's account balance.
        return self.__balance
        # Returns the current balance to the caller.

    def deposit(self, amount):
        # Defines a method that allows money to be deposited into the account.

        if amount > 0:
            # Checks whether the amount being deposited is greater than zero.
            self.__balance += amount
            # Adds the deposited amount to the existing account balance.
            print("Deposit successful!")
            # Displays a success message after depositing money.

        else:
            # Executes when the deposit amount is zero or negative.
            print("Invalid deposit amount!")
            # Displays an error message for an invalid deposit.

    def withdraw(self, amount):
        # Defines a method that allows the customer to withdraw money.

        if amount <= 0:
            # Checks whether the withdrawal amount is zero or negative.
            print("Invalid amount!")
            # Displays an error message if the amount is invalid.

        elif amount <= self.__balance:
            # Checks whether the customer has enough money to make the withdrawal.
            self.__balance -= amount
            # Subtracts the withdrawal amount from the current balance.
            print("Withdrawal successful!")
            # Displays a success message after withdrawing money.

        else:
            # Executes when the requested withdrawal exceeds the available balance.
            print("Insufficient balance!")
            # Displays a message informing the customer that the balance is insufficient.

    def send_money(self, receiver, amount):
        # Defines a method for sending money from the current account to another account.
        # receiver represents the recipient object, while amount represents the money being sent.

        if amount <= 0:
            # Checks whether the amount being sent is zero or negative.
            print("Invalid amount!")
            # Displays an error message if the amount is invalid.

        elif amount > self.__balance:
            # Checks whether the sender has enough money to complete the transfer.
            print("Insufficient balance!")
            # Displays an error message if the sender has insufficient funds.

        else:
            # Executes when the transfer amount is valid and the sender has enough money.
            self.__balance -= amount
            # Deducts the transferred amount from the sender's account.
            receiver.deposit(amount)
            # Calls the receiver's deposit method to add the money to their account.

            print(f"Ksh {amount} sent to {receiver.name}")
            # Displays the amount sent and the recipient's name using an f-string.

    def make_payment(self, amount):
        # Implements the abstract make_payment method inherited from MpesaPayment.
        self.withdraw(amount)
        # Uses the withdraw method to deduct the payment amount from the account.


# ==================================
# 3. INHERITANCE
# ==================================

class CustomerAccount(MpesaAccount):
    # Creates CustomerAccount as a child class of MpesaAccount.
    # It inherits the parent's methods and attributes.

    def account_type(self):
        # Defines a method that identifies the type of customer account.
        print("Personal M-PESA Account")
        # Displays that this is a personal M-PESA account.


class BusinessAccount(MpesaAccount):
    # Creates BusinessAccount as another child class of MpesaAccount.
    # It also inherits the parent's methods and attributes.

    def account_type(self):
        # Defines a method that identifies the type of business account.
        print("Business M-PESA Account")
        # Displays that this is a business M-PESA account.


# ==================================
# 4. CREATING OBJECTS
# ==================================

sheila = CustomerAccount("Sheila", "0712345678", 5000)
# Creates an Eric object with his name, phone number and an initial balance of Ksh 5,000.

kororio = CustomerAccount("Kororio", "0723456789", 3000)
# Creates a Kororio object with his name, phone number and an initial balance of Ksh 3,000.

shop = BusinessAccount("Sheila Shop", "0734567890", 10000)
# Creates a business account object with its name, phone number and an initial balance of Ksh 10,000.


# ==================================
# 5. POLYMORPHISM
# ==================================

kororio.account_type()
# Calls account_type() for Eric, displaying Personal M-PESA Account.

shop.account_type()
# Calls the same method name for the shop, but displays Business M-PESA Account.


# ==================================
# 6. INTERACTING WITH THE SYSTEM
# ==================================

print("\n--- M-PESA SYSTEM ---")
# Displays the M-PESA SYSTEM heading; \n creates a new line before the heading.

print("Customer:", sheila.name)
# Displays Eric's name by accessing the name attribute of his object.

print("Phone:", sheila.phone)
# Displays Eric's phone number by accessing his phone attribute.

print("Balance:", sheila.check_balance())
# Calls check_balance() to retrieve and display Sheila's current account balance.


# Deposit money
print("\n--- DEPOSIT ---")
# Displays the DEPOSIT heading on a new line.

sheila.deposit(2000)
# Deposits Ksh 2,000 into Sheila's account, increasing his balance from 5,000 to 7,000.


# Withdraw money
print("\n--- WITHDRAW ---")
# Displays the WITHDRAW heading on a new line.

sheila.withdraw(1000)
# Withdraws Ksh 1,000 from Sheila's account, reducing his balance from 7,000 to 6,000.


# Send money to another customer
print("\n--- SEND MONEY ---")
# Displays the SEND MONEY heading on a new line.

sheila.send_money(kororio, 1500)
# Sends Ksh 1,500 from Sheila's account to John's account.
# Sheila's balance becomes 4,500 while Kororio's balance becomes 4,500.


# Make a payment using abstraction
print("\n--- PAYMENT ---")
# Displays the PAYMENT heading on a new line.

sheila.make_payment(500)
# Calls the implemented make_payment() method, which withdraws Ksh 500 from Sheila's account.
# Sheila's balance becomes 4,000.


# Display final balances
print("\n--- FINAL BALANCES ---")
# Displays the FINAL BALANCES heading on a new line.

print("Sheila:", sheila.check_balance())
# Displays sheila's final balance of Ksh 4,000.

print("Kororio:", kororio.check_balance())
# Displays kororio's final balance of Ksh 4,500.

print("Shop:", shop.check_balance())
# Displays the shop's final balance of Ksh 10,000.