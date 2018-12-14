print('-' * 65)
print('<Morbid Death Predictor> ')
print()
print('Description: This program asks you for your current age and tells you the year you will die (on average).')
print()

x = input('What is your age today? ')
x = int(x)

print('...thinking...')
print('...thinking...')

birthyear = 2018 - x

y = birthyear + 79

print('You will most likely die in the year ' + str(y))