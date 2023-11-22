import json


def read_file_and_get_dict(file_path: str) -> dict:
    with open(file_path, 'r', encoding='UTF-8') as file:
        res_dict = dict()
        for item in file:
            res_dict.setdefault(json.loads(item)['user_id'], json.loads(item)['category'])
        return res_dict


def check_buys_and_write_to_file(all_buys: dict, file_path_all_buys: str, filename: str):
    with open(file_path_all_buys, 'r', encoding='UTF-8') as file_r:
        with open(f'../rwdata/{filename}', 'w', encoding='UTF-8') as file_w:
            while True:
                res = file_r.readline()
                if res == '':
                    break
                if res.split(',')[0] in all_buys:
                    file_w.write(res)


check_buys_and_write_to_file(read_file_and_get_dict('../rwdata/purchase_log.txt'), '../rwdata/visit_log.csv', 'funnel.csv')
