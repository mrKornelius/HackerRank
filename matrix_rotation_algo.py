def solve(g, r):
    m,n = len(g), len(g[0])

    if m > n:
        g = list(map(list, zip(*g)))
        r = -r
    # print(*g, sep='\n')

    m,n = len(g), len(g[0])

    m1 = []
    for _ in range(len(g)):
        if len(g) == 1: 
            m1.append(g[0])
            break
        elif len(g) > 0:
            a, b = g[0], list(reversed(g[-1]))
            g = list(map(list,zip(*g[1:-1])))

            if g != []:
                c, d = list(reversed(g[0])), g[-1]
                g = list(map(list,zip(*g[1:-1])))
            else:
                c = d = []

            t = [*a,*d,*b,*c]
            r1 = r % len(t)
            t1 = t[r1:] + t[:r1]
            m1.append(t1)
        else:
            break    
    
    m1.reverse()
    # print('-----')
    # print(*m1, sep='\n')

    m2 = []
    for x in m1:
        if m2 == [] and m%2 == 0 and m < n:
            m2.append(x[:len(x)//2])
            m2.append(list(reversed(x[len(x)//2:])))
            # print(m2)
        elif m2 == [] and m%2 == 0 and m > n:
            m2.append(x[:len(x)//2])
            m2.append(list(reversed(x[len(x)//2:])))
            # m2 = list(map(list, zip(*m2)))
            # print(m2)
        elif len(x) == 1 or m2 == []:
            m2.append(x)
        else:
            # print(x)
            if m >= n:
                u, v =  len(m2[0]), len(m2) + 2
            else:
                u, v =  len(m2), len(m2[0]) + 2
            # print(f'{u=},{v=}')

            a,b,c,d = x[:v], x[v: v+u], list(reversed(x[v+u: 2*v+u])), list(reversed(x[2*v+u:]))
            # print(a,b,c,d)
            # print(m2)

            m2 = list(map(list, zip(*m2)))
            m2 = [d] + m2 + [b]
            # print(m2)
            m2 = list(map(list, zip(*m2)))
            m2 = [a] + m2 + [c]
            # print(m2)
    
    if m < n:
        m2 = list(map(list, zip(*m2)))

    # print('----')
    # print(*m2, sep='\n')
    for a in m2:
        print(*a)



            

def mat(m, n, fill=0):
    mat=[]
    for i in range(m):
        mat.append([])
        for j in range(n):
            if isinstance(fill, int):
                mat[-1].append(j+i*n)
            else:
                mat[-1].append(0)
    return mat


if __name__ == '__main__':

    g = [[0,0,0,0],
         [0,1,1,1],
         [0,1,2,2],
         [0,1,2,2],
         [0,1,1,1],
         [0,0,0,0]]

    g1 = [[0,0,0,0,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,2,2,2,1,0],
          [0,1,2,2,2,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0]]

    g2 = [[ 0, 1, 2, 3, 4],
          [ 5, 6, 7, 8, 9],
          [10,11,12,13,14],
          [15,16,17,18,19],
          [20,21,22,23,24]]

    print(*g, sep='\n')
    print('^- input -^')
    solve(g, r=4)
