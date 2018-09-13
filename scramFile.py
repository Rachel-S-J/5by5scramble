"this file takes a user input string and converts it into a display of 5x5 POW code"

  x = input("Enter a statement to be scrambled")
s = x.lower()


def horiz(i):
        if s[i] == 'a' or s[i] == 'f' or s[i] == 'l' or s[i] == 'q' or s[i] == 'v':
            print('.   .')
        elif s[i] == 'b' or s[i] == 'g' or s[i] == 'm' or s[i] == 'r' or s[i] == 'w':
            print('.   ..')
        elif s[i] == 'c' or s[i] == 'k' or s[i] == 'h' or s[i] == 'n' or s[i] == 's' or s[i] == 'x':
            print('.   ...')
        elif s[i] == 'd' or s[i] == 'i' or s[i] == 'o' or s[i] == 't' or s[i] == 'y':
            print('.   ....')
        elif s[i] == 'e' or s[i] == 'j' or s[i] == 'p' or s[i] == 'u' or s[i] == 'z':
            print('.   .....')

for i in range(0, len(s)):
        if s[i] == 'a' or s[i] == 'b' or s[i] == 'c' or s[i] == 'k' or s[i] == 'd' or s[i] == 'e':
            horiz(i)
        elif s[i] == 'f' or s[i] == 'g' or s[i] == 'h' or s[i] == 'i' or s[i] == 'j':
            print('.')
            horiz(i)
        elif s[i] == 'l' or s[i] == 'm' or s[i] == 'n' or s[i] == 'o' or s[i] == 'p':
            print('.')
            print('.')
            horiz(i)
        elif s[i] == 'q' or s[i] == 'r' or s[i] == 's' or s[i] == 't' or s[i] == 'u':
            print('.')
            print('.')
            print('.')
            horiz(i)
        elif s[i] == 'v' or s[i] == 'w' or s[i] == 'x' or s[i] == 'y' or s[i] == 'z':
            print('.')
            print('.')
            print('.')
            print('.')
            horiz(i)
        else:
            print(' ')
