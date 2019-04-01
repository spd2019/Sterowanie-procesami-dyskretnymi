import numpy as np
import random as ran
import math

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

def makespan(order, tasks, machines_val):
    times = []
    for i in range(0, machines_val):
        times.append(0)
    for j in order:
        times[0] += tasks[j][0]
        for k in range(1, machines_val):
            if times[k] < times[k-1]:
                times[k] = times[k-1]
            times[k] += tasks[j][k]
    return max(times)

def sum_and_order(tasks_val, machines_val, tasks):
    tab = []
    tab1 = []
    for i in range(0, tasks_val):
        tab.append(0)
        tab1.append(0)
    for j in range(0, tasks_val):        #sumuje czas wykonywania się poszczególnych zadań
        for k in range(0, machines_val):
            tab[j] += tasks[j][k]
    #print(tab)
    tmp_tab = tab.copy()
    place = 0
    iter = 0
    while(iter != tasks_val):           #układa zadania w kolejności malejącej
        max_time = 1
        for i in range(0, tasks_val):
            if(max_time < tab[i]):
                max_time = tab[i]
                place = i
        tab[place] = 1
        tab1[iter] = place
        iter = iter + 1
    #print(tab1)
    return tab1

def insert(sequence, position, value):
    new_seq = sequence[:]
    new_seq.insert(position, value)
    return new_seq

def neh(tasks, machines_val, tasks_val):
    order = sum_and_order(tasks_val, machines_val, tasks)
    current_seq = [order[0]]
    for i in range(1, tasks_val):
        min_cmax = float("inf")
        for j in range(0, i + 1):
            tmp = insert(current_seq, j, order[i])
            cmax_tmp = makespan(tmp, tasks, machines_val)
            #print(tmp, cmax_tmp)
            if min_cmax > cmax_tmp:
                best_seq = tmp
                min_cmax = cmax_tmp
        current_seq = best_seq
    return current_seq, makespan(current_seq, tasks, machines_val)

def swap(list, a, b):
    tmp_list = list.copy()
    tmp = tmp_list[a]
    tmp_list[a] = tmp_list[b]
    tmp_list[b] = tmp
    return tmp_list

def probability(Cold, Cnew, Temp):
    if Cnew < Cold:
        prob = 1
    else:
        prob = math.exp((Cold-Cnew)/Temp)
    return prob

tasks_val, machines_val, tasks = read_data("data1.txt")

def sym_wyzarzanie(tasks_val, tasks, machines_val):
    #pi0 = []
    #for i in range(0, tasks_val):
    #    pi0.append(i)
    #cmax0 = makespan(pi0, tasks, machines_val)
    pi0, cmax0 = neh(tasks, machines_val, tasks_val)
    pi = pi0
    cmax_old = cmax0
    T0 = 100
    T = T0
    u = 0.9
    Tgr = 10
    print(pi, cmax_old)
    while (T >= Tgr):
        a = ran.randrange(0, tasks_val)
        b = ran.randrange(0, tasks_val)
        piprim = swap(pi, a, b)
        cmax = makespan(piprim, tasks, machines_val)
        p = probability(cmax_old, cmax, T)
        s = ran.random()
        if p >= s:
            pi = piprim
            cmax_old = cmax
            T = u*T
        else:
            T = u*T
        print(pi, cmax_old, p, s)
    return pi, cmax_old

seq, c = sym_wyzarzanie(tasks_val, tasks, machines_val)
best_seq, best_cmax = neh(tasks, machines_val, tasks_val)
print (best_seq, best_cmax)
print (seq, c)
