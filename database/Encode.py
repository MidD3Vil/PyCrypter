from Bank import bank

bank = bank()

word = str(input('\nDigite o texto para encrypt: '))

len = len(word)
# pad = ['m', 'i', 'd']
count = 0
count2 = 0

for c in range(len):
    place = bank.index(word[count])
    place_plus = (place + count)
    print(f'{bank[place_plus]}{count2}', end='')
    count += 1
    if count2 == 9:
        count2 = 0
print('\n\n')
