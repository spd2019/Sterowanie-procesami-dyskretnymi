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
    print("2m")


def johnson3m(tasks):
    print("3m")


tasks_val, machines_val, tasks = read_data("data_2m.txt")
johnson_algorithm(machines_val, tasks)


#input('Press ENTER to continue...')


##ALGORYTM JOHNSONA


