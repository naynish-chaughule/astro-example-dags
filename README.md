#

astro dev start --wait 15m
astro run dbt_postgres_dag

# run custom image

docker build --no-cache --tag my-dbt .
astro dev start --image-name my-dbt
