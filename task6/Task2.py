def calc_sum(path_to_file):
    file_sum = 0
    with open(path_to_file, 'r') as file:
        for i in file:
            price = i.strip().split('\t')[2]
            try:
                file_sum += float(price.replace(',', '.'))
            except:
                pass
    return file_sum


print(calc_sum('../rwdata/data_2/real_data.txt'))