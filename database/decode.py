def decode(word, key):
    len_str = len(word)
    from Bank import bank
    # pad = ['m', 'i', 'd']
    list = []
    end_list = []
    count = count_key = 0
    for c in range(len_str):
        if count % 2 == 0:
            list.append(word[count])
        else:
            pass
        count += 1
    count = 0
    for element in list:
        place = bank.index(element)
        place_plus = (place - int(key[count_key]))
        end_list.append(f'{bank[place_plus]}')
        count += 1
        count_key += 1
        if count_key == 4:
            count_key = 0
    end_list = ''.join(end_list)
    str_list = str(end_list)
    result = ''.join(map(str, str_list))
    return result
