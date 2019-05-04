import numpy as np
import copy

def Schrage(tasks_val, tasks):
    print("Starting Schrage algorithm")


    sigma = []   #czesciowa kolejnosc skladajaca sie z uszeregowanych zadan
    Ng = []  # zadania gotowe do uszeregowania
    Nn = copy.deepcopy(tasks)# zadania nieuszeregowane
    R = copy.deepcopy(Nn[:,0])
    t = min(Nn[:,0])  # minimalny czas przygotowania
    print(t)
    i = 1


    while ( Ng != [] or Nn != [] ):
        while ( Nn != []  and  min(Nn[:,0]) <= t):
            Qnn = copy.deepcopy(Nn[:,0])
            j = np.argmin(Qnn)
            print("j = ",j)

            Ng.append(Nn[j,:])
            Nn = np.delete(Nn, (j), axis=0)
            #print("Ng: ", Ng)
            #print("Nn: ", Nn)
            #print("S: ", S)
        if Ng == []:
            t = min(Nn[:,0])
        else:

            j = np.argmax(Ng[:,0])
            Ng = np.delete(Ng, (j), axis=0)
            sigma[i] = j
            print("sigma = ", sigma)
            i = i+1
            t = t+tasks[i][1]
            cmax = max(cmax, t+tasks[j][2])
    print("sigma: ", sigma)
    print("Cmax: ", cmax)
    return cmax
