# a "better" implementation of addNumbers

def getNumber(prompt='Please enter a number: '):
    while True:
        entered = input(prompt)

        print(f'entered: {entered}')

        if entered.isdigit():
            print(f'"{entered}" is a number, thank you!')
            return int(entered)
        
        else:
            print(f'\n"{entered}" is not a number...try again!\n')
        

firstNumber = getNumber()
secondNumber = getNumber('Please enter another number: ')

# we now know that we have two numbers
print(f'{firstNumber} + {secondNumber} = {firstNumber + secondNumber}')
