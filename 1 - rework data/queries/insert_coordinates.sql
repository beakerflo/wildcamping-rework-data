INSERT INTO `coordinates` (`id`, `latitude`, `longitude`, `address_id`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, '52.68594','4.72473', (SELECT `id` FROM `addresses` WHERE `description` = 'Klaassen en Evendijk, Bergen (NH), North Holland, Netherlands, 1862PN, The Netherlands' AND `postcode` = '1862PN' AND `road` = 'Klaassen en Evendijk' AND `city` = 'Bergen (NH)'),CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL);
INSERT INTO `coordinates` (`id`, `latitude`, `longitude`, `address_id`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, '52.68594','4.72473', (SELECT `id` FROM `addresses` WHERE `description` = 'Klaassen en Evendijk, Bergen (NH), North Holland, Netherlands, 1862PN, The Netherlands' AND `postcode` = '1862PN' AND `road` = 'Klaassen en Evendijk' AND `city` = 'Bergen (NH)'),CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL);
