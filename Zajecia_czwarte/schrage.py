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
    print("Tasks: \n", tasks)
    file.close()
    return tasks_val, columns_val, tasks

tasks_val, columns_val, tasks = read_data("test.txt")
S = []
for i in range(0, tasks_val):
    S.append(tasks[i][0])

#Shrage
delta = []
Ng = []
Nn = []
Q = []
for i in range(0, tasks_val):
    Nn.append(i)
t = 0
k = 1
cmax = 0
e = 0

while Ng != [] or Nn != []:
    while Nn != [] and min(S) <= t:
        e = np.argmin(S)
        Ng.append(e)
        print("Ng: ", Ng)
        Nn.remove(e)
        print("Nn: ", Nn)
        S[e]=50
        print("S: ", S)
    if Ng == []:
        t = min(S)
    else:
        for i in Ng:
            Q.append(tasks[i][2])
        e = np.argmax(Q)
        if e in Ng:
            Ng.remove(e)
        delta.append(e)
        k = k+1
        t = t+tasks[e][1]
        cmax = max(cmax, t+tasks[e][2])
        Q = []
print("delta: ", delta)
print("Cmax: ", cmax)
