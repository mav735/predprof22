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


def merge_sort_company(mass: list, reverse: bool) -> list:
    """
    Function that implements merge sort

    Args:
        mass: list to sort
        reverse: bool value, ascending or descending order

    Returns:
        list: sorted mass
    """
    if len(mass) > 1:
        mid = len(mass) // 2
        left = mass[:mid]
        right = mass[mid:]
        merge_sort_company(left, reverse)
        merge_sort_company(right, reverse)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                mass[k] = left[i]
                i += 1
            else:
                mass[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            mass[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            mass[k] = right[j]
            j += 1
            k += 1

    if reverse:
        return mass[::-1]
    return mass


def main():
    """
    Main func executes on start
    """
    data = read_csv_file('devices.csv')
    data.pop(0)
    data = merge_sort_company(data, reverse=True)
    for element in data[:5]:
        print(f'{element[0]} - {element[1]} - {element[-1]}')


if __name__ == "__main__":
    main()
