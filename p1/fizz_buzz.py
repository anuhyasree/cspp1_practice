'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    nu_m = int(input())
    for nu_m in range(1,nu_m):
    	if nu_m%3 and nu_m%5:
    		print("Fizz")
    		print("Buzz")
    	elif nu_m%3:
    		print("Fizz")
    	else:
    		print("Buzz")


if __name__ == "__main__":
    main()
