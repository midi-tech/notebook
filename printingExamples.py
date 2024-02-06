# The following are all ways to call the print() function with parameters:

string = 'Hello'
number = 42

# as a list of parameters
print(string, number)

# with the sep and end parameters
print(string, number, sep=' ', end='\n')

# as a single string created with the + operator
print(string + ' ' + str(number))

# with the .format() method
print('{} {}'.format(string, number))

# with f-strings ('formatted strings')
print(f'{string} {number}')

# with f-strings and quotes
print(f'"{string} {number}"')

# with f-strings and quotes (reversed)
print(f"'{string} {number}'")

# writing to a file with the file parameter
with open('output.txt', 'w') as file:
    print(string, number, file=file)

# reading from that same file
with open('output.txt', 'r') as file:
    print(file.read())

# appending to a file
with open('log.txt', 'a') as file:
    print(f'{string} {number}', file=file)