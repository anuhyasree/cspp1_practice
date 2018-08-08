#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given
#testList = [1, -4, 8, -9] into [1, 4, 8, 9]


def apply_to_each(L, f):
    for l_val in enumarate(L):
    	L(l_val)= apply_to_each(L(l_val))

def main():
    data = input()
    data = data.split()
    list1 = []
    for j in l:
        list1.append(int(j))
    apply_to_each(list1, abs)
if __name__ == "__main__":
    main()
