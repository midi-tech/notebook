# a "better" implementation of addNumbers

def getNumber():
    while True:
        entered = input('Please enter a number: ')

        print(f'entered: {entered}')

        if entered.isdigit():
            print(f'"{entered}" is a number, thank you!')
            return int(entered)
        
        else:
            print(f'\n"{entered}" is not a number...try again!\n')
        

firstNumber = getNumber()
secondNumber = getNumber()

# we now know that we have two numbers
print(f'{firstNumber} + {secondNumber} = {firstNumber + secondNumber}')
