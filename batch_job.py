from prefect import flow, task

@task
def extract():
    return "Data Extracted"

@task
def transform(data):
    return f"{data} → Transformed"

@task
def load(data):
    return f"{data}"

@flow
def etl_flow(job_name: str = "Default Job"):
    raw = extract()
    processed = transform(raw)
    load(f"{job_name}: {processed}")

@flow
def post_etl_flow(job_name: str = "Daily ETL"):
    return f"Running post ETL tasks for job: {job_name}"

if __name__ == "__main__":
    etl_flow(job_name="Morning ETL")
    message = post_etl_flow(job_name="Morning ETL")
    print(message)
