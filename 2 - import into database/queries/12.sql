DELETE FROM `sources` WHERE `id` NOT IN (SELECT `source_id` FROM `location_source`);
UPDATE `types` SET `name` = 'slaapplek' WHERE `name` = 'overnachtingsplaats';
UPDATE `types` SET `name` = 'camperplek' WHERE `name` = 'camperplaats';
UPDATE `sources` SET `name` = replace(`name`,'Facebook:', 'FB:');