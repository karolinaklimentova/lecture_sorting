import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    data_dict = {}
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, 'r', newline="\n") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        iteration = 0
        for row in csv_reader:
            for column, value in row.items():
                if iteration == 0:
                    data_dict[column] = [int(value)]
                else:
                    data_dict[column].append(int(value))
            iteration = iteration + 1

    return data_dict


def selection_sort(list_of_numbers):
    """
    Sorts a list of numbers in ascending order using Selection Sort.
    :param list_of_numbers: list of integers
    :return: sorted list of integers
    """
    n = len(list_of_numbers)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if list_of_numbers[j] < list_of_numbers[min_index]:
                min_index = j

        list_of_numbers[i], list_of_numbers[min_index] = list_of_numbers[min_index], list_of_numbers[i]

    return list_of_numbers


def main():
    file_name = "numbers.csv"
    data = read_data(file_name)
    print("Original data:", data)
    for key in data:
        unsorted_series = data[key]
        sorted_series = selection_sort(unsorted_series)
        print("\nSorted series '{}':".format(key))
        print(sorted_series)


if __name__ == '__main__':
    main()
