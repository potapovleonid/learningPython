import math

type_of_figure = input('Input type of figure: ')

if type_of_figure.lower() == 'circle':
    radios = float(input('Input circle radios: '))
    print('Area: ' + (math.pi * radios ** 2).__str__())
elif type_of_figure.lower() == 'triangle':
    first_side = float(input('Input first side: '))
    second_side = float(input('Input second side: '))
    third_side = float(input('Input third side: '))
    s = (first_side + second_side + third_side) / 2
    area = math.sqrt(s * (s - first_side) * (s - second_side) * (s - third_side))
    print('Area: ' + area.__str__())
elif type_of_figure.lower() == 'rectangle':
    first_side = float(input('Input first side: '))
    second_side = float(input('Input second side: '))
    print('Area: ' + (first_side * second_side).__str__())
else:
    print('Type is incorrect')
