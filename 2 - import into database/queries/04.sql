INSERT IGNORE INTO `types` (`id`, `user_id`, `name`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, (SELECT `id` FROM `users` WHERE `email` = 'floris@vanenter.nl'), 'vrijstaan', NULL, NOW(), NOW(), NULL);
INSERT IGNORE INTO `types` (`id`, `user_id`, `name`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, (SELECT `id` FROM `users` WHERE `email` = 'floris@vanenter.nl'), 'overnachtingsplaats', NULL, NOW(), NOW(), NULL);
INSERT IGNORE INTO `types` (`id`, `user_id`, `name`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, (SELECT `id` FROM `users` WHERE `email` = 'floris@vanenter.nl'), 'camperplaats', NULL, NOW(), NOW(), NULL);
INSERT IGNORE INTO `types` (`id`, `user_id`, `name`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES (NULL, (SELECT `id` FROM `users` WHERE `email` = 'floris@vanenter.nl'), 'camping', NULL, NOW(), NOW(), NULL);
