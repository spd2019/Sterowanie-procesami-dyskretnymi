import numpy as np

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
        max_time = 10
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
    order = sum_and_order(tasks_val, machines_val, tasks)  #wagi w kolejnosci nierosnocej
    print("order:", order)
    current_seq = [order[0]]
    for i in range(1, tasks_val):
        min_cmax = float("inf")
        for j in range(0, i + 1):
            tmp = insert(current_seq, j, order[i])
            cmax_tmp = makespan(tmp, tasks, machines_val)
            if min_cmax > cmax_tmp:
                best_seq = tmp
                min_cmax = cmax_tmp
        current_seq = best_seq

   # neh_acc(tasks, machines_val, tasks_val)
    return current_seq, makespan(current_seq, tasks, machines_val)



def neh_wm(tasks, machines_val, tasks_val):
    order = sum_and_order(tasks_val, machines_val, tasks)  # wagi w kolejnosci nierosnocej
    current_seq = [order[0]]
    for i in range(1, tasks_val):
        min_cmax = float("inf")
        for j in range(0, i + 1):
            tmp = insert(current_seq, j, order[i])
            #print("i", i)
            graf, graf_wag, cmax_tmp, sciezka = create_graph_LR(tmp, tasks, machines_val)
            cmax_tmp = makespan(tmp, tasks, machines_val)
            if min_cmax > cmax_tmp:
                best_seq = tmp
                min_cmax = cmax_tmp
                bestj = j
        current_seq = best_seq
        #print("bestj:", bestj)
        current_seq = IR1_mod(sciezka, graf, bestj, current_seq, tasks, machines_val)
       # print("sq:", current_seq)
    print("koniec nowy neh")
    return current_seq, makespan(current_seq, tasks, machines_val)


def create_graph_LR(seq, tasks, machines_val):
    tasks_val = len(seq)  #ilosc zadan
    graf = []
    for i in seq:
        graf.append(tasks[i])

    graf_wag = []
    for j in range(0, tasks_val):
        graf_wag.append([0]*machines_val)

    #print("graf:", graf)
   # print("new:", graf_wag)

    for i in range(0, len(graf)):
        if i == 0:
            for j in range(0, machines_val):
                if j==0:
                    graf_wag[i][j] = graf[i][j]
                else:
                    graf_wag[i][j] = graf[i][j] + graf_wag[i][j-1]

        else:
            for j in range(0, machines_val):
                if j==0:
                    graf_wag[i][j] = graf[i][j] + graf_wag[i-1][j] #tylko lewo
                else:
                    graf_wag[i][j] = graf[i][j] + max( graf_wag[i-1][j], graf_wag[i][j-1]) #lewo i gora

    Cmax = graf_wag[-1][-1]

    i = 0;
    j = 0;
    sciezka = []
    while (i !=len(graf)-1)or(j!=machines_val-1) :
        if graf_wag[len(graf)-i-1][machines_val-j-1]-graf[len(graf)-i-1][machines_val-j-1] == graf_wag[len(graf)-i-2][machines_val-j-1]:
            sciezka.append([len(graf)-i-1, machines_val-j-1])
            i = i+1

        elif graf_wag[len(graf)-i-1][machines_val-j-1]-graf[len(graf)-i-1][machines_val-j-1] == graf_wag[len(graf)-i-1][machines_val-j-2]:
            sciezka.append([len(graf)-i-1, machines_val-j-1])
            j = j+1
    sciezka.append([0, 0])

    #print("sciezka:", sciezka)

    #print("gw:",graf_wag)
    return graf, graf_wag, Cmax, sciezka


def create_graph_RL(seq, tasks, machines_val):
    print("ODWROTNY")
    tasks_val = len(seq)  #ilosc zadan
    graf = []
    for i in seq:
        graf.append(tasks[i])

    graf_wag = []
    for j in range(0, tasks_val):
        graf_wag.append([0]*machines_val)

    #print("graf:", graf)
    #print("new:", graf_wag)

    for i in range(1, len(graf)+1):
        if i == 0:
            for j in range(1, machines_val+1):
                if j==0:
                    graf_wag[-i][-j] = graf[-i][-j]
                else:
                    graf_wag[-i][-j] = graf[-i][-j] + graf_wag[-i][-j+1]

        else:
            for j in range(1, machines_val+1):
                if j==0:
                    graf_wag[-i][-j] = graf[-i][-j] + graf_wag[-i+1][-j] #tylko lewo
                else:
                   graf_wag[-i][-j] = graf[-i][-j] + max( graf_wag[-i+1][-j], graf_wag[-i][-j+1]) #lewo i gora

    Cmax = graf_wag[0][0]
    #print("gw:",graf_wag)
    return graf_wag, Cmax


def IR1_mod(sciezka, graf, bestj , seq, tasks, machines_val):
    #print(seq)
    #print("AAA",sciezka)
    #print(graf)
    najnowsze = 999
    for k in range(len(seq)):
        if bestj == seq[k]:
            najnowsze = k
    max_task = 0
    max_task_wsp = []
    for i in sciezka:
        if i[0] != najnowsze:
            #print(i)
            #print(graf[i[0]][i[1]])
            if max_task < graf[i[0]][i[1]]:
                max_task = graf[i[0]][i[1]]
                max_task_wsp = i

    seq_idx = seq[max_task_wsp[0]]
    #print("seq_idx",seq_idx)
    #print(seq)
    seq.remove(seq_idx)
    #print("seqar", seq)
    new_mincmax = 999
    for i in range(0, len(seq)+1):
        tmp = insert(seq, i, seq_idx)
        #print(i)
       # print(tmp)
        newcmax_tmp = makespan(tmp, tasks, machines_val)
        if new_mincmax > newcmax_tmp:
            new_seq = tmp
            new_mincmax = newcmax_tmp
    #print("newseq",new_seq)
    #print("new_min_cmax", new_mincmax)
    return new_seq



def neh_akceleracja(kolejnosc, obciazenie1, obciazenie2, tabela, element):
    Cmax = []
    for i in range(len(obciazenie2) + 1):
        temp = []
        C = []
        if i == 0:
            for j in range(len(tabela[element])):
                if j == 0:
                    temp.append(tabela[element][j])
                else:
                    temp.append(tabela[element][j] + temp[j - 1])
                C.append(temp[j] + obciazenie2[i][j])
            Cmax.append(max(C))
        elif i == len(obciazenie2):
            for j in range(len(tabela[element])):
                if j == 0:
                    temp.append(tabela[element][j] + obciazenie1[i - 1][j])
                else:
                    temp.append(tabela[element][j] + max(obciazenie1[i - 1][j], temp[j - 1]))
                C.append(temp[j])
            Cmax.append(max(C))
        else:
            for j in range(len(tabela[element])):
                if j == 0:
                    temp.append(tabela[element][j] + obciazenie1[i - 1][j])
                else:
                    temp.append(tabela[element][j] + max(obciazenie1[i - 1][j], temp[j - 1]))
                C.append(temp[j] + obciazenie2[i][j])
            Cmax.append(max(C))
    miejsce = Cmax.index(min(Cmax))
    kolejnosc.insert(miejsce, element)
    return kolejnosc, min(Cmax)
