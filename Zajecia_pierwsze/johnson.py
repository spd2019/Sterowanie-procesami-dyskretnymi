import numpy as np


def johnson_algorithm(machines_val, tasks):
    print("\n Johnson algorithm: START")
    if(machines_val == 2):
        print("Two machines algorithm: START")
        return johnson2m(tasks)
    if (machines_val == 3):
        print("Three machines algorithm")
        return johnson3m(tasks)


def johnson2m(tasks):
    tmp_tasks = tasks.copy()

    mt_row = 0
    mt_column = 0
    tab1 = []
    tab2 = []
    iter = 0
    while(iter != len(tasks)):
        min_time = 100
        for i in range(0, len(tasks)):
            for j in range(0, len(tasks[i])):
                if(min_time > tasks[i][j]):
                    min_time = tasks[i][j]
                    mt_row = i
                    mt_column = j
        tasks[mt_row] = 1000

        if (mt_column == 0):
            tab1.append(mt_row)
        if (mt_column == 1):
            tab2.append(mt_row)
        iter = iter +1

    sequence = tab1 + list(reversed(tab2))


    print("Best sequence: ", sequence)
    print("Two machines algorithm: DONE")


##Creating 2 virtual machines
def transform3to2(tasks):
    virtual = np.zeros((len(tasks),2))

    for i in range(0, len(tasks)):
        virtual[i][0] = tasks[i][0] + tasks[i][1]
        virtual[i][1] = tasks[i][1] + tasks[i][2]

    print("Virtual machines: \n", virtual)
    return virtual

def johnson3m(tasks):
    print("Three machines algorithm: START")
    virtual_machine = transform3to2(tasks)
    johnson2m(virtual_machine)
    print("Three machines algorithm: DONE")

