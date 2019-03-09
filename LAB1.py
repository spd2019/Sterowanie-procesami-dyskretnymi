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


read_data("data_2m.txt")










#input('Press ENTER to continue...')


##ALGORYTM JOHNSONA


