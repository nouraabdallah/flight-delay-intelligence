# Flight Delay Intelligence

**Course:** Data Engineering  
**Phase:** 1 – Project Proposal and Environment Setup

## Team Members

| Team Member | Student ID | Responsibility |
|---|---:|---|
| Noura Abdallah Ahmed (Team Leader) | 692300123 | Team coordination and project integration |
| Alaa Ahmed Abdeltwab | 692300266 | Python data ingestion and source handling |
| Mariam Mohamed Hany | 692300216 | PostgreSQL database design and SQL transformations |
| Zeina Mabrouk Mabrouk | 692300112 | Data profiling and quality checks |
| Moataz Baligh Hamdy | 692300300 | Kestra workflows and dashboard planning |

## Project Overview

Flight Delay Intelligence is a Data Engineering project that focuses on analyzing historical flight delay data in the United States.

The project will help us understand how arrival delays differ between airlines and airports, how they change over time, and which factors contribute most to delays.

We will build a data pipeline that starts with collecting the source data using Python, stores the original data, and then processes it in PostgreSQL. We will also use Kestra to manage and automate the pipeline. Finally, we plan to use a BI dashboard to present the results and make comparisons easier.

The dataset contains monthly aggregated statistics for each carrier and airport, based on the month and year. It does not contain information about individual flights or real-time flight updates.

## Dataset

- **Dataset:** [Airline Delay Causes – Kaggle](https://www.kaggle.com/datasets/anshuls235/airline-delay-causes)
- **Original data source:** [Bureau of Transportation Statistics (BTS)](https://www.bts.gov/explore-topics-and-geography/topics/airline-time-performance-and-causes-flight-delays)
- **Local dataset profile:** 279,182 rows and 22 original columns (21 named columns and one completely empty column).
- **Time period:** 2003–2020.

The dataset file is not included in the repository. Each team member who needs the data should download it separately and place the local copy inside the `data/` directory.

## Project Objectives

We will focus on answering the following questions:

1. How do arrival delays vary between airlines and across different months and years?
2. Which airports have the highest arrival delay rates? We will also consider the number of flights and the average delay minutes per delayed arrival.
3. How much does each reported delay cause contribute to the total delay, and how does this differ between airlines and over time?

## Architecture and Current Progress

During Phase 1, we focused on understanding the dataset, preparing the project structure, and setting up the database environment.

**What we have completed:**

- Defined the project idea and its main objectives.
- Downloaded and examined the dataset to understand its structure and possible data-quality issues.
- Prepared the local Docker Compose environment.
- Set up PostgreSQL 16 and pgAdmin 4.
- Successfully connected to PostgreSQL through pgAdmin on the team leader's Windows machine.

**What we plan to work on in the next phases:**

- Build Python scripts to load the source data.
- Keep the original data in its raw form before applying transformations.
- Design the PostgreSQL tables and build the required SQL transformations.
- Add data-quality checks to identify invalid or missing values.
- Create and manage the pipeline using Kestra.
- Build a BI dashboard to explore and present the results.

The project architecture is available in `docs/architecture.png`, and the Phase 1 proposal is available in `docs/Flight_Delay_Intelligence_Phase1_Proposal.pdf`.

## Local Environment Setup

The following steps explain how to run the project environment locally on Windows.

### 1. Install Docker Desktop

Download and install Docker Desktop, then make sure it is running.

### 2. Create the Environment File

Open PowerShell in the project directory and run:

```powershell
Copy-Item .env.example .env
```

### 3. Set Your Local Credentials

Open the `.env` file and set strong passwords for:

- `POSTGRES_PASSWORD`
- `PGADMIN_DEFAULT_PASSWORD`

The `.env` file contains local credentials, so it should not be uploaded to GitHub.

### 4. Start the Services

Run the following commands in PowerShell:

```powershell
docker compose config --quiet
docker compose up -d
docker compose ps
```

The last command should show the running containers.

### 5. Open pgAdmin

Open the following address in your browser:

http://localhost:5050

Log in using the pgAdmin email and password defined in the `.env` file.

### 6. Connect to PostgreSQL


Register a new server in pgAdmin using these settings:

| Setting | Value |
|---|---|
| Host | `postgres` |
| Port | `5432` |
| Database | `flight_intelligence` |
| Username | `flight_user` |
| Password | Value of `POSTGRES_PASSWORD` in `.env` |

### 7. Test the Connection

Open the Query Tool in pgAdmin and run:

```sql
SELECT current_database(), current_user, version();
```

If the query returns the database name, username, and PostgreSQL version, the connection is working correctly.

### 8. Stop the Services

To stop the containers without deleting the database data, run:

```powershell
docker compose down
```

**Important:** Do not use `docker compose down -v` unless you intentionally want to delete the persistent database volumes and their stored data.

## Repository Structure

The project files are organized as follows:

```text
Flight-Delay-Intelligence/
│
├── docs/
│   ├── proposal
│   ├── architecture.png
│   ├── data profile
│   ├── submission checklist
│   └── screenshots
│
├── data/
│   └── Local dataset (not included in GitHub)
│
├── scripts/
│   └── Python ingestion and processing scripts
│
├── sql/
│   └── Database tables, transformations, and checks
│
├── flows/
│   └── Kestra workflow files
│
├── docker-compose.yml
└── .env.example
```

Some directories will contain more files as we move to the implementation phases.

## Data Limitations and Initial Observations

While examining the dataset, we noticed a few issues that need attention during the cleaning and transformation stages:

- Some metric values are missing.
- Some values are negative and need to be checked before deciding how to handle them.
- One of the original columns is completely empty.
- Some airlines have different names across different periods, which may affect comparisons.

Another limitation is that the dataset only covers the period from 2003 to 2020. Therefore, the project will focus on historical analysis rather than current flight conditions.

We will document the cleaning decisions and apply the necessary validation checks during the upcoming implementation phases.