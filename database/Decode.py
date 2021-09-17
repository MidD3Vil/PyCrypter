from Bank import bank

bank = bank()

word = str(input('\nDigite o texto para decrypt: '))

len = len(word)
list = []
count = 0

for c in range(len):
    if count % 2 == 0:
        list.append(word[count])
    else:
        pass
    count += 1
print('\n\n')

count = 0
for element in list:
    place = bank.index(element)
    place_plus = (place - count)
    print(f'{bank[place_plus]}', end='')
    count += 1
