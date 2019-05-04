import numpy as np
from Zajecia_czwarte import read_data as rd
from Zajecia_czwarte import schrage

print("Welcome to Schrage algorithm")
print("----------------------------")
print("Which test would you like to use?")
print(" 1. in50 \r\n 2. in100 \r\n 3. in200")
test_nr = input("Enter your choose: ")


def in50_test():
    tasks_val, columns_val, tasks = rd.read_data("in50.txt")
    cmax = schrage(tasks_val, tasks)
    print("Correct result for in50 test is 1513")
    print("Your result is: ",cmax)

def in100_test():
    tasks_val, columns_val, tasks = rd.read_data("in100.txt")
    cmax = schrage(tasks_val, tasks)
    print("Correct result for in100 test is 3076")
    print("Your result is: ",cmax)

def in200_test():
    tasks_val, columns_val, tasks = rd.read_data("in200.txt")
    cmax = schrage(tasks_val, tasks)
    print("Correct result for in200 test is 6416")
    print("Your result is: ",cmax)


def switcher (test_nr):
    switcher = {
        1: in50_test(),
        2: in100_test(),
        3: in200_test()
    }
    func = switcher.get(test_nr, "nothing")
    return func()

switcher(test_nr)




