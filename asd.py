clovo = input('Введите слово ')
coglas = ''

for i in clovo:
    if i == 'а'or i == 'о' or i == 'у' or i == 'э' or i == 'я' or i == 'е' or i == 'и' or i == 'ю' or i == 'ё' or i == 'ы':
       continue
    else:
        coglas = coglas + i
       
print(coglas)

clovo = input('Введите слово ')
coglas = ''

for i in clovo:
    coglas = i + coglas
       
print(coglas)

clovo = input('Введите слово ')
coglas = 0
bukv = ''

for i in clovo:
    coglas = coglas +1
    if coglas % 2 != 0 :
        continue
    else :
        bukv += i
print(bukv)

clovo = input('Введите слово ')
coglas = input('Какая буква вам не нравиться ')
bukv = ''

for a in clovo :
    if a == coglas :
        continue
    else: 
        bukv += a
     
print(bukv)




