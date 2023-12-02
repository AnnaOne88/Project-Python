#split() function:
sentence = "this is a sample."
words = sentence.split(" ")
print(words)

#working with a dictionary
dict = {
    'blue' : 'blau',
    'red' : 'rot',
    'yellow' : 'gelb'
}
print('\nOur dictionary: ', dict)

print('--- only keys:')
for key in dict.keys():
    print(key)

print('\n---only values:')

for value in dict.values():
    print(value)

#convert all keys into a list:
keys_list = []
for key in dict.keys():
    keys_list.append(key)
print('\nour list of keys:', keys_list)

# print key-value pair:
for key, value in dict.items():
    print(key, value) #if you want to format the pair, then use print(f'{key}: {value}')