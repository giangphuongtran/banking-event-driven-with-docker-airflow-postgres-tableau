## 10-Feb-2026:
 
``` bash
cd Volumes/Sandisk/learning
mkdir docker .github/workflows consumer postgres kafka-debezium data-generator
python -m venv .venv
source .venv/bin/activate
```

- Created `README.md, .gitignore, docker-compose.yml, dockerfile-airflow.dockerfile, .env`
- Added `platform: linux/amd64` because some images in the `docker-compose.yml` don't publish an arm64 manifest for that tag

```bash
docker compose exec airflow-webserver airflow users Created --username mimi --firstname tran --lastname mi --role Admin --email admin@gmail.com --password airflow_password
```

- Airflow services failed because of no airflow db init -> Add airflow-init service into `docker-compose.yml`
- Created database and tables `postgres/01_create_tables.sql`
- Created data generator `data-generator/faker_generator.py`
- Created a connector to Kafka and Debezium `kafka-debezium/generate_post_connector.py`
- Checked for existing topics on Kafka

```bash
docker compose exec kafka kafka-topics --bootstrap-server kafka:9092 --list
```

- Committed and saved today's progress to Github

```bash
git init
git add README.md
git commit -m "Initial commit: event-driven banking data platform"
git branch -M main
git remote add origin https://github.com/giangphuongtran/banking-event-driven-with-docker-airflow-postgres-tableau.git
git push -u origin main
```

- Created DAG tasks to download data from MinIO and load into Snowflake `docker/dags/minio_to_snowflake.py`

## 11-Feb-2026:

- Initialized dbt with
```bash
dbt init banking_dbt
dbt debug
dbt run
```
- Created dbt models for staging and marts
- Created dbt snapshots
- Created DAG task to automate
- Failed to run the DAG task for replication due to schema not found, insufficient privilege even though ran successfully in terminal

## 12-Feb-2026

- Troubleshoot the issue, root cause was '$$' in password converted to only '$' -> change Snowflake password and remember this issue
- Created CI/CD workflows