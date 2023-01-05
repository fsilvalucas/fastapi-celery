# fastapi_celery

``` mermaid 
sequenceDiagram
    actor A as Client
    participant B as API [FastApi]
    participant C as Broker [Redis]
    participant D as Worker [Celery]
    participant E as Backend [Redis]
    participant F as Database
    A->>B: Post a Taask.
    B->>C: Send task to queue
    B->>A: Response OK!

    D->>C: Worker picks a task from queue

    D->>F: Stores result on database

    D->>E: Send the result of task to backend
``` 


- RUN WORKER: celery -A main.celery worker --loglevel=info
- RUN FLOWER: celery -A main.celery flower --port=XXYZ
