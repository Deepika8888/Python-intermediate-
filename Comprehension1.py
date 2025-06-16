#lets learn about list comprehension 

squares = [x*x for x in range(1,8)]
print('Squares:', squares)

evens = [x for x in range (10) if x%2==0]
print('Evens:', evens)

#length of each word
words = ["hello", "world"]
lengths = [len(word) for word in words]
print('Lengths:', lengths)
