# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
from error_tracking import ErrorDB


def main():
    print_hi(name)
    make_directories(data, model, test, output)
    ErrorDB()


def print_hi(name):
    """
    Pycharm standard breakpoint in the code line below to debug your script
    :param name:
    :return:
    """
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def make_directories(data, model, test, output):
    """
    creates the 'data', 'model', 'test', 'output', folders for data engineering pythonic code
    :param data:
    :param model:
    :param test:
    :param output:
    :return:
    """
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists("model"):
        os.makedirs("model")

    if not os.path.exists("test"):
        os.makedirs("test")

    if not os.path.exists("output"):
        os.makedirs("output")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = 'Andrew'
    data = str
    model = str
    test = str
    output = str
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
