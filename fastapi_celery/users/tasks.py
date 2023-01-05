import time
import random

from celery import shared_task, chain

from .models import User


@shared_task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y


@shared_task(
    name='Verify email',
    # max_retries=5,
    # retry_backoff=True,
    # retry_backoff_max=700,
)
def verify(username, email):
    time.sleep(random.randint(5, 9))  # block processing of verify the email
    return username, email


@shared_task(
    name='send email',
    # max_retries=5,
    # retry_backoff=True,
    # retry_backoff_max=700,
)
def send_email(username_and_email):
    username, email = username_and_email
    time.sleep(random.randint(3, 7))  # blocking processing of sending an email
    return username, email


@shared_task(
    name='Store on database',
    # max_retries=5,
    # retry_backoff=True,
    # retry_backoff_max=700,
)
def store_on_db(username_and_email):
    from fastapi_celery.database import SessionLocal
    username, email = username_and_email
    user = User(username=username, email=email)
    session = SessionLocal()
    session.add(user)
    session.commit()
    return True


def task_pipeline(username: str, email: str):
    c = chain(
        verify.s(username=username, email=email),
        send_email.s(),  # .s means sequence. the result of a task will be passed as arguments to the next.
        store_on_db.s(),  # .s means sequence.
    )

    c()  # run the chain

    return "You are going to receive an email of confirmation soon"
