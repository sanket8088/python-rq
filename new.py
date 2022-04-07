from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler
from datetime import datetime, timedelta
import json

from task1 import example

scheduler = Scheduler(connection=Redis()) # Get a scheduler for the "default" queue
# scheduler = Scheduler(connection=Redis()) # Get a scheduler for the "foo" queue

sing = scheduler.schedule(
    scheduled_time=datetime.utcnow(), # Time for first execution, in UTC timezone
    func=example,                     # Function to be queued
    interval=10,                   # Time before the function is called again, in seconds
    repeat=None,                     # Repeat this number of times (None means repeat forever)
)


print(sing.id)


