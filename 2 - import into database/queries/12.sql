INSERT INTO `favorites`
	SELECT NULL, (SELECT `id` FROM `users` WHERE `email` = 'floris@vanenter.nl'), `id`, NOW(),NOW() FROM `locations`;