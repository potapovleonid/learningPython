car_ids = ['A222BC96', 'AB22BB193', 'C974AY105']

for car_id in car_ids:
    if 8 <= len(car_id) <= 9 and car_id[0].isalpha() and car_id[1:4].isnumeric() and car_id[4:6].isalpha():
        if len(car_id) == 8 and car_id[6:8].isnumeric():
            print(f'Number {car_id} is valid. Region: {car_id[6:8]}')
        elif car_id[6:9].isnumeric():
            print(f'Number {car_id} is valid. Region: {car_id[6:9]}')
    else:
        print(f'Number {car_id} isn\'t valid.')
