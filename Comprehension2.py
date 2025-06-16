#lets learn about dictionary comprehension

#squares in dictionary form

squares_dict = [x* x for x in range(1,10)]
print("Squares Dictionary:", squares_dict)

# dictionary of word lengths 

words = ["Apple", "Banana", "Cherry"]
word_lengths = {word: len(word) for word in words}
print("Word Lengths:", word_lengths)