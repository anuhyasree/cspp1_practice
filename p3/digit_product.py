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
    s_p = int(input())
    sum_p = 1
    n_p = 0
    while s_p != 0:
        n_p = s_p % 10
        sum_p = sum_p * n_p
        s_p = s_p / 10
    print(n_p)
if __name__ == "__main__":
    main()
