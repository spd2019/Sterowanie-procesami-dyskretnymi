import numpy as np

def read_data_2list(filename):
    file = open(filename, "r")
    tasks_val, columns_val = file.readline().split()
    tasks_val = int(tasks_val)
    columns_val = int(columns_val)
    tasks = []
    values = []
    for val in file.read().split():
        values.append(float(val))

    for a in range(0, len(values), 3):
        tmp_tab = []
        for b in range(0,3):
            tmp_tab = tmp_tab + [values[a+b]]
        tasks.append(tmp_tab)


    #print("Number of tasks: ", tasks_val)
    #print("Number of columns: ", columns_val)
    #print("Tasks: \n", tasks)
    file.close()
    return tasks_val, columns_val, tasks
