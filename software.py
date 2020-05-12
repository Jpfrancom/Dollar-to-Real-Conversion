import requests
import json
while True:
    req = requests.get('https://api.hgbrasil.com/finance')
    quotation = json.loads(req.text) #quotation['results']['currencies']['USD']['buy']
    d = quotation['results']['currencies']['USD']['buy']
    option = int(input('''[1] dollar --> Real \n[2] Real --> dollar \nchoice: '''))
    if option == 1:
        dollar = float(input('dollar: '))
        real = dollar * d
        print(f'{dollar} USD to {real:.2f} BRA')
    elif option == 2:
        real = float(input('Real: '))
        dollar = real / d
        print(f'{real} BRA to {dollar:.2f} USD')
    else:
        print('[ \033[1;31mERROR\033[m ] Number cannot be recognized.')
    print('-=-='*10)
    while True:
        YorN = str(input('Do you wish to continue? [y] [n]: ')).upper()
        if YorN in 'YN':
            break
        else:
            print('[ \033[1;31mERROR\033[m ] Code cannot be recognized.')
    if YorN == 'N':
        break