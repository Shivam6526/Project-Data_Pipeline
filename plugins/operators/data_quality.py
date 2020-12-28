from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):
    #Code to configure the color of the task on Airflow UI
    ui_color = '#89DA59'
    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 tables=[],
                 sql="",
                 expected_result="",
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.tables = tables
        self.sql = sql
        self.expected_result=expected_result

    def execute(self, context):
        redshift_hook = PostgresHook(self.redshift_conn_id)
        for table in self.tables:
            sample_records = redshift_hook.get_records(self.sql.format(table=table))

            if len(sample_records) < 1 or len(sample_records[0]) < 1:
                raise ValueError(f"Data quality check failed for {table}; No results returned")
            num_records = sample_records[0][0]
            if self.expected_result=="greater than 0":
                if num_records < 1:
                    raise ValueError(f"Data quality check failed for {table}; Table contained 0 rows")
                self.log.info(f"Data quality check on table:- {table} passed with {sample_records[0][0]} number of records")