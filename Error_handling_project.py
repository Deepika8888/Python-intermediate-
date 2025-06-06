#lets create a simple ATM simulator 

class InsufficientFunds(Exception):
    pass

#lets setup and validate pin 

def pin(pin):
    if(len(pin)) != 4 or not pin.isdigit():
        raise ValueError('Pin must be a 4 digit number.')
    return pin

#lets setup withdraw function 

def withdraw(balance):
    global amount 
    if balance > amount: 
        raise InsufficientFunds("Insufficient balance.")
    amount -= balance
    return amount

amount = 5000 # starting amount

    
try: 
    user_pin = input('Enter your 4-digit pin: ')
    pin(user_pin) 
except ValueError as e: 
    print("The pin is rejected", e)
else: 
    print("Pin is accepted. You can move further.")
    
amount_withdrawn = int(input("Enter amount to withdraw: "))
try: 
    withdraw(amount_withdrawn) 
except InsufficientFunds as e: 
    print("Oops, not even fund", e) 
else: 
    print("Your transaction is successful.")
    
    
