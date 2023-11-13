person = int(input('Input quantity of persons: '))

cook_book = {
    'салат': [
        {'ingredient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
        {'ingredient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
        {'ingredient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
        {'ingredient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
        {'ingredient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
        {'ingredient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
    'пицца': [
        {'ingredient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
        {'ingredient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
        {'ingredient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
        {'ingredient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
        {'ingredient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
        {'ingredient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
    ],
    'лимонад': [
        {'ingredient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
        {'ingredient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
        {'ingredient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
    ]
}

all_ingredients = []

for dish in cook_book.keys():
    for ingredient in cook_book.get(dish):
        all_ingredients_of_dish = [ingredient.get('ingredient_name'),
                                   ingredient.get('quantity'),
                                   ingredient.get('measure')]

        for name, quantity, measure in all_ingredients:
            if all_ingredients_of_dish[0] == name and all_ingredients_of_dish[2] == measure:
                all_ingredients[all_ingredients.index([name, quantity, measure])] = \
                    [name, quantity + all_ingredients_of_dish[1], measure]
                break
            else:
                all_ingredients.append(all_ingredients_of_dish)
                break

        if len(all_ingredients) == 0:
            all_ingredients.append(all_ingredients_of_dish)

print(*[f'{name}: {quantity * person} {measure}' for name, quantity, measure in all_ingredients], sep='\n')
