#Didn't understand

def sentence(s1):
    largest = s1[0]
    for word in s1:
        if len(word) > len(largest):
            largest = word


    return largest

s1 = input("Enter sentence:").split()
result = sentence(s1)
print(result)

'''
def most_frequent_word(sentence):
    words = sentence.split()         # Step 1: Split into words
    freq = {}                        # Step 2: Empty dictionary to store frequency

    for word in words:              # Count each word
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    max_word = None
    max_count = 0

    for word, count in freq.items():   # Step 3: Find word with max count
        if count > max_count:
            max_word = word
            max_count = count

    return max_word                   # Step 4: Return result

'''