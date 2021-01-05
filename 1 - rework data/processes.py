#!/usr/bin/python3
import requests,csv,json
sourceQuery = open('./queries/insert_sources.sql', 'a')
typeQuery = open('./queries/insert_types.sql','a')
tagQuery = open('./queries/insert_tags.sql','a')
locationQuery = open('./queries/insert_locations.sql','a')
locationSourceQuery = open('./queries/insert_location_source.sql','a')
locationTagQuery = open('./queries/insert_location_tag.sql','a')
imageQuery = open('./queries/insert_images.sql','a')

coordinateDict = dict()
with open('data/coordinates.csv', encoding="utf8") as csvFile:
	readerResult = csv.DictReader(csvFile, delimiter=';', quotechar='"')
	for line in readerResult:
		coordinateDict[line['id']] = line

locationDict = dict()
with open('data/locations.csv', encoding="utf8") as csvFile:
	readerResult = csv.DictReader(csvFile, delimiter=';', quotechar='"')
	for line in readerResult:
		locationDict[line['id']] = line

locationPictureDict = dict()
with open('data/location_picture.csv', encoding="utf8") as csvFile:
	readerResult = csv.DictReader(csvFile, delimiter=';', quotechar='"')
	for line in readerResult:
		locationPictureDict[line['id']] = line

locationTagDict = dict()
with open('data/location_tag.csv', encoding="utf8") as csvFile:
	readerResult = csv.DictReader(csvFile, delimiter=';', quotechar='"')
	for line in readerResult:
		locationTagDict[line['id']] = line

pictureDict = dict()
with open('data/pictures.csv', encoding="utf8") as csvFile:
	readerResult = csv.DictReader(csvFile, delimiter=';', quotechar='"')
	for line in readerResult:
		pictureDict[line['id']] = line

regionDict = dict()
with open('data/regions.csv', encoding="utf8") as csvFile:
	readerResult = csv.DictReader(csvFile, delimiter=';', quotechar='"')
	for line in readerResult:
		regionDict[line['id']] = line
		
sourceDict = dict()
with open('data/sources.csv', encoding="utf8") as csvFile:
	readerResult = csv.DictReader(csvFile, delimiter=';', quotechar='"')
	for line in readerResult:
		sourceDict[line['id']] = line
		
tagDict = dict()
with open('data/tags.csv', encoding="utf8") as csvFile:
	readerResult = csv.DictReader(csvFile, delimiter=';', quotechar='"')
	for line in readerResult:
		tagDict[line['id']] = line
		
typeDict = dict()
with open('data/types.csv', encoding="utf8") as csvFile:
	readerResult = csv.DictReader(csvFile, delimiter=';', quotechar='"')
	for line in readerResult:
		typeDict[line['id']] = line
		
#for type in typeDict.values():
#	query = "INSERT INTO `types` (`id`, `user_id`, `name`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, 1, '" + type['name'] + "', NULL, NOW(), NOW(), NULL);"
#	typeQuery.write(query + '\n')

#for source in sourceDict.values():
#	query = "INSERT INTO `sources` (`id`, `user_id`, `name`, `link`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, '1', '" + source['name'] + "', '" + source['link'] + "', '" + source['note'] + "', NOW(), NOW(), NULL);"
#	sourceQuery.write(query + '\n')
	
#query = "INSERT INTO `sources` (`id`, `user_id`, `name`, `link`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, '1', 'Onbekend', 'https://beakerbus.nl', 'Ergens opgedoken', NOW(), NOW(), NULL);"
#sourceQuery.write(query + '\n')
	
#for tag in tagDict.values():
#	query = "INSERT INTO `tags` (`id`, `user_id`, `name`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, 1, '" + tag['name'] + "', NOW(), NOW(), NULL);"
#	tagQuery.write(query + '\n')

for loc in locationDict.values():
	type = typeDict[loc['type_id']]
	coordinate = coordinateDict[loc['coordinate_id']]
	lat = coordinate['latitude']
	lon = coordinate['longitude']
	lat5 = (lat.split('.'))[0] + '.' + (lat.split('.'))[1][0:5]
	lon5 = (lon.split('.'))[0] + '.' + (lon.split('.'))[1][0:5]
	query1 = "INSERT INTO `locations` (`id`, `user_id`, `type_id`, `coordinate_id`, `private`, `name`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, '1', (SELECT `id` FROM `types` WHERE `name` = '" + type['name'] + "'),  (SELECT `id` FROM `coordinates` WHERE `latitude` = '" + lat5 + "' AND `longitude` = '" + lon5 + "'), '0', '" + loc['name'] + "', '" + loc['note'] + "', NOW(), NOW(), NULL);"
	locationQuery.write(query1 + '\n')
	if loc['source_id'] == '0':
		{ 'id': 0, 'name': 'Onbekend', 'nickname': 'n/a', 'link': 'https://beakerbus.nl', 'note': 'Ergens opgedoken' }
	else:
		source = sourceDict[loc['source_id']]
	query2 = "INSERT INTO `location_source` (`id`, `location_id`, `source_id`, `deleted_at`) VALUES (NULL, (SELECT `id` FROM `locations` WHERE `name` = '" + loc['name'] + "'), (SELECT `id` FROM `sources` WHERE `name` = '" + source['name'] + "'), NULL);"
	locationSourceQuery.write(query2 + '\n')
	
for locpic in locationPictureDict.values():
	location = locationDict[locpic['location_id']]
	image = pictureDict[locpic['picture_id']]
	query3 = "INSERT INTO `images` (`id`, `user_id`, `location_id`, `name`, `filename`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, '1', (SELECT `id` FROM `locations` WHERE `name` = '" + location['name'] + "'), '" + image['name'] + "', '" + image['filename'] + "', NOW(), NOW(), NULL);"
	imageQuery.write(query3 + '\n')

for loctag in locationTagDict.values():
	if loctag['tag_id'] == '0':
		print('skipped tag = 0')
	else:
		location = locationDict[loctag['location_id']]
		tag = tagDict[loctag['tag_id']]
		query4 = "INSERT INTO `location_tag` (`id`, `location_id`, `tag_id`, `deleted_at`) VALUES (NULL, (SELECT `id` FROM `locations` WHERE `name` = '" + location['name'] + "'), (SELECT `id` FROM `tags` WHERE `name` = '" + tag['name'] + "'), NULL);"	
		locationTagQuery.write(query4 + '\n')