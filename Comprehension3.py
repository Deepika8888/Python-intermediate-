#lets learn about set comprehension 

#unique length of words 

word_set = ['hi', 'hello', 'world', 'hi', 'python']
unique_lengths = {len(word) for word in word_set}
print("Unique Lengths:", unique_lengths)