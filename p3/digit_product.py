'''
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    S = int(input())
    sum = 0
    N=1
    while S != 0:
        sum = N%10
        N = N + sum
        S = S/10
    print(N)

if __name__ == "__main__":
    main()
