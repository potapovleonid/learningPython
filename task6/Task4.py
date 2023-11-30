from datetime import datetime

all_dates = ['2018-04-02', '2018-02-29', '2018-19-02']


def check_dates_validation(stream: []):
    return [f'{i} is_valid: {check_date_validation(i)}' for i in stream]


def check_date_validation(dt: str):
    try:
        datetime.strptime(dt, '%Y-%m-%d')
        return True
    except ValueError:
        return False


print(check_dates_validation(all_dates))
