from prefect import flow, task


@task
def extract():
    return "Data Extracted"

@task
def transform(data):
    return f"{data} → Transformed"

@task
def load(data):
    print(f"Loading: {data}")

@flow
def etl_flow():
    raw = extract()
    processed = transform(raw)
    load(processed)

#@flow
#def post_etl_flow(job_name: str = "Daily ETL"):
    #return f"Running job: {job_name}"


if __name__ == "__main__":
    etl_flow()

    #message = post_etl_flow(job_name="Morning ETL")
    #print(message)
