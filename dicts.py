
#mapping of counties to abbreviation
counties = {
	'Nairobi': 'NRB',
	'Kisumu': 'KSM',
	'Mombasa': 'MSA',
	'Nyeri': 'NYR',
	'Machakos': 'MCK',
	}

#basic set of counties and cities in them
cities = {
	'NRB': 'Nairobi',
	'KSM': 'Kakamega',
	'NYR': 'Karatina',
	}	
#add more cities
cities['MCK'] = 'Kitui'
cities['MSA'] = 'Diani'

#print some cities
print '-' * 10
print "Nairobi's abbreviation is: ", counties['Nairobi']
print "Mombasa's abbreviation is: ", counties['Mombasa']

#print using county then cities dict
print '-' * 10
print "Machakos has: ", cities[counties['Machakos']]
print "Nyeri has: ", cities[counties['Nyeri']]

#print every county abbreviation
print '-' * 10
for state, abbrev in counties.items():
	print '%s is abbreviated %s ' %(counties, abbrev)

#print every city in county
print '-' * 10
for abbrev, city in cities.items():
	print '%s has the city %s '% (abbrev, city)

#print both at the same time
print '-' * 10
for county, abbrev in counties.items():
	print '%s county is abbreviated %s and has city %s ' % (county, abbrev, cities[abbrev])








