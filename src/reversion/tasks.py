import celery

@celery.task(ignore_result=True, default_retry_delay=60, max_retried=5)
def delay_save_revision(manager, manager_context, **kwargs):
    manager.save_revision(dict(
        (obj, callable(data) and data() or data)
        for obj, data
        in manager_context.items()
    ), **kwargs)