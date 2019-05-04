import numpy as np

def Schrage(tasks_val, tasks):
    print("Starting Schrage algorithm")
    S = []
    for i in range(0, tasks_val):
        S.append(tasks[i][0])
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
    print("delta: ", delta)
    print("Cmax: ", cmax)
    return cmax
