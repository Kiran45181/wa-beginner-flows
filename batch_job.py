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

@flow
def post_etl_flow():
    return "Post ETL tasks executed"  # Won't show in Cloud


if __name__ == "__main__":
    etl_flow()
