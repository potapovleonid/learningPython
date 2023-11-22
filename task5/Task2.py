def read_n_lines_into_file(file: open, number_of_lines: int):
    result = []
    for i in range(0,number_of_lines):
        result.append(file.readline().strip())

    file.close()
    return result

res = read_n_lines_into_file(open('../rwdata/visit_log.csv', 'r'), 5)

print(*res, sep='\n')
