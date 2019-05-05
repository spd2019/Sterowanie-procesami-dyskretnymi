import numpy as np
from Zajecia_czwarte import read_data as rd
from Zajecia_czwarte import schrage

# print("Welcome to Schrage algorithm")
# print("----------------------------")
# print("Which test would you like to use?")
# print(" 1. in50 \r\n 2. in100 \r\n 3. in200 \r\n 4.FULL(sum)")
# test_nr = int(input("Enter your choose: "))
test_nr = 4


if test_nr == 1:
    tasks_val, columns_val, tasks = rd.read_data_2list("in50.txt")
    print(tasks)
    sigma50, Cmax50 = schrage.Schrage(tasks)
    print("-------SCHRAGE--------")
    print("Correct result for in50 test is 1513")
    print("Your result is: ", Cmax50)
    if Cmax50 == 1513: print("CORRECT!")

    sigma50_pmtn, Cmax50_pmtn = schrage.Schrage_pmtn(tasks)
    # sigma50_pmtn, Cmax50_pmtn = schrage.schragepmtn(tasks)
    print("-----SCHRAGE_PMTN------")
    print("Correct result for in50 test is 1492")
    print("Your result is: ", Cmax50_pmtn)
    if Cmax50_pmtn == 1492: print("CORRECT!")


elif test_nr == 2:
    tasks_val, columns_val, tasks = rd.read_data_2list("in100.txt")
    sigma100, Cmax100 = schrage.Schrage(tasks)
    print("Correct result for in100 test is 3070")
    print("Your result is: ",Cmax100)
    if Cmax100 == 3070: print("CORRECT!")

    sigma100_pmtn, Cmax100_pmtn = schrage.Schrage_pmtn(tasks)
    print("-----SCHRAGE_PMTN------")
    print("Correct result for in100 test is 1492")
    print("Your result is: ", Cmax100_pmtn)
    if Cmax100_pmtn == 1492: print("CORRECT!")


elif test_nr == 3:
    tasks_val, columns_val, tasks = rd.read_data_2list("in200.txt")
    sigma200, Cmax200 = schrage.Schrage(tasks)
    print("Correct result for in200 test is 6416")
    print("Your result is: ",Cmax200)
    if Cmax200 == 6416: print("CORRECT!")

    sigma200_pmtn, Cmax200_pmtn = schrage.Schrage_pmtn(tasks)
    print("-----SCHRAGE_PMTN------")
    print("Correct result for in200 test is 6398")
    print("Your result is: ", Cmax200_pmtn)
    if Cmax200_pmtn == 6398: print("CORRECT!")

elif test_nr == 4:
    results = []
    results_pmtn = []
    tests = ["in50.txt", "in100.txt", "in200.txt"]
    for test_file in tests:
        tasks_val, columns_val, tasks = rd.read_data_2list(test_file)
        sigma, Cmax = schrage.Schrage(tasks)
        sigma_pmtn, Cmax_pmtn = schrage.Schrage_pmtn(tasks)
        results.append(Cmax)
        results_pmtn.append(Cmax_pmtn)
    print("=== Schrage === \r\n Correst result is: [1513, 3076, 6416]")
    print("Your result is:", results)
    print("=== Schrage Pmtn === \r\n Correst result is: [1492 3070 6398]")
    print("Your result is:", results_pmtn)