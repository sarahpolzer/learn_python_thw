#Part 1
things= ['a', 'b', 'c', 'd']
print(things[1])
things[1]= 'z' #reassignment
print(things[1])
things


#Part 2
stuff = {'name': 'Zed', 'age':39, 'height': 6*12 +2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])
stuff['city'] = "SF"
print(stuff['city'])

#Part 3
stuff[1] = "Wow"
stuff[2]= "Neato"
print(stuff[1])
print(stuff[2])


#Part 4
del stuff['city']
del stuff[1]
del stuff[2]
print (stuff)

#Part 5
states = {'Oregon': 'OR', 
        'Florida' : 'FL',
        'California' : 'CA',
        'New York' : 'NY',
        'Michigan' : 'MI'}
cities = {'CA' : 'San Francisco',
        'MI': 'Detroit',
        'FL' : 'Jacksonville'}
#add some more cities
cities['NY']= 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' *10)
print("NY State has:", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

#do it by using the states then cities dict
print('-'*10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

#print every state abbreviation
print('-' * 10 )
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get a abbreviation by state that might not be there
states = states.get('Texas')

if not state:
    print("Sorry, not Texas.")

#get a city with a default value
city= cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: {city}")
