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


def selection_sort(list_of_numbers, direction="descending"):
    """
    Sorts a list of numbers in ascending order using Selection Sort.
    :param list_of_numbers: list of integers
    :param direction: direction of sorting, "ascending" or "descending" (default: "ascending")
    :return: sorted list of integers
    """
    n = len(list_of_numbers)
    for i in range(n-1):
        if direction == "ascending":
            min_index = i
            for j in range(i+1, n):
                if list_of_numbers[j] < list_of_numbers[min_index]:
                    min_index = j
            list_of_numbers[i], list_of_numbers[min_index] = list_of_numbers[min_index], list_of_numbers[i]
        elif direction == "descending":
            max_index = i
            for j in range(i+1, n):
                if list_of_numbers[j] > list_of_numbers[max_index]:
                    max_index = j
            list_of_numbers[i], list_of_numbers[max_index] = list_of_numbers[max_index], list_of_numbers[i]

    return list_of_numbers


def bubble_sort(list_of_whole_numbers):
    """
    Sorts a list of numbers in ascending order using Bubble Sort.
    :param list_of_whole_numbers: list of integers
    :return: sorted list of integers
    """
    n = len(list_of_whole_numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_of_whole_numbers[j] > list_of_whole_numbers[j+1]:
                list_of_whole_numbers[j], list_of_whole_numbers[j+1] = list_of_whole_numbers[j+1], list_of_whole_numbers[j]

    return list_of_whole_numbers


def insertion_sort(list_of_whole_numbers):
    """
    Sorts a list of numbers in ascending order using Insertion Sort.
    :param list_of_whole_numbers: list of integers
    :return: sorted list of integers
    """
    for i in range(1, len(list_of_whole_numbers)):
        key = list_of_whole_numbers[i]
        j = i - 1
        while j >= 0 and key < list_of_whole_numbers[j]:
            list_of_whole_numbers[j + 1] = list_of_whole_numbers[j]
            j -= 1
        list_of_whole_numbers[j + 1] = key

    return list_of_whole_numbers


def main():
    file_name = "numbers.csv"
    data = read_data(file_name)
    print("Původní data:", data)

    for key in data:
        unsorted_numbers = data[key]
        sorted_numbers = selection_sort(unsorted_numbers)
        print("\nSeřazená posloupnost podle selection_sort '{}':".format(key))
        print(sorted_numbers)

    for key in data:
        unsorted_numbers = data[key]
        sorted_numbers = bubble_sort(unsorted_numbers)
        print("\nSeřazená posloupnost podle bubble_sort '{}':".format(key))
        print(sorted_numbers)

    for key in data:
        unsorted_numbers = data[key]
        sorted_numbers = insertion_sort(unsorted_numbers)
        print("\nSeřazená posloupnost podle insertion_sort '{}':".format(key))
        print(sorted_numbers)


if __name__ == '__main__':
    main()
