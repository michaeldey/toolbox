import json

person = {
	'first_name': 'Mike',
	'isAlive': True,
	'age': 41,
	'address': {
		'street':'4301 Cromwell',
		'city': 'SLC',
		'postalCode': '84123-1234'
	},
	'hasMortgage':None
}

with open('person.json', 'w') as f: #writing a json object
	json.dump(person, f)

m = open ('person.json', 'r').read() #reading JSON object as string

print(m)

with open('person.json', 'r') as f: #reading a json object
	newPerson = json.load(f)

for item in newPerson:
	print(newPerson[item])

