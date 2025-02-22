from celery import Celery

celery_app = Celery('tasks', broker='pyamqp://guest@localhost//')

@celery_app.task
def example_task(data):
    return f"Processed {data}"
