toChange = open('./queries/insert_coordinates.sql','r').read()
toSave = open('./queries/insert_coordinates_v2.sql','a')

print(toChange)

for line in toChange.split('\n'):
	output = line.split(' AND `postcode`')
	toSave.write(output[0] + '),CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL);\n')