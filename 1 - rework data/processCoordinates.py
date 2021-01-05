import requests,csv,json,time

addressQuery = open('./queries/insert_addresses.sql','a')
coordinateQuery = open('./queries/insert_coordinates.sql', 'a')
mapQuery = open('./queries/insert_maps.sql','a')

coordinateDict = dict()
with open('data/coordinates.csv', encoding="utf8") as csvFile:
	readerResult = csv.DictReader(csvFile, delimiter=';', quotechar='"')
	for line in readerResult:
		coordinateDict[line['id']] = line

done = open('./logs/gps_done.txt','r').read()
saveToDone = open('./logs/gps_done.txt','a')
runCount = 0

for gps in coordinateDict.values():
	if runCount > 4951:
		print("4950 requests is gehaald. Stop")
		break

	lat = gps['latitude']
	lon = gps['longitude']
	lat5 = (lat.split('.'))[0] + '.' + (lat.split('.'))[1][0:5]
	lon5 = (lon.split('.'))[0] + '.' + (lon.split('.'))[1][0:5]
	
	if (lat5 + '_' + lon5) in done:
		print(lat + ', ' + lon + ' zit al in het systeem.')
		continue
	else:
		print('opzoeken: ' + lat + ', ' + lon)

	url = "https://eu1.locationiq.com/v1/reverse.php"
	apikey = 'pk.36d3af127c87a9c91e5fd69631e4647e'

	lat5 = (lat.split('.'))[0] + '.' + (lat.split('.'))[1][0:5]
	lon5 = (lon.split('.'))[0] + '.' + (lon.split('.'))[1][0:5]

	data = {
		'key': apikey,
		'lat': lat,
		'lon': lon,
		'format': 'json'
	}

	response = requests.get(url, params=data)
	time.sleep(1)
	returndata = json.loads(response.text)

	iso_code = returndata['address']['country_code']
	description = returndata['display_name'].replace("'","\'")
	if 'road' in returndata['address']:
		road = returndata['address']['road'].replace("'","\'")
	else:
		road = ''
	if 'postcode' in returndata['address']:
		postcode = returndata['address']['postcode']
	else:
		postcode = ''
	if 'suburb' in returndata['address'] and 'neighbourhood' in returndata['address'] and 'city' in returndata['address']:
		if returndata['address']['city'] == returndata['address']['suburb']:
			part = returndata['address']['neighbourhood'].replace("'","\'")
		elif 'suburb' in returndata['address']:
			part = returndata['address']['suburb'].replace("'","\'")
		else:
			part = ''
		
	elif 'county' in returndata['address']:
		part = returndata['address']['county'].replace("'","\'")
	else:
		part = ""
	if 'city' in returndata['address']:
		city = returndata['address']['city'].replace("'","\'")
	elif 'town' in returndata['address']:
		city = returndata['address']['town'].replace("'","\'")
	elif 'village' in returndata['address']:
		city = returndata['address']['village'].replace("'","\'")
	else:
		city = ''
	if 'state' in returndata['address']:
		state = returndata['address']['state'].replace("'","\'")
	else:
		state = ''

	query = "INSERT INTO `coordinates` (`id`, `latitude`, `longitude`, `address_id`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, '" + lat5 + "','" + lon5 + "', (SELECT `id` FROM `addresses` WHERE `description` = '" + description + "' AND `postcode` = '" + postcode + "' AND `road` = '" + road + "' AND `city` = '" + city + "'),CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL);"
	coordinateQuery.write(query + '\n')

	query = "INSERT INTO `addresses` (`id`, `country_id`, `description`, `road`, `postcode`, `part`, `city`, `state`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, (SELECT `id` FROM `countries` WHERE `iso_code_2` = '" + iso_code + "')	, '" + description + "', '" + road + "', '" + postcode + "', '" + part + "', '" + city + "', '" + state + "', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL);"
	addressQuery.write(query + '\n')
	
	print(lat5 + ", " + lon5 + ": " + road + ", " + state + ", " + city + " (" + iso_code + ")")

	zoom = '18'
	filename = './maps/' + lat5 + '_' + lon5 + '_' + zoom + '.jpg'
	url = 'https://maps.locationiq.com/v2/staticmap?key=' + apikey + '&format=jpg&center='+lat+','+lon+'&zoom='+zoom+'&size=1250x1000&markers='+lat+','+lon+'|icon:large-red-cutout'
	time.sleep(1)
	r = requests.get(url, allow_redirects=True)
	open(filename, 'wb').write(r.content)
	query = "INSERT INTO `maps` (`id`, `coordinate_id`, `zoom`, `filename`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, (SELECT `id` FROM `coordinates` WHERE `latitude` = '" + lat5 + "' AND `longitude` = '" + lon5 + "'), " + zoom + ", '" + filename + "', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL);"
	mapQuery.write(query + '\n')

	zoom = '16'
	filename = './maps/' + lat5 + '_' + lon5 + '_' + zoom + '.jpg'
	url = 'https://maps.locationiq.com/v2/staticmap?key=' + apikey + '&format=jpg&center='+lat+','+lon+'&zoom='+zoom+'&size=1250x1000&markers='+lat+','+lon+'|icon:large-red-cutout'
	time.sleep(1)
	r = requests.get(url, allow_redirects=True)
	open(filename, 'wb').write(r.content)
	query = "INSERT INTO `maps` (`id`, `coordinate_id`, `zoom`, `filename`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, (SELECT `id` FROM `coordinates` WHERE `latitude` = '" + lat5 + "' AND `longitude` = '" + lon5 + "'), " + zoom + ", '" + filename + "', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL);"
	mapQuery.write(query + '\n')

	zoom = '12'
	filename = './maps/' + lat5 + '_' + lon5 + '_' + zoom + '.jpg'
	url = 'https://maps.locationiq.com/v2/staticmap?key=' + apikey + '&format=jpg&center='+lat+','+lon+'&zoom='+zoom+'&size=1250x1000&markers='+lat+','+lon+'|icon:large-red-cutout'
	time.sleep(1)
	r = requests.get(url, allow_redirects=True)
	open(filename, 'wb').write(r.content)
	query = "INSERT INTO `maps` (`id`, `coordinate_id`, `zoom`, `filename`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, (SELECT `id` FROM `coordinates` WHERE `latitude` = '" + lat5 + "' AND `longitude` = '" + lon5 + "'), " + zoom + ", '" + filename + "', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL);"
	mapQuery.write(query + '\n')

	saveToDone.write(lat5 + '_' + lon5 + '\n')
	runCount += 1
	print(" ")
	
