# Check-Checker
Pet-project to analyze money spends in Russia


Instrution:
```
git clone https://github.com/mintedcoinn/Check-Checker.git
```
Change env_example -> env

Setup secrets if needed.

cd Check-Checker

```
docker compose up -d

docker compose exec redash_server /app/bin/docker-entrypoint create_db

```
## Open browser and put:
```
localhost:5000
```
DB type:
```
PostegreSQL
```
Host:
```
postgres
```
User:
```
analytics_user
```
Password:
```
analytics_pass
```
DB name:
```
analytics
```
# Example:
<img width="3179" height="1633" alt="Снимок экрана 2026-01-25 232503" src="https://github.com/user-attachments/assets/a3620ccb-9953-4aa8-8589-70d92fb8b984" />
