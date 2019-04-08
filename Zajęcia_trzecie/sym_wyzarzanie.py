import numpy as np
import random as ran
import math
import time

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

def insertNEH(sequence, position, value):
    new_seq = sequence[:]
    new_seq.insert(position, value)
    return new_seq

def insert(sequence, tasks_val):
    a = ran.randrange(0, tasks_val)
    b = ran.randrange(0, tasks_val)
    new_seq = sequence[:]
    new_seq.remove(a)
    new_seq.insert(b, a)
    return new_seq

def neh(tasks, machines_val, tasks_val):
    order = sum_and_order(tasks_val, machines_val, tasks)
    current_seq = [order[0]]
    for i in range(1, tasks_val):
        min_cmax = float("inf")
        for j in range(0, i + 1):
            tmp = insertNEH(current_seq, j, order[i])
            cmax_tmp = makespan(tmp, tasks, machines_val)
            #print(tmp, cmax_tmp)
            if min_cmax > cmax_tmp:
                best_seq = tmp
                min_cmax = cmax_tmp
        current_seq = best_seq
    return current_seq, makespan(current_seq, tasks, machines_val)

def swap(list, tasks_val):
    a = ran.randrange(0, tasks_val)
    b = ran.randrange(0, tasks_val)
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


def chlodzenie1(T, u):
    return T*u

def sym_wyzarzanie1(tasks_val, tasks, machines_val, T_start, T_end):
    # pi0 = []
    # for i in range(0, tasks_val):
    #     pi0.append(i)
    # cmax0 = makespan(pi0, tasks, machines_val)
    pi0, cmax0 = neh(tasks, machines_val, tasks_val)
    pi = pi0
    cmax_old = cmax0
    T0 = T_start
    T = T0
    u = 0.99
    Tgr = T_end
    while (T >= Tgr):
        #piprim = swap(pi, tasks_val)
        piprim = insert(pi, tasks_val)
        cmax = makespan(piprim, tasks, machines_val)
        p = probability(cmax_old, cmax, T)
        s = ran.random()
        if p >= s:
            pi = piprim
            cmax_old = cmax
            T = chlodzenie1(T,u)
        else:
            T = chlodzenie1(T, u)
    return pi, cmax_old





#zmieniona funckja chlodzenia
def chlodzenie2(T, k, kmax):
    return T*(k/kmax)

def sym_wyzarzanie2(tasks_val, tasks, machines_val, T_start, T_end, iter_val):
    # pi0 = []
    # for i in range(0, tasks_val):
    #     pi0.append(i)
    # cmax0 = makespan(pi0, tasks, machines_val)
    pi0, cmax0 = neh(tasks, machines_val, tasks_val)
    pi = pi0
    cmax_old = cmax0
    T0 = T_start
    T = T0
    u = 0.99
    Tgr = T_end
    iter = 0
    max_iter = iter_val

    for i in range(0, max_iter):
        iter = iter + 1
        #piprim = swap(pi, tasks_val)
        piprim = insert(pi, tasks_val)
        cmax = makespan(piprim, tasks, machines_val)
        p = probability(cmax_old, cmax, T)
        s = ran.random()
        if p >= s:
            pi = piprim
            cmax_old = cmax
            T = chlodzenie2(T, iter, max_iter)
        else:
            T = chlodzenie2(T, iter, max_iter)
        #print(T)
        if T == 0:
            break
    return pi, cmax_old




def probability3(Cold, Cnew, Temp):
    prob = math.exp((Cold-Cnew)/Temp)
    return prob

#bez prawdopodobienstwa = 1
def sym_wyzarzanie3(tasks_val, tasks, machines_val, T_start, T_end):
    # pi0 = []
    # for i in range(0, tasks_val):
    #     pi0.append(i)
    # cmax0 = makespan(pi0, tasks, machines_val)
    pi0, cmax0 = neh(tasks, machines_val, tasks_val)
    pi = pi0
    cmax_old = cmax0
    T0 = T_start
    T = T0
    u = 0.99
    Tgr = T_end
    while (T >= Tgr):
        #piprim = swap(pi, tasks_val)
        piprim = insert(pi, tasks_val)
        cmax = makespan(piprim, tasks, machines_val)
        p = probability3(cmax_old, cmax, T)
        s = ran.random()
        if p >= s:
            pi = piprim
            cmax_old = cmax
            T = chlodzenie1(T,u)
        else:
            T = chlodzenie1(T, u)
    return pi, cmax_old



def probability4(Cold, Cnew, Temp):
    if Cnew < Cold:
        prob = 1
    if Cnew > Cold:
        prob = math.exp((Cold - Cnew) / Temp)
    return prob

#bez prawdopodobienstwa = 1
def sym_wyzarzanie4(tasks_val, tasks, machines_val, T_start, T_end):
    # pi0 = []
    # for i in range(0, tasks_val):
    #     pi0.append(i)
    # cmax0 = makespan(pi0, tasks, machines_val)
    pi0, cmax0 = neh(tasks, machines_val, tasks_val)
    pi = pi0
    cmax_old = cmax0
    T0 = T_start
    T = T0
    u = 0.99
    Tgr = T_end
    while (T >= Tgr):
        #piprim = swap(pi, tasks_val)
        piprim = insert(pi, tasks_val)
        cmax = makespan(piprim, tasks, machines_val)
        if cmax_old != cmax:
            p = probability4(cmax_old, cmax, T)
            s = ran.random()
            if p >= s:
                pi = piprim
                cmax_old = cmax
                T = chlodzenie1(T,u)
            else:
                T = chlodzenie1(T, u)
    return pi, cmax_old




