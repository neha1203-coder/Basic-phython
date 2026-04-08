sentence = input("enter the sentence: ")
 
words = sentence.split()
word_lenght = {}

for word in words:
    word_lenght[word] = len(word)

print(word_lenght)    
