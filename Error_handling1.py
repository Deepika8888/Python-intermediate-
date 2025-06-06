#lets learn about advanced error handling 

#we are going to learn about try, except, else, finally

try:  #Block that might cause an error
    num = int(input("Enter a number: "))
except ValueError:  #What to do if error occurs
    print("are you dumb man?")
else:        #Runs if no error occurs
    print("You entered:", num)
finally:  #Always runs (used to clean up things like closing files)
    print("Wow, you are good.")
