fruits = ['Apple','Mango','orange','Berry','melon']

cap_words = [word.capitalize() for word in fruits]
print(cap_words)
print("\n")
for index, fruit in enumerate(cap_words):
    print(f"Index [{index}] : Item- {fruit}")