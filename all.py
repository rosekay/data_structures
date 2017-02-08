
#programming challenges today 

#function that prints hello world to the screen
def hello():
	print '-' * 10
	return'Hello World!'

#function that asks user for name and if name is alice or bob it prints out their name
def user_name():
	print '-' * 10
	name = raw_input('Please Enter your Name: \n')
	names = name.title()
	
	if names == 'Alice' or names == 'Bob':
		return 'Nice to know you %s!' %(names)
	return 'Nice to know you!'

def user_number():
	'''
		function that asks user for number(n) and prints the sum of numbers 
		between 0-n but only for numbers divisible by both 3 and 5
	'''
	print '-'* 10
	num = int(raw_input('Enter Any Number \n'))
	total = 0
	new_list = []

	for elem in range(0, num+1):
		if elem % 3 == 0 or elem % 5 == 0:
			new_list.append(elem)
			
	new_sum = sum(new_list)
	return 'The Total Sum of FizzBuzz Numbers From 0 to %s Is %s: '% (num, new_sum)

def sum_product():
	'''
		function that asks user for a number(n) then asks user to choose whether to find 
		sum or product of 1-n
	'''	
	print '-' * 10
	num = int(raw_input('Enter Another Number \n'))

	choice = ''
	print "Choose A Method Below"
	print "[1] to get Sum of Numbers upto %s" % (num)
	print "[2] to get Product of Numbers upto %s \n" % (num) 
	
	choice = raw_input("Enter your choice. \n")

	while choice!= 0:
		item_list = []
		if choice == '1':
			for item in range(0, num+1):
				item_list.append(item)

				num_sum = sum(item_list)
			return "The Sum of Numbers From 0 to %s Is %s : "% (num, num_sum)
			

		elif choice == '2':
			product = 1
			for item in range(1, num+1):
				product *= item
			return "The Product of Numbers From 0 to %s Is \n %s:" %(num, product)	
		return "Not a valid choice."
#play again
def play_again():
	print '-' * 10
	next = raw_input('Do you want to play again? y/n \n')
	if next == "y":
		user_number()
		sum_product()
	else:
		return end_text()
	

#ending note
def end_text():
	print '-' * 10
	return "GoodBye!"		
				


print hello()	
print user_name()
print user_number()
print sum_product()
print play_again()
print end_text()
