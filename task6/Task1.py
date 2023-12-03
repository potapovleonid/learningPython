import datetime
from datetime import date, timedelta


def get_date_range(start_date, last_date):
    if last_date < start_date:
        return []
    delta = last_date - start_date
    return [(start_date + timedelta(days=i)) for i in range(delta.days + 1)]


print(*get_date_range(date(2023, 12, 20), date(2023, 11, 15)), sep='\n')
