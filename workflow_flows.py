from prefect import flow, task

@task
def extract():
    return "Data Extracted"

@task
def transform(data):
    return f"{data} → Transformed"

# ✅ New validate task added
@task
def validate(data):
    return f"{data} → Validated"

@task
def load(data):
    return f"{data}"  # Logs will not show in Cloud

@flow
def etl_flow(job_name: str = "Daily ETL"):
    raw = extract()
    processed = transform(raw)
    # ✅ Validation step added
    validated = validate(processed)
    load(f"{job_name}: {validated}")

@flow
def post_etl_flow():
    return "Post ETL tasks executed"  # Logs not visible

@flow
def notification_flow():
    return "Notification sent"  # Logs not visible
