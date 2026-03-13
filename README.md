# Airflow Data Pipeline Project

## Project Overview
This project demonstrates a simple automated ETL pipeline using Apache Airflow and Python.

The pipeline performs:

- Extract raw sales data from CSV
- Transform the dataset using Pandas
- Load processed data into a new file
- Automate the workflow using Airflow DAG

## Technologies Used

- Python
- Pandas
- Apache Airflow
- SQL
- Git & GitHub

## Project Structure

airflow-data-pipeline
│
├── dags
│   └── sales_pipeline_dag.py
│
├── scripts
│   └── etl_process.py
│
├── data
│   ├── raw_sales.csv
│   └── processed_sales.csv
│
├── sql
│   └── create_table.sql
│
└── README.md

## Workflow

1. Extract raw sales dataset
2. Clean and transform data
3. Generate processed dataset
4. Automate pipeline with Airflow

## Skills Demonstrated

- Data Engineering pipelines
- ETL process design
- Workflow orchestration
- Data cleaning and transformation
- Git version control

## Author

Sandeep Reddy