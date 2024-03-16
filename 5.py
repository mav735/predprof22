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


def generate_hash(data) -> list:
    """
    Generates hash for each line in csv db
    Args:
        data: uploaded from csv file

    Returns:
        list: new_data with hash as last element
    """
    p = 53
    m = 10 ** 9 + 8

    for i in range(len(data)):
        line_to_encode = data[i][0] + ' ' + data[i][1]
        hash_ = 0
        for j in range(len(line_to_encode)):
            hash_ += ord(line_to_encode[j]) * ((p ** j) % m)
        data[i].append(hash_)

    return data


def main():
    """
    Main func executes on start and generates hash for each element of data from csv file
    """
    data = read_csv_file('devices.csv')
    data.pop(0)
    data = generate_hash(data)
    for line in data[:10]:
        print(f'{line[0]}\t{line[1]}, \t hash: {line[-1]}')


if __name__ == "__main__":
    main()
