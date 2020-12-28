Project: Data Pipelines with Airflow

1. Introduction
A music streaming company, Sparkify, has decided to introduce more automation and monitoring to their data warehouse ETL pipelines and came to the decision that Apache Airflow might be the best solution to meet their ask.
Their source data is residing in S3 buckets and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consists of JSON logs having the information about the user activity in the application and the JSON metadata about the songs the users listen to.
The purpose of this project is to build a good quality Data Pipeline on Apache Airflow which is dynamic and has reusable tasks along with monitoring for business purposes.

2. Source Data
As discusses in the introduction, the source data includes song data and the activities data present in the JSON format, sample locations are as below-
a. Song data: s3://udacity-dend/song_data
b. Log data: s3://udacity-dend/log_data

3. Design: Data Warehouse on Amazon Redshift
a.Fact Table
    songplays - records in log data associated with song plays i.e. records with page NextSong
      songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
b.Dimension Tables
    users - users in the app fields - user_id, first_name, last_name, gender, level
    songs - songs in music database fields - song_id, title, artist_id, year, duration
    artists - artists in music database fields - artist_id, name, location, lattitude, longitude
    time - timestamps of records in songplays broken down into specific units fields - start_time, hour, day, week, month, year, weekday


4. Project structure
a. dags
     final_pipeline.py - The main Airflow DAG for the data pipeline
b. plugins
     operators
       stage_redshift.py - Airflow custom operator to read JSON files from S3 to Redshift
       load_fact.py - Airflow custom operator to load the fact table in Redshift
       load_dimension.py - Airflow custom operator to load dimension tables in Redshift
       data_quality.py - Airflow custom operator for checking data quality
c. helpers
     create_tables.sql - Contains DDL statements to create tables in Redshift
     sql_queries.py - Redshift SQL queries used in the pipeline

The pipeline looks like as in the attached pipeline.PNG