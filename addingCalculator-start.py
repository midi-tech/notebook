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
        

def getInput(prompt='Please enter something: '):
	while True:
		entered = input(prompt)

		print(f'entered: {entered}')

		if entered == "":
			print("entered an empty string...done")
			return None

		if entered == "c":
			print("entered clear command")
			return entered

		try:
			asInt = int(entered)
			print(f'"{entered}" is a number, thank you!')
			return int(entered)

		except ValueError:
			print(f'\n"{entered}" is not a number, "c", or ""...try again!\n')
        

#######################

value = 0
done = False

while not done:
	entered = getInput()

	# entered will be one of 3 things
	# a number
	# a None value
	# a "c"

	if entered is None:
		done = True
		continue

	if entered == "c":
		# what do I do here???
		value = 0
		print(value)
		continue

	print('you entered: ', entered)

	value = value + entered

	print(value)

print('Goodbye!')
