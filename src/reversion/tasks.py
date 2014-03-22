import celery

@celery.task(ignore_result=True, default_retry_delay=60, max_retried=5)
def delay_save_revision(manager, data, **kwargs):
    manager.save_revision(data, **kwargs)