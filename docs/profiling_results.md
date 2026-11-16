# Raw Dataset Profiling Results

## 1. Dataset Overview

- **File:** `894233989_32020_056_airline_delay_causes.csv`
- **Total records:** 279,182
- **Total columns:** 22
- **Duplicate records:** 0
- **Rows with unexpected field count:** 0

## 2. Column Name Issues

- **Empty column names:** 1
- **Column names with extra surrounding spaces:** 4
- Empty header positions: 22
- Column names with spaces: ` month`, ` weather_ct`, ` arr_delay`, ` carrier_delay`

## 3. Missing Values and Data Types

| Column | Missing Values | Integer | Float | Text |
|---|---:|---:|---:|---:|
| `year` | 0 | 279,182 | 0 | 0 |
| ` month` | 0 | 279,182 | 0 | 0 |
| `carrier` | 0 | 0 | 0 | 279,182 |
| `carrier_name` | 0 | 0 | 0 | 279,182 |
| `airport` | 0 | 0 | 0 | 279,182 |
| `airport_name` | 0 | 0 | 0 | 279,182 |
| `arr_flights` | 376 | 0 | 278,806 | 0 |
| `arr_del15` | 438 | 0 | 278,744 | 0 |
| `carrier_ct` | 376 | 0 | 278,806 | 0 |
| ` weather_ct` | 376 | 0 | 278,806 | 0 |
| `nas_ct` | 376 | 0 | 278,806 | 0 |
| `security_ct` | 376 | 0 | 278,806 | 0 |
| `late_aircraft_ct` | 376 | 0 | 278,806 | 0 |
| `arr_cancelled` | 376 | 0 | 278,806 | 0 |
| `arr_diverted` | 376 | 0 | 278,806 | 0 |
| ` arr_delay` | 376 | 0 | 278,806 | 0 |
| ` carrier_delay` | 376 | 0 | 278,806 | 0 |
| `weather_delay` | 376 | 0 | 278,806 | 0 |
| `nas_delay` | 376 | 0 | 278,806 | 0 |
| `security_delay` | 376 | 0 | 278,806 | 0 |
| `late_aircraft_delay` | 376 | 0 | 278,806 | 0 |
| `` | 279,182 | 0 | 0 | 0 |

## 4. Month Value Validation

- **Invalid or missing month values:** 0

## 5. Initial Observations

- This report describes the raw dataset before cleaning.
- Missing values are counted when a field is empty or contains only whitespace.
- Duplicate records are identified using a SHA-256 fingerprint of each parsed CSV row.
- Numeric types are inferred from the values; they are not validated against a complete data schema.
- No source data has been modified.