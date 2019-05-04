import numpy as np

def read_data(filename):
    file = open(filename, "r")
    tasks_val, columns_val = file.readline().split()
    tasks_val = int(tasks_val)
    columns_val = int(columns_val)
    tasks = np.zeros((tasks_val, columns_val))
    for i in range(tasks_val):
        tmp = file.readline().split()
        for j in range(columns_val):
            tasks[i][j] = int(tmp[j])
    print("Number of tasks: ", tasks_val)
    print("Number of columns: ", columns_val)
    #print("Tasks: \n", tasks)
    file.close()
    return tasks_val, columns_val, tasks
