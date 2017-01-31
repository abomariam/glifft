from __future__ import absolute_import

from celery import shared_task


@shared_task
def dummy_task():
    print("Executing dummy task")
