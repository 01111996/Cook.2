# Задание 1 (только открываю файл, в котором уже есть меню и кол-во ингр.)
f = open('cook.txt')
print(type(f))
cook_book = {}

# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish not in cook:
            continue
        for ingredient in cook[dish]:
            name = ingredients['ingredients_name']
            amount = ingredients['quantity'] * persons
            pieces = ingredients['pieces']
            if name in shop_list:
                shop_list[name]['quantity'] += amount
            else:
                shop_list[name] = {
                    'pieces': pieces,
                    'quantity': amount
                }
    return shop_list

    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задание 3 (строка 29 и 32 - это же открытие файлов через with? ЕСли нет, то, подскажите, пожалуйста, какие именно строки нужно переделать)
for file, name in enumerate (['1.txt', '2.txt']):
    with open('1.txt', 'w') as f:
        f.write('Строка номер 1 файла номер 1\n')
        f.write('Строка номер 2 файла номер 1\n')
    with open('2.txt', 'w') as f:
        f.write('Строка номер 1 файла номер 2\n')
file_names = ['1.txt', '2.txt']
files_data = []
for file_name in file_names:
    with open(file_name, 'r') as f:
        lines = f.readlines()
    files_data.append((file_name, lines))
files_data.sort(key=lambda x: len(x[1]))
with open('result.txt', 'w') as result:
    for file_name, lines in files_data:
        result.write(file_name + '\n')
        result.write(str(len(lines)) + '\n')
        result.writelines(lines)
        if lines and not lines[-1].endswith('\n'):
            result.write('\n')
