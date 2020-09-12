from celery.result import AsyncResult
from django.http import JsonResponse

# Create your views here.
from app_log.tasks import handler_log


def async_route_handler_log(request):
    log_content = 'async_route_handler_log'
    result = handler_log.apply_async(args=(log_content,))
    task_status = AsyncResult(result.task_id, app=result.app)
    return JsonResponse({'input_args': [log_content], 'task_id': result.task_id, 'result': task_status.get()})


def sync_route_handler_log(request):
    log_content = 'async_route_handler_log'
    result = handler_log.delay(log_content)
    task_status = AsyncResult(result.task_id, app=result.app)
    return JsonResponse({'input_args': [log_content], 'task_id': result.task_id, 'result': task_status.get()})
