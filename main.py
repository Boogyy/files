from pprint import pprint
cookbook_data = 'ingredients.txt'


def catalog_reader(file_name):
    with open(file_name, encoding='utf-8') as recipe_book:
        result = {}
        for line in recipe_book:
            dish = line.strip()
            products = []
            for items in range(int(recipe_book.readline())):
                check_dict_data = {}
                checking = recipe_book.readline().strip()
                check = checking.split(' | ')
                check_dict_data['ingredient_name'] = check[0]
                check_dict_data['quantity'] = check[1]
                check_dict_data['measure'] = check[2]
                products.append(check_dict_data)
            result[dish] = products
            recipe_book.readline()
    return result


cook_book = catalog_reader(cookbook_data)
pprint(cook_book, sort_dicts=False)
print()


def get_shop_list_by_dishes(dishes, person):
    result_shop_list = {}
    for dish in dishes:
        list_ingredient = (cook_book[dish])
        for item in list_ingredient:
            resources = {}
            ingredient = item['ingredient_name']
            count = int(item['quantity']) * person
            if ingredient in result_shop_list:
                count += result_shop_list[ingredient]['quantity']
            resources['measure'] = item['measure']
            resources['quantity'] = count
            result_shop_list[ingredient] = resources
    return result_shop_list


dish_1 = get_shop_list_by_dishes(['Омлет', 'Омлет', 'Омлет'], 1)
dish_2 = get_shop_list_by_dishes(['Омлет'], 3)
pprint(dish_1)
print()
pprint(dish_2)
print()

first_txt = '1.txt'
second_txt = '2.txt'
third_txt = '3.txt'
file_data = [first_txt, second_txt, third_txt]


def open_file(file_name):
    result = {}
    for item_txt in file_name:
        with open(item_txt, encoding='utf-8') as txt_obj:
            check_list = []
            for i in txt_obj.readlines():
                check_list.append(i.strip())
        result[item_txt] = check_list
    return result


element = open_file(file_data)


def read_txt(file_data_name):
    result = {}
    for i in file_data_name:
        with open(i, encoding='utf-8') as file:
            result[i] = (len(file.readlines()))
    return result


file_obj = read_txt(file_data)
data = []
for i in file_obj.values():
    data.append(i)
data.sort()


def get_key(file, value):
    for k, v in file.items():
        if v == value:
            return k


for item in data:
    print(get_key(file_obj, item))
    print(item)
    for i in element[get_key(file_obj, item)]:
        print(i)

