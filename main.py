from fastapi_celery import create_app
from fastapi_celery.users.tasks import task_pipeline


app = create_app()
celery = app.celery_app

if __name__ == '__main__':

    print(task_pipeline(username='Lucas', email='email@email.com'))
