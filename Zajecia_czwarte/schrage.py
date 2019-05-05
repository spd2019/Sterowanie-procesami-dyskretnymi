import numpy as np
import copy
import operator

def Schrage(tasks):
    # print("Starting Schrage algorithm")

    sigma = []   #czesciowa kolejnosc skladajaca sie z uszeregowanych zadan
    Ng = []  # zadania gotowe do uszeregowania
    Nn = copy.deepcopy(tasks)# zadania nieuszeregowane
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
            idx = Ng.index(max(Ng, key=operator.itemgetter(2)))
            j = Ng[idx]
            Ng.pop(idx)
            sigma.append(j)
            t = t + j[1]
            Cmax = max(Cmax, t+j[2])
    return  sigma, Cmax


def Schrage_pmtn(tasks):
    # print("Starting Schrage pmtn algorithm")

    sigma = []  # czesciowa kolejnosc skladajaca sie z uszeregowanych zadan
    Ng = []  # zadania gotowe do uszeregowania
    Nn = copy.deepcopy(tasks)  # zadania nieuszeregowane
    t = min(Nn)[0]  # minimalny czas przygotowania
    Cmax = 0
    l = [0, 0, 1000000000]

    while (Ng != [] or Nn != []):
        while (Nn != [] and min(Nn)[0] <= t):
            i = Nn.index(min(Nn))
            j = Nn[i]
            Ng.append(j)
            Nn.pop(i)
            if j[2] > l[2]:
                l[1] = t-j[0]
                t = j[0]
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

