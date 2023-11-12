results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

for value in results.values():
    roi = format((value.get('revenue') / value.get('cost') - 1) * 100, '.2f')
    value.setdefault('ROI', roi)

print(*results.items(), sep='\n')
