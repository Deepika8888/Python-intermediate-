#lets learn to create our custom exceptions 

class TooYoung(Exception):  #Creating own exception class
    pass

def apply_for_job(age):
    if age < 18:
        raise TooYoung("You are too young for this job.")
    return "Application successful!"


try:
    user_age = int(input("Enter your age: "))
    apply_for_job(user_age)
except TooYoung as e:
    print('You cant do the job', e)
else: 
    print("You can do this job.")