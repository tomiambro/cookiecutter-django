# import logging

# from celery import current_app as app
# from celery import Task
# from django.db import IntegrityError

# class BaseTask(Task):
#     soft_time_limit = 60 * 15  # in seconds, 15 minutes
#     time_limit = soft_time_limit + 30  # in seconds, 15.5 minutes
#     ignore_result = False

#     def before_start(self, task_id, args, kwargs):
#         pass

#     def after_return(self, status, retval, task_id, args, kwargs, einfo):
#         # Celery uses confusing function signatures...
#         # If the task succeeds the arguments are as expected.
#         # If the task fails the error is in the retval and the einfo parameter is empty.
#         if not isinstance(retval, Exception):
#             pass


# @app.task(base=BaseTask)