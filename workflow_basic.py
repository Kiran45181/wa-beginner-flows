from prefect import flow, task

@task
def first_step():
    return "Version 2"

@task
def second_step(data):
    return f"{data} -> Second step finished"

@task
def third_step(data):
    return f"{data} -> Third step finished"

@flow
def basic_workflow():
    first_step()
    