#neh z najlepszymi ustawieniami
def sym_wyzarzanie_best(tasks_val, tasks, machines_val, T_start, T_end, pi0, cmax0, iter_val):
    # pi0 = []
    # for i in range(0, tasks_val):
    #     pi0.append(i)
    # cmax0 = makespan(pi0, tasks, machines_val)
    # pi0, cmax0 = neh(tasks, machines_val, tasks_val)
    pi = pi0
    cmax_old = cmax0
    T0 = T_start
    T = T0
    u = 0.99
    Tgr = T_end
    iter = 0
    max_iter = iter_val

    for i in range(0, max_iter):
        iter = iter + 1
        # piprim = swap(pi, tasks_val)
        piprim = insert(pi, tasks_val)
        cmax = makespan(piprim, tasks, machines_val)
        p = probability(cmax_old, cmax, T)
        s = ran.random()
        if p >= s:
            pi = piprim
            cmax_old = cmax
            T = chlodzenie2(T, iter, max_iter)
        else:
            T = chlodzenie2(T, iter, max_iter)
        # print(T)
        if T == 0:
            break
    return pi, cmax_old




# #wplyt funkcji chlodzenia
# print("--------------------------------------------------------------")
# print("Chlodzenie 1 ")
# best_seq, best_cmax = sym_wyzarzanie1(tasks_val, tasks, machines_val, 5000, 10)
# print (best_seq, best_cmax)
#
# print("Chlodzenie 2")
# best_seq, best_cmax = sym_wyzarzanie2(tasks_val, tasks, machines_val, 5000, 10, 1000)
# print (best_seq, best_cmax)


#wpływ ilości iteracji dla chłodzenia 2

# a_iter = [10, 100, 1000, 10000, 100000]
# cmax = 0
# for i in a_iter:
#     for j in range(0,4):
#         best_seq, best_cmax = sym_wyzarzanie2(tasks_val, tasks, machines_val, 5000, 10, i)
#         cmax = cmax + best_cmax
#     cmax = cmax /4
#     print(i, cmax)
#     cmax = 0


#wplyw odrzucnia prawdopodobienstwa = 1
# print("--------------------------------------------------------------")
# cmax = 0
# print("Prawdopodobeinstwo z 1 ")
# for k in range(0,4):
#     best_seq, best_cmax = sym_wyzarzanie1(tasks_val, tasks, machines_val, 5000, 10)
#     cmax = cmax + best_cmax
# cmax = cmax/4
# print (best_seq, cmax)
#
# cmax= 0
# print("Prawdopodobeinstwo bez 1 ")
# for k in range(0,4):
#     best_seq, best_cmax = sym_wyzarzanie3(tasks_val, tasks, machines_val, 5000, 10)
#     cmax = cmax + best_cmax
# cmax = cmax/4
# print (best_seq, cmax)


#wplyw odrzucnia prawdopodobienstwa gdy cmax=cmaxold
# print("--------------------------------------------------------------")
# cmax = 0
# print("Prawdopodobeinstwo z >=")
# for k in range(0,4):
#     best_seq, best_cmax = sym_wyzarzanie1(tasks_val, tasks, machines_val, 5000, 10)
#     cmax = cmax + best_cmax
# cmax = cmax/4
# print (best_seq, cmax)
#
# cmax= 0
# print("Prawdopodobeinstwo bez = ")
# for k in range(0,4):
#     best_seq, best_cmax = sym_wyzarzanie4(tasks_val, tasks, machines_val, 5000, 10)
#     cmax = cmax + best_cmax
# cmax = cmax/4
# print (best_seq, cmax)



#badanie wplytu Tstart i Tstop
# T_start = [5000, 10000]
# T_end = [1000]
#
# cmax = 0
# for i in T_start:
#     for j in T_end:
#         for k in range(0,4):
#             seq, c = sym_wyzarzanie1(tasks_val, tasks, machines_val, i, j)
#             cmax = cmax + c
#         cmax = cmax/4
#         cmax = 0
#         print("T_start: ", i, "T_stop:", j)
#         print(seq, c)




#Porownanie najlepszego SA z NEHem
start = 0
stop =0

start = time.perf_counter()
best_seqneh, best_cmaxneh = neh(tasks, machines_val, tasks_val)
stop = time.perf_counter()
czasneh = round((stop-start), 3)


start = time.perf_counter()
best_seqsa, best_cmaxsa = sym_wyzarzanie_best(tasks_val, tasks, machines_val,5000,10, best_seqneh, best_cmaxneh, 1000)
stop = time.perf_counter()
czassa = round((stop-start), 3)

print("--------------------------------------------------------------")
print("Algorytm NEH ")
print (best_seqneh, best_cmaxneh)
print("czas:", czasneh)
print("Algorytm SA ")
print (best_seqsa,  best_cmaxsa)
print("czas:", czassa)

