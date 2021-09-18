def menu():
    purple1 = '\033[38;5;53m'
    purple2 = '\033[38;5;54m'
    purple3 = '\033[38;5;55m'
    purple4 = '\033[38;5;56m'
    purple5 = '\033[38;5;57m'
    purple6 = '\033[38;5;93m'
    purple7 = '\033[38;5;92m'
    purple8 = '\033[38;5;91m'
    purple9 = '\033[38;5;127m'
    purple10 = '\033[38;5;128m'
    purple11 = '\033[38;5;129m'
    dic_color_purple = [
        purple1, purple1, purple1, purple2, purple2, purple2, purple3, purple3, purple3, purple4, purple4, purple4,
        purple5, purple5, purple5, purple6, purple6, purple6, purple7, purple7, purple7, purple8, purple8, purple8,
        purple9, purple9, purple9, purple10, purple10, purple10, purple11, purple11, purple11, purple10, purple10,
        purple10, purple9, purple9, purple9, purple8, purple8, purple8, purple7, purple7, purple7, purple6, purple6]
    from math import ceil
    txt = (r'''.                   
    
                    /|                                           |\
                   /||             ^               ^             ||\
                  / \\__          //               \\          __// \
                 /  |_  \         | \   /     \   / |         /  _|  \
                /  /  \  \         \  \/ \---/ \/  /         /  /     \
               /  /    |  \         \  \/\   /\/  /         /  |       \
              /  /     \   \__       \ ( 0\ /0 ) /       __/   /        \
             /  /       \     \__    \ \/|\_/ /    _/     /\         \   \
            /  /         \_)      \__ \/-\|/-\/ _/      (/\ \      `  \   \
           /  /           /\_)       \/  oVo  \/       (_/   ` \      `  \ \
          /  /           /,   \_)    (/\ _ /\_)    (__/         `      \  \ \
         /  '           //       \_)  (V_V)  (_/                    \  \     \
        /  '  '        /'           \   |{_}|   /         .              \  \ \
       /  '  /        /              \/ |{_}| \/\          `              \  \ \
      /     /        '       .        \/{___}\/  \          \    `         \  \ \
     /     /                ,         /{___}\   \          \    \         \      \
                            /         /{_/\__}\   `          \    `
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ┃
┃ ░░              ==================================================               ░░ ┃
┃ ░░                     ENCODE - DECODE  BY DR MIDNIGHT / VRC                     ░░ ┃
┃ ░░                          ESCOLHA A OPÇÃO QUE DESEJA:                          ░░ ┃
┃ ░░                                                                               ░░ ┃
┃ ░░              01 <<< ENCODE        <-------->      DECODE >>> 02               ░░ ┃
┃ ░░              ==================================================               ░░ ┃
┃ ░░              03 <<< ATUALIZAR     <-------->        SAIR >>> 04               ░░ ┃
┃ ░░              05 <<< CRIADOR       <-------->       GRUPO >>> 06               ░░ ┃
┃ ░░                                                                               ░░ ┃
┃ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    ''').strip()
    split = txt.split(None, 16)
    split_line = txt.split('\n')
    num_lines = len(split_line)
    process_number = 0
    count = -1
    for c in range(num_lines):
        print('')
        line1 = split_line[process_number]
        num_line1 = len(line1)
        num_line1_12 = ceil(num_line1 / 16)
        plus_fim = num_line1_12
        plus_inicio = 0
        list12 = []
        for c in range(16):
            list12.append(line1[plus_inicio:plus_fim])
            plus_fim += num_line1_12
            plus_inicio += num_line1_12
        list12_count = 0
        color = 'mid.vrc'
        count += 1
        for c in range(16):
            color = dic_color_purple[count]
            count += 1
            print(f'{color}{list12[list12_count]}', end='')
            list12_count += 1
        process_number += 1
        count -= 16
