import random

def solve(s):
    results = []

    # check palindromes for each rotation.
    # More effective to check s+s instead and skip the rotation
    # but harder to know the length of the palindrom in each word 
    for _ in range(len(s)):
        results.append(palin(s))
        s = s[1:] + s[:1]

    return results

# Basically check palindromes from each starting point, i, in s, in two
# ways, first odd length palindromes and then even length. Start with
# two pointers l and r pointing at i, then try to expand outwards from
# i and check if we still have a palindrome.
def palin(s):
    mx = 0
    le = len(s)
    for i in range(le):

        # odd length pal.
        l, r = i, i
        while l >= 0 and r < le and s[l] == s[r]:     
            if r-l+1 > mx:
                mx = r-l+1
            l -= 1
            r += 1
        
        # even length pal.
        l, r = i, i+1
        while l >= 0 and r < le and s[l] == s[r]:     
            if r-l+1 > mx:
                mx = r-l+1
            l -= 1
            r += 1
        
    return mx


if __name__ == '__main__':    
    x = solve('aaaaabbbbaaaa')
    print(x)
    assert x == [12,12,10,8,8,9,11,13,11,9,8,8,10], 'error 1'

    x = solve('eededdeedede')
    print(x)
    assert x == [5,7,7,7,7,9,9,9,9,7,5,4], 'error 2'

    x = solve('cacbbba')
    print(x)
    assert x == [3,3,3,3,3,3,3], 'error 3'

    x = solve('abcdefgh')
    print(x)
    assert x == [1,1,1,1,1,1,1,1], 'error 4'

    x = solve('aaaaaaaa')
    print(x)
    assert x == [8,8,8,8,8,8,8,8], 'error 5'

    t = ''.join(['abc'[random.randrange(2)] for _ in range(1000)])
    x = solve(t)
    print(x)

    

