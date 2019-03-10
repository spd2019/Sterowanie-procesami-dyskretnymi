from prettytable import PrettyTable

figure =  PrettyTable()
figure.field_names = ["Sequence", "Makespan"]

def permute(x, index=0):
    if index+1 >= len(x):
        yield x
    else:
        for p in permute(x, index+1):
            yield p
        for i in range(index+1,len(x)):
            x[index], x[i]=x[i], x[index]
            for p in permute(x,index+1):
                yield p
            x[index], x[i]=x[i], x[index]

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

def bruteforce(tasks, machines_val, tasks_val):
    print("Starting bruteforce")
    t = []
    min_time = 1000
    for z in range(0, tasks_val):
        t.append(z)
    for p in permute(t):
        #print("order: {}".format(p))
        #print("makespan: {}".format(makespan(p, tasks, machines_val)))
        tmp = makespan(p, tasks, machines_val)
        figure.add_row([format(p), tmp ])
        if (tmp < min_time):
            min_time = tmp
            best_permute = format(p)
    print(figure)
    print("Min time:", min_time, "  for :", format(best_permute), "permutation")
    print("Bruteforce: DONE")
