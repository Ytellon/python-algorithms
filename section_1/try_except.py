# simple mode

number = input('Ill double it for you. Give me a number: ')

number_float = float(number)
print(f'The double of {number} is {number_float * 2:.2f}')

## using try except

try:
    number = input('Ill double it for you. Give me a number: ')
    number_float = float(number)
    print(f'The double of {number} is {number_float * 2:.2f}')
except:
    print('You did not enter a number')


