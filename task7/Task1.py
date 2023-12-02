line = '2019-01-01,organic,4293'


def column_count(columns_str: str):
    if columns_str:
        columns = line.split(',')
        return len(columns)
    else:
        return 0


print(column_count(line))
