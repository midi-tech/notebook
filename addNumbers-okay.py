# an "okay" implementation of addNumbers

def myInput(prompt='Enter Something: '):
    return input(prompt)

firstNumber = int(input('Please enter a number: '))
secondNumber = int(input('Please enter another number: '))

print(f'{firstNumber} + {secondNumber} = {firstNumber + secondNumber}')
