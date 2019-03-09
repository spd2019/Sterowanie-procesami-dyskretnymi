import numpy as np

print("Starting program...")

def read_data(filename):
    file = open(filename, "r")

    tasks_val, machines_val = file.readline().split()
    tasks_val = int(tasks_val)
    machines_val = int(machines_val)

    tasks = np.zeros((tasks_val,machines_val))
    for i in range(tasks_val):
        tmp = file.readline().split()
        for j in range(machines_val):
            tasks[i][j] = int(tmp[j])

    print("Number of tasks: ", tasks_val)
    print("Number of machines: ", machines_val)
    print("Tasks: \n", tasks)
    file.close()
    return tasks_val, machines_val, tasks


def johnson_algorithm(machines_val, tasks):
    if(machines_val == 2):
        print("Two machines algorithm")
        return johnson2m(tasks)
    if (machines_val == 3):
        print("Three machines algorithm")
        return johnson3m(tasks)


def johnson2m(tasks):
    #print("2m")
    #print(len(tasks[1]))
    mt_row = 0
    mt_column = 0
    tab1 = []
    tab2 = []
    iter = 0
    #print(len(tasks))
    while(iter != len(tasks)):
        min_time = 100
       # print(tasks)
        for i in range(0, len(tasks)):
            for j in range(0, len(tasks[i])):
                if(min_time > tasks[i][j]):
                    min_time = tasks[i][j]
                    mt_row = i
                    mt_column = j
        #print("Iteracja:", iter, "MT_ROW:",mt_row, "MT_COL:", mt_column)
        tasks[mt_row] = 1000

        if (mt_column == 0):
            tab1.append(mt_row)
           # print("Dodaje", mt_row, "Do tab 1")
        if (mt_column == 1):
            tab2.append(mt_row)
           # print("Dodaje", mt_row, "Do tab 2")

        iter = iter +1
        #print(iter)

    print(tab1)
    print(tab2)
    sequence = tab1 + list(reversed(tab2))
    print("Sequence: ", sequence)

def johnson3m(tasks):
    print("3m")


tasks_val, machines_val, tasks = read_data("data_2m.txt")
johnson_algorithm(machines_val, tasks)


#input('Press ENTER to continue...')


##ALGORYTM JOHNSONA


