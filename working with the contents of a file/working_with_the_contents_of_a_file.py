t = 'text.txt'

with open(t, 'a') as text:
    a = True
    print('Для выхода нажмите "q"')
    print('______________________')
    print('\n')
    mes_1 = ''
    while mes_1 != 'q':
        mes_1 = input('Ведите имя: ')
        if mes_1 != 'q':
            text.write(f'{mes_1} Вроде человек... \n')
            print(f'Имя {mes_1} сохранено \n')
        else:
            print('Завершение программы...')
            break
            
        
