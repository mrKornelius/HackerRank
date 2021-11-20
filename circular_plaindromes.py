import random
import time
import sys
import cProfile

sys.setrecursionlimit(10000)

mem = {}
def solve(s):
    results = []

    for _ in range(len(s)):
        results.append(palin(s))
        s = s[1:] + s[:1]
    return results

def palin(s):
    i = j = k = 0

    p = 1
    mx = 0
    while k < len(s):
        i -= 1
        j += 1
        if i < 0 or j >= len(s) or s[i] != s[j]:
            mx = max(mx, p)
            k += 1
            i = j = k
            p = 1
        else: # s[i] == s[j]:
            p += 2
        

    i = k = 0
    j = i +1
    p = 2
    while k < len(s):
        i -= 1
        j += 1
        if i < 0 or j >= len(s) or s[i] != s[j]:
            mx = max(mx, p)
            k += 1
            i = k
            j = i + 1
            p = 2
        else: # s[i] == s[j]:
            p += 2


    return mx



if __name__ == '__main__':    
    pr = cProfile.Profile()
    pr.enable()

    tic = time.perf_counter()
    x = solve('aaaaabbbbaaaa')
    print(x)
    assert x == [12,12,10,8,8,9,11,13,11,9,8,8,10], 'error'

    t = ''.join(['abc'[random.randrange(3)] for _ in range(2000)])
    print(solve(t))

    toc = time.perf_counter()
    print(f'Elapsed time: {toc-tic:.04f}s')
    
    pr.disable()
    pr.print_stats(sort='cumtime')
    

