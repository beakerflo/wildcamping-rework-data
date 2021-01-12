#!/bin/bash

rsync -avz ./profile-photos/ ~/Sites/apiVanlife/storage/app/public/profile-photos/
rsync -avz ./maps/ ~/Sites/apiVanlife/storage/app/public/gps-map

mysql -u "floris" "api" < "./queries/00.sql"
mysql -u "floris" "api" < "./queries/01.sql"
mysql -u "floris" "api" < "./queries/02.sql"
mysql -u "floris" "api" < "./queries/03.sql"
mysql -u "floris" "api" < "./queries/04.sql"
mysql -u "floris" "api" < "./queries/05.sql"
mysql -u "floris" "api" < "./queries/06.sql"
mysql -u "floris" "api" < "./queries/07.sql"
mysql -u "floris" "api" < "./queries/08.sql"
mysql -u "floris" "api" < "./queries/09.sql"
mysql -u "floris" "api" < "./queries/10.sql"
mysql -u "floris" "api" < "./queries/11.sql"
mysql -u "floris" "api" < "./queries/12.sql"
mysql -u "floris" "api" < "./queries/13.sql"