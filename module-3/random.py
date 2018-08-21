def rev(m):
    n = m[::-1]
    for [i,j] in enumerate(n):
        if isinstance(j,list):
            n[i] = j[::-1]
    return n
def main(): 
    n = input()
    l = []
    for _ in range(int(n)):
        k = input()
        k = k.split(',')
        l.append(k)
    print(l)
    print(rev(l))
if __name__ == '__main__':
    main()
