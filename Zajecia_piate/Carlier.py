def get_b(U, pi, tab):
    p = 0
    for i in pi:
        r = tab[i][0]
        p = max(p, r) + tab[i][1]
        if U == p + tab[i][2]:
            j = i
    return j


def get_a(U, pi, b, tab):
    q = tab[b][2]
    mx = pi.index(b)
    for i in pi:
        p = 0
        r = tab[i][0]
        mi = pi.index(i)
        for a in range(mi, mx+1):
            p += tab[pi[a]][1]
        if U == r+p+q:
            return i


def get_c(pi,a,b,tab):
    flaga = 0
    a = pi.index(a)
    b = pi.index(b)
    for i in range(a, b+1):
        if tab[pi[i]][2] < tab[pi[b]][2]:
            j = pi[i]
            flaga = 1
    if flaga == 1:
        return j
    else:
        return []


