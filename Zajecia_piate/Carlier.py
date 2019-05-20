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
