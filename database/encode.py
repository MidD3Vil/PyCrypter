def encode(word, key):
    len_str = len(word)
    from Bank import bank
    end_list = []
    # pad = ['m', 'i', 'd']
    count = count_add = count_key = 0
    for c in range(len_str):
        place = bank.index(word[count])
        place_plus = (place + int(key[count_key]))
        end_list.append(f'{bank[place_plus]}{count_add}')
        count += 1
        count_add += 1
        count_key += 1
        if count_add == 9:
            count_add = 0
        if count_key == 4:
            count_key = 0
    end_list = ''.join(end_list)
    str_list = str(end_list)
    result = ''.join(map(str, str_list))
    return result
