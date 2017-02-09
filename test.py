
'''
a command line app that helps
users to keep track of events on the calendar
user is able to:
	create new calendar
	add an event
	see all events
	view last event on my calendar

'''
import calendar


def create_cal():

	cal = calendar.month(2017, 1)
	return cal

def get_user_choice():
	print '-' * 10
	print "Choose an Option Below:\n"
	print '[1] Add an Event'
	print '[2] See All Events'
	print '[3] View last Event\n'

	choice = raw_input( "Enter your Choice. \n") 

def add_event():
	if choice == '1':
		
	

	
	
	
def see_all():
	pass
def view_last_event():
	pass			
	

print create_cal()
print get_user_choice()

