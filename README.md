# Flight Delay Intelligence

**Course:** Data Engineering  
**Phase:** 1 — Project Proposal and Environment Setup

## Team

| Team member | Student ID | Responsibility |
|---|---:|---|
| Noura Abdallah Ahmed (Team Leader) | 692300123 | Coordination, reproducibility, and project integration |
| Alaa Ahmed Abdeltwab | 692300266 | Python ingestion and source handling |
| Mariam Mohamed Hany | 692300216 | PostgreSQL schema and SQL transformations |
| Zeina Mabrouk Mabrouk | 692300112 | Data profiling and data-quality checks |
| Moataz Baligh Hamdy | 692300300 | Kestra orchestration and dashboard planning |

## Project overview

The project analyzes historical U.S. airline arrival-delay statistics by carrier, airport, month, year, and reported delay cause. It is designed as a reproducible data pipeline that will ingest the source data, preserve raw observations, transform and validate the data in PostgreSQL, coordinate tasks with Kestra, and present comparative results in a BI dashboard.

The source file contains monthly aggregated records at the grain of **carrier × airport × month × year**. It does not contain individual-flight records and is not a live data feed.

## Dataset

- Dataset page: https://www.kaggle.com/datasets/anshuls235/airline-delay-causes
- Underlying public statistics: https://www.bts.gov/explore-topics-and-geography/topics/airline-time-performance-and-causes-flight-delays
- Supplied local CSV profile: 279,182 rows, 22 original columns (21 named and one entirely empty), covering 2003–2020.
- Source CSV inferred types: `year` and `month` are `int64`; carrier and airport codes/names are text-like (`object`); numeric measures are inferred as `float64`; the final unnamed column is entirely null. The Proposal PDF contains the per-column type table.
- The dataset file is not included in this repository. Download it separately and keep the local copy under `data/` if required.

## Analytical questions

1. How do arrival delay rates differ by carrier, month, and year?
2. Which airports have the highest arrival delay rates and delay minutes per delayed arrival, with traffic-volume context?
3. How does the distribution of reported delay minutes by cause change across carriers and months/years?

## Architecture and implementation status

- **Completed in Phase 1:** project proposal, source-data profiling, and local Docker Compose setup with PostgreSQL 16 and pgAdmin 4. The PostgreSQL connection was demonstrated through pgAdmin on the team leader's Windows environment.
- **Planned for later phases:** Python ingestion, raw-data preservation, PostgreSQL analytical modeling, data-quality tests, Kestra orchestration, and BI dashboard development.
- Each teammate should independently run the local setup and be prepared to explain the Docker Compose services, network, persistent volumes, and PostgreSQL connection.

See `docs/architecture.png` and `docs/Flight_Delay_Intelligence_Phase1_Proposal.pdf`.

## Local environment setup

1. Install and start Docker Desktop.
2. Copy `.env.example` to `.env` using PowerShell:

   ```powershell
   Copy-Item .env.example .env
   ```

3. Set strong local values for `POSTGRES_PASSWORD` and `PGADMIN_DEFAULT_PASSWORD`. Do not commit `.env`.
4. Validate and start the services:

   ```powershell
   docker compose config --quiet
   docker compose up -d
   docker compose ps
   ```

5. Open http://localhost:5050 and sign in using the pgAdmin credentials in `.env`.
6. Register the PostgreSQL server with host `postgres`, port `5432`, database `flight_intelligence`, user `flight_user`, and the PostgreSQL password from `.env`.
7. Verify the connection:

   ```sql
   SELECT current_database(), current_user, version();
   ```

8. Stop services without deleting persistent volumes:

   ```powershell
   docker compose down
   ```

   Do not use `docker compose down -v` unless you intentionally want to delete the database volumes.

## Repository structure

- `docs/` — proposal, architecture, data profile, and local screenshots
- `scripts/` — Python ingestion and processing scripts (later phases)
- `sql/` — database definitions, transformations, and checks (later phases)
- `flows/` — Kestra workflow definitions (later phases)
- `docker-compose.yml` — PostgreSQL and pgAdmin services
- `.env.example` — configuration template without local credentials

## Data limitations

The supplied historical dataset ends in 2020. Missing metric values, negative values, an entirely empty column, and historical carrier-name variations were observed in the local copy. Cleaning and modeling rules will be documented and tested in the relevant implementation phases.
