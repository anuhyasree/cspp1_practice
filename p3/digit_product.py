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
    s = int(input())
    sum = 1
    n = 1
    while s != 0:
        sum = n % 10
        n = n + sum
        s = s/10
    print(n)

if __name__ == "__main__":
    main()
