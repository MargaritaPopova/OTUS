**List of all ports listening**  
sudo lsof -i -P | grep -i "listen" 

**Kill process by PID**  
sudo kill -9 PID 

**List system daemons**  
launchctl list # list daemons 

**Kill system daemons**  
launchctl kill # kill daemons

 **Dump database FROM CONTAINER compressed**  
docker exec -u postgres <container_id> pg_dump -Cc | gzip > pg-backup-$(date -u +%Y-%m-%d).sql.gzip 

**Dump database FROM CONTAINER uncompressed**  
docker exec -u postgres <container_id> pg_dump -Cc > pg-backup-$(date -u +%Y-%m-%d).sql 

**Restore database LOCALLY**   
psql -U postgres postgres < pg-backup-2020-11-02.sql   
*-U postgres* - от какого пользователя заходить в базу  
*postgres* - имя базы

**Restore database IN CONTAINER**  
docker exec -u postgres <container_id> psql -U postgres postgres < pg-backup-2020-11-02.sql

**Dump database LOCALLY**  
pg_dump -Cc -U postgres > pg-backup-$(date -u +%Y-%m-%d).sql 

**Migrate IN CONTAINER**  
docker-compose exec web python expences/manage.py migrate

**Migrate LOCALLY with env variables from .env file**  
pipenv run python manage.py migrate


