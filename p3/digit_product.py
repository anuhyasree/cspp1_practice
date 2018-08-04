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
    int_input = int(input())
    sum = 0
    while int_input > 0:
        sum = sum + int_input
        int_input = int_input%10
    print(sum)

if __name__ == "__main__":
    main()
