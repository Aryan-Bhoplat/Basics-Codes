'''
dict1 = {
    'Aryan':95,
    'Yash':100,
    'Om': 87,
    'Rushi': 90
}

z = list(dict1.items())
print(z)
'''

#Or

dict1 = {
    'Aryan':95,
    'Yash':100,
    'Om': 87,
    'Rushi': 90
}

list_of_tuples = [(key, value) for key, value in dict1.items()]
print(list_of_tuples)

