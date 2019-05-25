import json

with open('states.json') as f:
	data=json.load(f) # f.read()


for state in data['states']:
	del state['area_codes']

with open('new_states.json','w') as f:
	json.dump(data,f,indent=2) # f.write(json.dump(data,indent=2))