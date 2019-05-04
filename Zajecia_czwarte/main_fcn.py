import numpy as np
from Zajecia_czwarte import read_data as rd
from Zajecia_czwarte import schrage

print("Welcome to Schrage algorithm")
print("----------------------------")
print("Which test would you like to use?")
print(" 1. in50 \r\n 2. in100 \r\n 3. in200")
test_nr = int(input("Enter your choose: "))


if test_nr == 1:
    tasks_val, columns_val, tasks = rd.read_data("in50.txt")
    cmax = schrage.Schrage(tasks_val, tasks)
    print("Correct result for in50 test is 1513")
    print("Your result is: ")
    if cmax == 1513: print("CORRECT!")

elif test_nr == 2:
    tasks_val, columns_val, tasks = rd.read_data("in100.txt")
    cmax = schrage.Schrage(tasks_val, tasks)
    print("Correct result for in100 test is 3076")
    print("Your result is: ",cmax)
    if cmax == 3076: print("CORRECT!")

elif test_nr == 3:
    tasks_val, columns_val, tasks = rd.read_data("in200.txt")
    cmax = schrage.Schrage(tasks_val, tasks)
    print("Correct result for in200 test is 6416")
    print("Your result is: ",cmax)
    if cmax == 6416: print("CORRECT!")
