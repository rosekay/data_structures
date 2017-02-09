
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
class calendarApp():
	events = ''
	my_event = {dd: events}
	event_list = []

	#Title message
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
		
		
		print "On %s/%s/%s: %s " % (dd, mm, yy, events)


	#See all events	
	def see_all():
		event_list = []
		for event in my_event:
			event_list.append(events)
		print event_list

		
	#view last event	
	def view_last_event():
		return event_list[-1]			
		

	title()
	get_user_choice()
	add_event()
	see_all()
	view_last_event()

