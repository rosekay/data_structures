#multiplication table for numbers upto (n)	

def mult_table():
	n = int(raw_input("Enter A Number to Print Its Multiplication Table:\n "))
	for x in range(1, n+1):
		print '-' * 30
		print "Multiplication Table For %s" % (x)
		print '-' * 30
		for y in range(1, n+1):
			times = x * y
			print "{:3} * {:3} = {:3}".format(x, y, times)
print mult_table()
