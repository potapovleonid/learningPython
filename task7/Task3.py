import libs.exchange as exc


def get_currency_with_maximum_course():
    rt = exc.Rate()

    name = ''
    value = 0

    for info in rt.exchange_rates().values():
        print(f"{info['Name']} {info['Value']}")
        if info['Value'] > value:
            name = info['Name']
            value = info['Value']
    print({name: value})