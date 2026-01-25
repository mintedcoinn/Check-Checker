# Check-Checker
Pet-project to analyze money spends in Russia


Instrution:
```
git clone https://github.com/mintedcoinn/Check-Checker.git
```
Change env_example -> env.
Setup secrets if needed.

cd Check-Checker

```
docker-compose up -d

docker-compose exec redash_server /app/bin/docker-entrypoint create_db

docker-compose restart redash_server redash_worker redash_scheduler
```
## Open browser and put:
```
localhost:5000
```
Create admin-user in Redash and u can work in it.

To down system:
```
docker-compose down
```

