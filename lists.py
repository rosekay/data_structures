#list methods applied

list_a = [15, 13.56, 200.0, -34,-1]
list_b = ['a', 'b', 'g',"henry", 7]

def list_max_min(price):
	#list comprehension
		return [num for num in price if num == min(price) or num == max(price)]


def list_reverse(price):
	#reverse the list
	price.reverse()
	return price

def list_count(price, num):
	#checks whether an element occurs in a list
	return price.count(num)

def list_odd_position(price ):
	#returns the elements on odd positions in a list
	return [num for num in price if price.index(num) % 2 != 0]

def list_total(price):
	#computes the running total of a list

	#simple version 
	# return sum(price)

	#for loop
	total = 0
	for num in price:
		total += num
	return total

def list_concat(price, new_price):
	#concatenates two lists together
	if type(new_price) == list:
		price.append(new_price)
		return price
	else:
		return "Not a list"	
	

def list_merge_sort(price, new_price):
	#merges two sorted lists into a sorted list
	price.append(new_price)
	return sorted(price)


print list_max_min(list_a)
print list_reverse(list_a)
print list_count(list_a, -34)
print list_odd_position(list_a)
print list_total(list_a )
print list_concat(list_a, list_b)
print list_merge_sort(list_a, list_b)

	

