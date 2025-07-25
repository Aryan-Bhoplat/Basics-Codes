'''sentence = input("Type your sentence:")
count = 0
sentence = sentence.replace(" ", "")
for i in sentence:
    count+=1
    
print(count)'''

#Or

sentence = input("Type your sentence:")
count = len(sentence.replace(" ", ""))
print(count)