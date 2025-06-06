#lets learn to use raise to trigger an error

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age 

try: 
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as e: 
    print(f"Error: {e}")
else: 
    print("Your age is valid.")