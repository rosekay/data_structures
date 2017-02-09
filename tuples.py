"""
	tuples are immutable are enclosed in parenthesis
	and when value is only one it must have a trailing comma
""" 
# rose = tuple('leather')
# print rose
# print rose[4]

'''
	Write a function called most_frequent that takes a string and prints the
	letters in decreasing order of frequency.
'''


def most_frequent(strings):
	str_dict = dict()
	for letter in strings:
		if letter in str_dict:
			str_dict[letter] +=1
		else:
			str_dict[letter] = 1
				
		sort_letters = sorted(str_dict.iteritems(), key=lambda (k, v): (v,k), reverse=True)
	
	
	return [x[0] for x in sort_letters]



print most_frequent("sally")





