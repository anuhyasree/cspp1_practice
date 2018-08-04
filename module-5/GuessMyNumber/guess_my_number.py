"""Guess My Number Exercise"""
def main():
    """def"""
print('Please think of a number between 0 and 100!')
LOW = 0
HEIGH = 100
ANS = (LOW + HEIGH) // 2
while True:
    USER = input('Is your secret number ' + str(ANS) + '\n'
                 + 'Enter "h" to indicate the guess is too high. '
                 + 'Enter "l" to indicate the guess is too low. '
                 + 'Enter "c" to indicate I guessed correctly. ')
    if USER == 'h':
        LOW = ANS
    elif USER == 'l':
        HEIGH = ANS
    elif USER == 'c':
        print('Game over. Your secret number was: ' + str(ANS))
        break
    else:
        print('Sorry, I did not understand your input.')
    ANS = (LOW + HEIGH) // 2
if __name__ == "__main__":
    main()
