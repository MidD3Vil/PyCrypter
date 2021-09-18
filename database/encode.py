def encode():
    import os

    ## Tabela de cores ANSI (Python) ##
    Mblack = '\033[1;30m'   # Preto
    Ired = '\033[1;31m'     # Vermelho
    Dgreen = '\033[1;32m'   # Verde
    Nyellow = '\033[1;33m'  # Amarelo
    Iblue = '\033[1;34m'    # Azul
    Gpurple = '\033[1;35m'  # Roxo
    Hcyan = '\033[1;36m'    # Ciano
    Twhite = '\033[1;37m'   # Branco
    VRCRM = '\033[0;0m'     # Remover
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    clear()
        
    print(f'Script de Ofuscação by Dr Midnight')
    
    print(f'{Gpurple}====================================\n')
    word = str(input(f'{Gpurple}Digite o texto para encrypt:{VRCRM} '))
    key = str(input(f'{Gpurple}Digite o seu pin de 4 digitos:{VRCRM} '))
    print(f'\n{Gpurple}====================================')
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
