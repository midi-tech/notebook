# a "good" implementation of addNumbers

firstNumber = None

while firstNumber is None:
    entered = input('Please enter a number: ')

    print(f'entered: {entered}')

    if entered.isdigit():
        print(f'"{entered}" is a number, thank you!')
        firstNumber = int(entered)
    else:
        print(f'\n"{entered}" is not a number...try again!\n')

secondNumber = None

while secondNumber is None:
    entered = input('Please enter another number: ')

    print(f'entered: {entered}')

    if entered.isdigit():
        print(f'"{entered}" is a number, thank you!')
        secondNumber = int(entered)
    else:
        print(f'\n"{entered}" is not a number...try again!\n')

# we now know that we have two numbers
print(f'{firstNumber} + {secondNumber} = {firstNumber + secondNumber}')
