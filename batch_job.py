from prefect import flow, task

# ----------------- Tasks -----------------
@task
def extract():
    return "Data Extracted"

@task
def transform(data):
    return f"{data} → Transformed"

@task
def load(data):
    print(f"Loading: {data}")

# ----------------- ETL Flow -----------------
@flow
def etl_flow():
    raw = extract()
    processed = transform(raw)
    load(processed)

# ----------------- Post ETL Flow -----------------
@flow
def post_etl_flow(job_name: str = "Daily ETL"):
    return f"Running job: {job_name}"

# ----------------- Main Execution -----------------
if __name__ == "__main__":
    # Run ETL flow
    etl_flow()

    # Run Post ETL flow and capture output
    message = post_etl_flow(job_name="Morning ETL")
    print(message)  # Optional: see output in console
