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


def main():
    pass


if __name__ == '__main__':
    file_name = "numbers.csv"
    data = read_data(file_name)
    print(data)
    #main()
