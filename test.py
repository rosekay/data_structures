
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

#create new calendar
def title():
	print '-' * 10
	print "Calendar App."
	 

	

#Get user choice 
def get_user_choice():
	print '-' * 10
	print "Choose an Option Below:\n"
	print '[1] Add an Event'
	print '[2] See All Events'
	print '[3] View last Event\n'

	

#Add an event
def add_event():
	print '-' * 10

	choice = raw_input( "Enter your Choice. \n") 
	if choice == '1':
		mm = int(raw_input('Enter Month: \n'))
		yy = int(raw_input('Enter Year: \n'))
		dd = int(raw_input('Enter Day: \n'))

		my_cal = calendar.month(yy, mm)
		print my_cal

	event = raw_input(" Add Event: \n")
	events = event.title()

	my_event = {dd: events}
	print "On %s/%s/%s: %s " % (dd, mm, yy, events)
		


def see_all():
	
	pass
def view_last_event():
	pass			
	

# title()
# get_user_choice()
add_event()

