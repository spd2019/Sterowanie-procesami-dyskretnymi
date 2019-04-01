import numpy as np

######### KLASYCZNY ###############################################
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
        max_time = 0
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

    return current_seq, makespan(current_seq, tasks, machines_val)


################AKCELERACJA ALGORTYTMU NEH #########################################3

def create_graph_LR(seq, tasks, machines_val):
    tasks_val = len(seq)  #ilosc zadan
    graf = []
    for i in seq:
        graf.append(tasks[i])

    graf_wag = []
    for j in range(0, tasks_val):
        graf_wag.append([0]*machines_val)

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

 #wyznaczanie najdłuższej ścieżki
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

    return sciezka, graf, graf_wag



def create_graph_RL(seq, tasks, machines_val):
    tasks_val = len(seq)  #ilosc zadan
    graf = []
    for i in seq:
        graf.append(tasks[i])

    graf_wag = []
    for j in range(0, tasks_val):
        graf_wag.append([0]*machines_val)

    for i in range(1, len(graf)+1):
        if i == 0:
            for j in range(1, machines_val+1):
                if j==0:
                    graf_wag[-i][-j] = graf[-
                    i][-j]
                else:
                    graf_wag[-i][-j] = graf[-i][-j] + graf_wag[-i][-j+1]

        else:
            for j in range(1, machines_val+1):
                if j==0:
                    graf_wag[-i][-j] = graf[-i][-j] + graf_wag[-i+1][-j] #tylko lewo
                else:
                   graf_wag[-i][-j] = graf[-i][-j] + max( graf_wag[-i+1][-j], graf_wag[-i][-j+1]) #lewo i gora

    Cmax = graf_wag[0][0]
    return graf_wag


def makespan_acc(order, weight_LR, weight_RL, tasks, new_elem):
    Cmax = []
    for i in range(len(weight_RL) + 1):
        temp = []
        C = []
        if i == 0: #wstawiam element na początek uszeregowania
            for j in range(len(tasks[new_elem])):
                if j == 0:
                    temp.append(tasks[new_elem][j])
                else:
                    temp.append(tasks[new_elem][j] + temp[j - 1])
                C.append(temp[j] + weight_RL[i][j])
            Cmax.append(max(C))
        elif i == len(weight_RL): #wstawiam element na koniec
            for j in range(len(tasks[new_elem])):
                if j == 0:
                    temp.append(tasks[new_elem][j] + weight_LR[i - 1][j])
                else:
                    temp.append(tasks[new_elem][j] + max(weight_LR[i - 1][j], temp[j - 1]))
                C.append(temp[j])
            Cmax.append(max(C))
        else: #wstawiam element w środek
            for j in range(len(tasks[new_elem])):
                if j == 0:
                    temp.append(tasks[new_elem][j] + weight_LR[i - 1][j])
                else:
                    temp.append(tasks[new_elem][j] + max(weight_LR[i - 1][j], temp[j - 1]))
                C.append(temp[j] + weight_RL[i][j])
            Cmax.append(max(C))
    miejsce = Cmax.index(min(Cmax))
    order.insert(miejsce, new_elem)
    return order, min(Cmax)




def neh_acc(tasks, machines_val, tasks_val):
    order = sum_and_order(tasks_val, machines_val, tasks)
    k=0;
    print("order:", order)
    for i in order:
        if k == 0:
            current_seq = [order[0]]
            path, graph, weight_LR = create_graph_LR(current_seq, tasks, machines_val)
            weight_RL = create_graph_RL(current_seq, tasks, machines_val)
            k+=1
        else:
            path, graph, weight_LR = create_graph_LR(current_seq, tasks, machines_val)
            weight_RL = create_graph_RL(current_seq, tasks, machines_val)
            current_seq, Cmax = makespan_acc(current_seq, weight_LR, weight_RL, tasks, i)

    print("Acc_seq:", current_seq)
    print("Acc_cmax: ", Cmax)
    return current_seq, Cmax


#################### MODYFIKACJA ###################################

def neh_wm(tasks, machines_val, tasks_val):
    order = sum_and_order(tasks_val, machines_val, tasks)
    k = 0;
    print("order:", order)
    for i in order:
        if k == 0:
            current_seq = [order[0]]
            path, graph, weight_LR = create_graph_LR(current_seq, tasks, machines_val)
            weight_RL = create_graph_RL(current_seq, tasks, machines_val)
            k += 1
        else:
            path, graph, weight_LR = create_graph_LR(current_seq, tasks, machines_val)
            weight_RL = create_graph_RL(current_seq, tasks, machines_val)
            current_seq, Cmax = makespan_acc(current_seq, weight_LR, weight_RL, tasks, i)

            MOD = NEH_IR1(path, graph, i , current_seq)
            if MOD!= -1:
                print(MOD)
                current_seq.remove(MOD)
                path, graph, weight_LR = create_graph_LR(current_seq, tasks, machines_val)
                weight_RL = create_graph_RL(current_seq, tasks, machines_val)
                current_seq, Cmax = makespan_acc(current_seq, weight_LR, weight_RL, tasks, MOD)

    print("Acc_seq:", current_seq)
    print("Acc_cmax: ", Cmax)
    return current_seq, Cmax



def NEH_IR1(sciezka, graf, i, kolejnosc):
    max = 0;
    index = 999;
    zadanie_odrzucone = 999
    for k in range(len(kolejnosc)):
        if i == kolejnosc[k]:
            zadanie_odrzucone = k
    for i in sciezka:
        if i[0] != zadanie_odrzucone:
            if graf[i[0]][i[1]] > max:
                max = graf[i[0]][i[1]]
                index = i[0]
    if index == 999:
        return -1
    return kolejnosc[index]