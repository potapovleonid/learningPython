def calc_sum(path_to_file):
    file_sum = 0
    file = None
    try:
        file = open(path_to_file)
        for i in file:
            i = i.strip().split(" ")
            if len(i) >= 3: file_sum += i[2]
    except FileNotFoundError as e:
        print("Error open file")
    except Exception as e:
        print(e)
    finally:
        if file is not None:
            file.close()


calc_sum('../rwdata/data_2/real_data.txt')
