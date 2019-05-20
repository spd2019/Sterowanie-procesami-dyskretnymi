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

def get_c(pi, a, b):
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
    UB = float("inf")
    if U < UB:
        UB = U
        pi_gw = pi
    b = get_b(U, pi, tasks_val)
    a = get_a(U, pi, b, tasks_val)
    c = get_c(pi, a, b)
    if c == []:
        return pi_gw
    K = []
    for i in range(c+1, b+1):
        K.append(i)
    print(K)
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
    remember_r = pi[c][0]
    pi[c][0] = max(pi[c][0], Kr + Kp)
    ord, LB = Schrage_pmtn(tasks)
    LB = max(Kh, Kh+pi[c][0]+pi[c][1]+pi[c][2], LB)
    if LB < UB:
        Carlier(tasks, tasks_val)
    pi[c][0] = remember_r
    remember_q = pi[c][2]
    pi[c][2] = max(pi[c][2], Kq+Kp)
    ord, LB = Schrage_pmtn(tasks)
    LB = max(Kh, Kh + pi[c][0] + pi[c][1] + pi[c][2], LB)
    if LB < UB:
        Carlier(tasks, tasks_val)
    pi[c][2] = remember_q
