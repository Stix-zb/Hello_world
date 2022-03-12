# mass = [5, 'gh', 1, 'zx', 'Ajhg', 8]
# digits = []
# abc = []
#
# for i in mass:
#     if type(i) == int or type(i) == float:
#         digits.append(i)
#     else:
#         abc.append(i)
# # str1 = str(sorted(digits))
# # print(str1)
#
#
# with open('test1.txt', 'w') as file1:
#     file1.write(' '.join(sorted(abc, key=len)) + '\n')
#     [file1.write(str(q) + ' ') for q in sorted(digits)]


# Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов
# продукции, а также узнать её состав.
# Реализуйте кондитерскую.
# У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и т.д.).
# Значение – список, который содержит состав, цену (за 100гр) и кол-во (в граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном
# списке
# 6. До свидания

products = {'торт':['медовые коржи с кремом',20, 1700],
            'пироженное':['шоколад с вишней',15, 950],
            'маффин':['сгущеное молоко',10, 900],
            'кекс':['изюм, шоколад',5, 750],}

menu = ('1','2','3','4','5')

all_price = 0
# print('Наличие товаров в магазине: ')
# for k, v in products.items():
#     print(f'{k} - {v[0]} - {v[1]}')

while True:
    vibor = input('Если хотите посмотреть описание, введите 1 \n'
                    'Если хотите посмотреть цену, введите 2 \n'
                    'Если хотите посмотреть наличие, введите 3 \n'
                    'Если хотите посмотреть всю информацию, введите 4 \n'
                    'Если хотите приступить к покупкам, введите 5 \n'
                    'Если хотите закончить, введите n \n'
                    'Ваш ответ: ')
    if vibor not in menu and vibor != 'n':
        print('Попробуйте снова!')
        continue
    elif vibor == 'n':
        break
    elif vibor == '1':
        print('-'*50)
        for k, v in products.items():
            print(f'{k} - {v[0]}')
        print('-'*50)
        continue
    elif vibor == '2':
        print('-'*50)
        for k, v in products.items():
            print(f'{k} - {v[1]} руб. за 100 гр.')
        print('-'*50)
        continue
    elif vibor == '3':
        print('-'*50)
        for k, v in products.items():
            print(f'{k} - {v[2]} гр.')
        print('-'*50)
        continue
    elif vibor == '4':
        print('-'*50)
        for k, v in products.items():
            print(f'{k} - {v[0]} - {v[1]} руб. за 100 гр. - {v[2]} гр. в наличии')
        print('-'*50)
        continue
    elif vibor == '5':
        while True:
            product = input('Введит название продукта: ')
            if product not in products and product != 'n':
                print('В нашем магазине нету такого товара. Попробуйте снова!')
                continue
            elif product in products:
                amount = int(input('Введите количество: '))
                if amount <= products[product][2]:
                    all_price += products[product][1] * amount / 100
                    products[product][2] -= amount
                    print('Покупка совершена успешно!\n')
                else:
                    print('В нашем магазине нет этого товара в таком количестве :(\nПопробуйте снова')
                    continue
            else:
                print('-'*50)
                print(f'Вы совершили покупки на сумму: {all_price} руб.\n\n\n')
                print('Отстаток товаров в магазине:')
                for k, v in products.items():
                    print(f'{k} - {v[0]} - {v[1]} руб. за 100 гр. - {v[2]} гр. в наличии')
                print()
                break