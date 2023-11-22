def read_and_write_by_type(file_read_path: str, filename_write_path: str, filter_type: str):
    with open(file_read_path, 'r') as fr:
        with open(filename_write_path, 'w') as fw:
            while True:
                res = fr.readline()
                if filter_type in res:
                    fw.write(res)
                elif res == '':
                    break


read_and_write_by_type('../rwdata/visit_log.csv', '../rwdata/context.csv', 'context')
