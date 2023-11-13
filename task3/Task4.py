stats = {
    'facebook': 55,
    'yandex': 115,
    'vk': 120,
    'google': 99,
    'email': 42,
    'ok': 98
}

max_value = max(stats.values())

for name, value in stats.items():
    if value == max_value:
        print(f'Max sale value into: {name}')
