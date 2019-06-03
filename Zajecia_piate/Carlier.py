import operator
import time
import time
import datetime
import threading

from Zajecia_piate import read_data, schrage


# Wyznacza zadanie, które jest pierwsze na ścieżce krytycznej#
# zadanie najbliższe w kolejności #pi#, takie że nie występują przestoje w pracy maszyny
# między tym zadaniem oraz zadaniem #b#  #
def get_a(U, pi, tasks, b):
    q = tasks[b][2]
    idx_b = pi.index(b)
    for val in pi:
        p = 0
        r = tasks[val][0]
        mi = pi.index(val)
        for a in range(mi, idx_b+1):
            p += tasks[pi[a]][1]
        if U == r+p+q:
            return val

# Wyznacza zadanie, które jest ostatnie na ścieżce krytycznej #
# zadanie najdalsze w kolejności #pi#, takie że suma czasu jego zakończenia i dostarczenia jest równa Cmax #
def get_b(U, pi, tasks):
    p = 0
    for val in pi:
        r = tasks[val][0]
        p = max(p, r) + tasks[val][1]
        if U == p + tasks[val][2]:
            j = val
    return j


# Zadanie krytyczne #
# Zadanie najdalsze w kolejności #pi#, takie że jego czas dostarczenia jest mniejszy od czasu dostarczenia zadania b#
def get_c(pi, tasks, a, b):
    flag = 0
    a = pi.index(a)
    b = pi.index(b)
    for val in range(a, b+1):
        if tasks[pi[val]][2] < tasks[pi[b]][2]:
            j = pi[val]
            flag = 1
    if flag == 1:
        return j
    else:
        return []


# Podstawowy algorytm #
def Carlier(tasks):
    global UB
    global n
    pi, U = schrage.Schrage(tasks)
    #print(wejscie, poziom, "\n")
    if U < UB:
        UB = U
    b = get_b(U, pi, tasks)
    a = get_a(U, pi, tasks, b)
    c = get_c(pi, tasks, a, b)
    if c == []:
        return UB, tasks
    K = []

    # TO JEST ŹLE
    # for i in range(c+1, b+1):
    #     K.append(i)

    for i in pi[pi.index(c)+1:pi.index(b)+1]:
        K.append(i)

    rK = []
    qK = []
    pK = 0
    for val in K:
        rK.append(tasks[val][0])
        qK.append(tasks[val][2])
        pK += tasks[val][1]
    qK = min(qK)
    rK = min(rK)
    rpq = [rK, pK, qK]
    LB = schrage.Schrage_pmtn(tasks)
    remember_R = tasks[c][0]
    tasks[c][0] = max(tasks[c][0], rK+pK)
    hkc = min(rK, tasks[c][0])+pK+tasks[c][1]+min(qK, tasks[c][2])
    LBL = max(sum(rpq), LB, hkc)
    if LBL < UB:
        Carlier(tasks)
    tasks[c][0] = remember_R
    remember_Q = tasks[c][2]
    tasks[c][2] = max(tasks[c][2], qK + pK)
    hkc = min(rK, tasks[c][0]) + pK + tasks[c][1] + min(qK, tasks[c][2])
    LBP = max(sum(rpq), hkc, LB)
    if LBP < UB:
        Carlier(tasks)
    tasks[c][2] = remember_Q
    return UB



def Carlier_Elim(tasks):
    global UB
    global n
    pi, U = schrage.Schrage(tasks)
    if U < UB:
        UB = U
    b = get_b(U, pi, tasks)
    a = get_a(U, pi, tasks, b)
    c = get_c(pi, tasks, a, b)
    if c == []:
        return UB, tasks
    K = []

    for i in pi[pi.index(c)+1:pi.index(b)+1]:
        K.append(i)

    rK = []
    qK = []
    pK = 0
    for i in K:
        rK.append(tasks[i][0])
        qK.append(tasks[i][2])
        pK += tasks[i][1]
    qK = min(qK)
    rK = min(rK)
    rpq = [rK, pK, qK]
    LB = schrage.Schrage_pmtn(tasks)

    #####ELIMINACJA#####
    #Wyznaczanie zbioru L
    L = []
    for i in pi[0:pi.index(c)]:
        L.append(i)
    for i in pi[pi.index(b)+1:]:
        L.append(i)
    for i in L:
        if UB - sum(rpq) >= tasks[i][1]:
            L.pop(L.index(i))
    #Sprawdzenie warunków
    # sprawdzamy 2 warunki i jeśli są spełnione to aktualizujemy tablicę zadań #
    for i in L:
        if UB <= tasks[i][0] + tasks[i][1] + rpq[1] + tasks[b][2]: #jeśli ri + pi + pK + qb >=UB
            # i musi być wykonuwane ZA wszyztkimi zadaniami K i wtedy:
            tasks[i][0] = max(tasks[i][0], rpq[0]+rpq[1]) #max z {ri, rK+pK}
        if UB <= rpq[0] + tasks[i][1] + rpq[1] + tasks[i][2]: #jeśli rK + pi + pK + qi >=UB
            # i musi być wykonuwane PRZED wszyztkimi zadaniami K i wtedy:
            tasks[i][2] = max(tasks[i][2], rpq[2]+rpq[1])
    ### KONIEC ELIMINACJI ####

    remember_R = tasks[c][0]
    tasks[c][0] = max(tasks[c][0], rK+pK)
    hkc = min(rK, tasks[c][0])+pK+tasks[c][1]+min(qK, tasks[c][2])
    LBL = max(sum(rpq), LB, hkc)
    if LBL < UB:
        Carlier_Elim(tasks)
    tasks[c][0] = remember_R
    remember_Q = tasks[c][2]
    tasks[c][2] = max(tasks[c][2], qK + pK)
    hkc = min(rK, tasks[c][0]) + pK + tasks[c][1] + min(qK, tasks[c][2])
    LBP = max(sum(rpq), hkc, LB)
    if LBP < UB:
        Carlier_Elim(tasks)
    tasks[c][2] = remember_Q
    return UB

print("ALGORYTM PODSTAWOWY")

data = [0,1,3,4]
correct = [228, 3026, 3309, 3191]
tmp = 0
for i in data:
    UB = 9999999
    plik = "data" + str(i) + ".txt"
    tasks_val, columns_val, tasks = read_data.read_data_2list(plik)
    start = time.perf_counter()
    UB = Carlier(tasks)
    stop = time.perf_counter()
    czas = round((stop-start), 5)
    print("{} {}  Correct: {}  Czas: {}".format(plik, UB, correct[tmp], czas))
    tmp +=1


print("ALGORYTM Z ELIMINACJĄ")


data = [0,1,2,3,4,5,6,7,8]
correct = [228, 3026, 3665 ,3309, 3191, 3618, 3446, 3821, 3634]

for i in data:
    UB = 9999999
    plik = "data" + str(i) + ".txt"
    tasks_val, columns_val, tasks = read_data.read_data_2list(plik)
    start = time.perf_counter()
    UB = Carlier_Elim(tasks)
    stop = time.perf_counter()
    czas = round((stop-start), 5)
    print("{} {}  Correct: {}  Czas: {}".format(plik, UB, correct[i], czas))



