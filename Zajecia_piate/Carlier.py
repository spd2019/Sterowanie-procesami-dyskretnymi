import operator

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


def Schrage(tasks):
    # print("Starting Schrage algorithm")

    sigma = []   #czesciowa kolejnosc skladajaca sie z uszeregowanych zadan
    Ng = []  # zadania gotowe do uszeregowania
    Nn = tasks.copy() # zadania nieuszeregowane
    t = min(Nn)[0]  # minimalny czas przygotowania
    Cmax = 0

    while (Ng !=[] or Nn!=[]):
        while(Nn !=[] and min(Nn)[0] <=t):
            j = Nn.index(min(Nn))
            Ng.append(Nn[j])
            Nn.pop(j)
        if Ng == []:
            t = min(Nn)[0]
        else:
            j = Ng.index(max(Ng, key=operator.itemgetter(2)))
            tmp = Ng[j]
            Ng.pop(j)
            sigma.append(tmp)
            t = t + tmp[1]
            Cmax = max(Cmax, t+tmp[2])
    return  sigma, Cmax


def Schrage_pmtn(tasks):
    # print("Starting Schrage pmtn algorithm")

    sigma = []  # czesciowa kolejnosc skladajaca sie z uszeregowanych zadan
    Ng = []  # zadania gotowe do uszeregowania
    Nn = tasks.copy()  # zadania nieuszeregowane
    t = 0
    Cmax = 0
    l = [0, 0, 0]  #aktualnie wykonywane zadanie

    while (Ng != [] or Nn != []):
        while (Nn != [] and min(Nn)[0] <= t):
            j = Nn.index(min(Nn))
            tmp = Nn[j]
            Ng.append(tmp)
            Nn.pop(j)
            if tmp[2] > l[2]:
                l[1] = t-tmp[0]
                t = tmp[0]
                if l[1] > 0:
                    Ng.append(l)
        if Ng == []:
             t = min(Nn)[0]
        else:
            i = Ng.index(max(Ng, key=operator.itemgetter(2)))
            j = Ng[i]
            Ng.pop(i)
            sigma.append(j)
            l = j
            t = t + j[1]
            Cmax = max(Cmax, t + j[2])
    return sigma, Cmax

def get_b(U, pi, tasks_val):
    p = 0
    for i in range(0, tasks_val):
        r = pi[i][0]
        p = max(p, r) + pi[i][1]
        if U == p + pi[i][2]:
            j = i
    return j

def get_a(U, pi, b, tasks_val):
    q = pi[b][2]
    for i in range(0, tasks_val):
        p = 0
        r = pi[i][0]
        for a in range(i, b+1):
            p += pi[a][1]
        if U == r+p+q:
            return i

def get_c(pi,a,b):
    flaga = 0
    for i in range(a, b+1):
        if pi[i][2] < pi[b][2]:
            j = i
            flaga = 1
    if flaga == 1:
        return j
    else:
        return []

def Carlier(tasks, tasks_val):
    pi, U = Schrage(tasks)
    global UB
    global pi_gw
    if U < UB:
        UB = U
        pi_gw = pi
    b = get_b(U, pi, tasks_val)
    a = get_a(U, pi, b, tasks_val)
    c = get_c(pi, a, b)
    if c == []:
        return
    K = []
    for i in range(c+1, b+1):
        K.append(i)
    Kr = []
    Kp = 0
    Kq = []
    for j in K:
        Kr.append(pi[j][0])
        Kp += pi[j][1]
        Kq.append(pi[j][2])
    Kr = min(Kr)
    Kq = min(Kq)
    Kh = Kr + Kp + Kq
    Kc = []
    for i in range(c, b+1):
        Kc.append(i)
    remember_r = pi[c][0]
    pi[c][0] = max(pi[c][0], Kr + Kp)
    Kcr = []
    Kcp = 0
    Kcq = []
    for j in Kc:
        Kcr.append(pi[j][0])
        Kcp += pi[j][1]
        Kcq.append(pi[j][2])
    Kcr = min(Kcr)
    Kcq = min(Kcq)
    Khc = Kcr + Kcp + Kcq
    ord, LB = Schrage_pmtn(tasks)
    LB = max(Kh, Khc, LB)
    if LB < UB:
        Carlier(tasks, tasks_val)
    pi[c][0] = remember_r
    remember_q = pi[c][2]
    pi[c][2] = max(pi[c][2], Kq+Kp)
    Kcr = []
    Kcp = 0
    Kcq = []
    for j in Kc:
        Kcr.append(pi[j][0])
        Kcp += pi[j][1]
        Kcq.append(pi[j][2])
    Kcr = min(Kcr)
    Kcq = min(Kcq)
    Khc = Kcr + Kcp + Kcq
    ord, LB = Schrage_pmtn(tasks)
    LB = max(Kh, Khc, LB)
    if LB < UB:
        Carlier(tasks, tasks_val)
    pi[c][2] = remember_q

data = [0,1,2,3,4,5,6,7,8]

for i in data:
    UB = 9999999
    plik = "data" + str(i) + ".txt"
    tasks_val, columns_val, tasks = read_data_2list(plik)
    Carlier(tasks, tasks_val)
    print("{} {}".format(plik, UB))
