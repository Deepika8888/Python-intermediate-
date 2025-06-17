#lets import our own module and use it 

import Mymath


print("Enter any two numbers: ")
input2 = int(input("a: "))
input3 = int(input("b: "))



print(Mymath.add(input2, input3))
print(Mymath.subtract(input2, input3))
print(Mymath.multiply(input2, input3))
print(Mymath.divide(input2, input3))

