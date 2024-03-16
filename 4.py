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


def money_count(data: list) -> dict:
    """
    Gets money, that shop can get from selling all laptops of each company
    Args:
        data: base uploaded from csv
    Returns:
        dict: company + earnings
    """
    companies = {}
    for element in data:
        if element[0] in companies.keys():
            companies[element[0]] += float(element[-1].replace(',', '.'))
        else:
            companies.update({f"{element[0]}": float(element[-1].replace(',', '.'))})
    return companies


def main():
    """
    Main func executes on start and counts earnings from selling all devices of each company
    """
    data = read_csv_file('devices.csv')
    data.pop(0)
    result = money_count(data)
    for company in result:
        print(f'Если продать все ноутбуки {company} можно заработать {result[company]}.')


if __name__ == "__main__":
    main()
