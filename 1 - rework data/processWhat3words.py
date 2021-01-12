import what3words,csv

whatWordsQuery = open('./queries/insert_what3words.sql', 'a')

coordinateDict = dict()
with open('data/coordinates.csv', encoding="utf8") as csvFile:
	readerResult = csv.DictReader(csvFile, delimiter=';', quotechar='"')
	for line in readerResult:
		coordinateDict[line['id']] = line

done = open('./logs/w3w_done.txt','r').read()
saveToDone = open('./logs/w3w_done.txt','a')

for gps in coordinateDict.values():

	lat = gps['latitude']
	lon = gps['longitude']
	lat5 = (lat.split('.'))[0] + '.' + (lat.split('.'))[1][0:5]
	lon5 = (lon.split('.'))[0] + '.' + (lon.split('.'))[1][0:5]
	
	if (lat5 + '_' + lon5) in done:
		print(lat + ', ' + lon + ' zit al in het systeem.')
		continue
	else:
		print('opzoeken: ' + lat + ', ' + lon)
		
	geocoder = what3words.Geocoder("J4UXR7ZO")
	res = geocoder.convert_to_3wa(what3words.Coordinates(lat, lon),'json','nl')
	w3w_nl = res['words']
	w3w_nearest = res['nearestPlace']

	res = geocoder.convert_to_3wa(what3words.Coordinates(lat, lon),'json','de')
	w3w_de = res['words']
	
	res = geocoder.convert_to_3wa(what3words.Coordinates(lat, lon),'json','en')
	w3w_en = res['words']
	
	res = geocoder.convert_to_3wa(what3words.Coordinates(lat, lon),'json','fr')
	w3w_fr = res['words']
	
	res = geocoder.convert_to_3wa(what3words.Coordinates(lat, lon),'json','es')
	w3w_es = res['words']
	
	query = "INSERT INTO `what3words` (`id`, `en`, `nl`, `fr`, `de`, `es`, `created_at`, `updated_at`) VALUES (NULL, '" + w3w_en + "', '" + w3w_nl + "', '" + w3w_fr + "', '" + w3w_de + "', '" + w3w_es + "', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
	whatWordsQuery.write(query + '\n')
	
	query = "INSERT INTO `near_places` (`id`, `name`, `created_at`, `updated_at`) VALUES (NULL, '" + w3w_nearest + "', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
	whatWordsQuery.write(query + '\n')

	query = "UPDATE `coordinates` SET `what3words_id` = (SELECT `id` FROM `what3words` WHERE `en` = '" + w3w_en + "'), `near_place_id` = (SELECT `id` FROM `near_places` WHERE `name` = '" + w3w_nearest + "') WHERE `latitude` = '" + lat5 + "' AND `longitude` = '" + lon5 + "';"
	whatWordsQuery.write(query + '\n')
	
	saveToDone.write(lat5 + '_' + lon5 + '\n')
