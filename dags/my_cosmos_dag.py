from datetime import datetime
import os
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

profile_config = ProfileConfig(profile_name="default",
                               target_name="dev",
                               profile_mapping=PostgresUserPasswordProfileMapping(conn_id="postgres_default", 
                                                    profile_args={                                                        
                                                        "schema": "airflow_test"
                                                        },
                                                    ))


dbt_postgres_dag = DbtDag(project_config=ProjectConfig("/usr/local/airflow/dags/dbt/hello_world",),
                    operator_args={"install_deps": True},
                    profile_config=profile_config,
                    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
                    schedule_interval="@daily",
                    start_date=datetime(2024, 1, 1),
                    catchup=False,
                    dag_id="dbt_postgres_dag",)