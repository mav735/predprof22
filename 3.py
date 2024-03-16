import csv


def read_csv_file(file_path: str) -> list:
    """
    Reads csv and returns list of lines
    Args:
        file_path: path to csv file

    Returns:
        list: of lines
    """
    with open(file_path, encoding='UTF-8') as file:
        lines_reader = csv.reader(file, delimiter=';')
        return [line for line in lines_reader]


def linear_search(data: list, value: str) -> list:
    """
    Gets data and product to find
    Args:
        data: base uploaded from csv
        value: product to find

    Returns:
        list: list of index
    """
    result = []
    for i in range(len(data)):
        if data[i][1] == value:
            result.append(i)
    return result


def main():
    """
    Main func executes on start and find device by name
    """
    data = read_csv_file('devices.csv')
    data.pop(0)
    now_find = input('Введите модель устройства:\n')
    while now_find != '666':
        res_find = linear_search(data, now_find)
        if res_find:
            print(f'По вашему запросу: {now_find} найдены следующие варианты:')
            for element in res_find:
                print(f'{data[element][0]} {data[element][1]} - тип устройства: {data[element][2]};'
                      f' Разрешение экрана - {data[element][3]}; Цена - {data[element][-1]}')
        else:
            print('У нас нет данного устройства\n')
        now_find = input('\nВведите модель устройства:\n')


if __name__ == "__main__":
    main()
