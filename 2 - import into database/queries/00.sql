INSERT INTO `users` (`id`, `name`, `email`, `email_verified_at`, `password`, `two_factor_secret`, `two_factor_recovery_codes`, `remember_token`, `current_team_id`, `profile_photo_path`, `created_at`, `updated_at`)
VALUES
	(1,'Floris','floris@vanenter.nl',NULL,'',NULL,NULL,NULL,1,NULL,'2020-12-29 13:24:13','2020-12-29 13:24:13');
INSERT INTO `teams` (`id`, `user_id`, `name`, `personal_team`, `created_at`, `updated_at`)
VALUES
	(1,1,'Floris\'s Team',1,'2020-12-29 13:24:13','2020-12-29 13:24:13');