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


def write_csv_file_companies(file_path: str, data: dict) -> None:
    """
    Writes csv from list of lines
    Args:
        file_path: path to csv file
        data: dict to write
    Returns:
        None
    """
    with open(file=file_path, mode='w', encoding='UTF-8') as file:
        fieldnames = ['Company', 'countProduct']
        lines_writer = csv.DictWriter(file,
                                      fieldnames=fieldnames,
                                      quoting=csv.QUOTE_MINIMAL,
                                      delimiter=',',
                                      quotechar='|',
                                      lineterminator='\r')
        lines_writer.writeheader()
        for company in data.keys():
            lines_writer.writerow({'Company': f'{company}', 'countProduct': f'{data[company]}'})


def count_devices_in_company(data: list) -> dict:
    """
    Gets data from file and writes file count_company.csv and returns how many devices in each company(dict)
    Args:
        data:

    Returns:
        dict: key(company), value(amount devices)
    """
    companies = {}
    for line in data:
        if line[0] in companies.keys():
            companies[line[0]] += 1
        else:
            companies.update({f"{line[0]}": 1})

    write_csv_file_companies('count_company.csv', companies)
    return companies


def main():
    """
    Main func executes on start
    """
    data = read_csv_file('devices.csv')
    data.pop(0)
    result = count_devices_in_company(data)
    print(f'От компании Asus у нас есть {result['Asus']} товаров.')


if __name__ == "__main__":
    main()
