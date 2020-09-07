from __future__ import absolute_import, unicode_literals
from django.http import JsonResponse
from celery.result import AsyncResult

# Create your views here.
from app01.tasks import add, mul, xsum


def async_mul_task(request):
    """
      使用调用apply_async，相乘的任务
    :param request:
    :return:
    """
    arg1 = 1
    arg2 = 2
    result = mul.apply_async(args=(arg1, arg2,),
                             queue='mul_queue',
                             routing_key='mul_task',
                             priority=0,
                             exchange='compute_node')
    task_status = AsyncResult(result.task_id, app=result.app)
    return JsonResponse({'input_args': [arg1, arg2], 'task_id': result.task_id, 'result': task_status.get()})


def sync_mul_task(request):
    """
        使用delay，调用相乘的任务
    :param request:
    :return:
    """
    arg1 = 1
    arg2 = 2
    result = mul.delay(arg1, arg2)
    task_status = AsyncResult(result.task_id, app=result.app)
    return JsonResponse({'input_args': [arg1, arg2], 'task_id': result.task_id, 'result': task_status.get()})


def async_add_task(request):
    """
        使用调用apply_async，求和的任务
    :param request:
    :return:
    """
    arg1 = 2
    arg2 = 2
    result = add.apply_async(args=(arg1, arg2,),
                             queue='add_queue',
                             routing_key='add_task',
                             priority=0,
                             exchange='compute_node')

    task_status = AsyncResult(result.task_id, app=result.app)

    return JsonResponse({'input_args': [arg1, arg2], 'task_id': result.task_id, 'result': task_status.get()})


def sync_add_task(request):
    """
        使用调用delay，求和的任务
    :param request:
    :return:
    """
    arg1 = 2
    arg2 = 2
    result = add.delay(arg1, arg2)
    print(result)
    task_status = AsyncResult(result.task_id, app=result.app)

    return JsonResponse({'input_args': [arg1, arg2], 'task_id': result.task_id, 'result': task_status.get()})


def async_xsum_task(request):
    """
        使用apply_async，调用列表求和
    :param request:
    :return:
    """
    number_list = [1, 1, 1, 1, 6]
    result = xsum.apply_async(args=(number_list,),
                              queue='xsum_queue',
                              routing_key='xsum_task',
                              priority=0,
                              exchange='compute_node')

    task_status = AsyncResult(result.task_id, app=result.app)
    return JsonResponse({'input_args': number_list, 'task_id': result.task_id, 'result': task_status.get()})


def sync_xsum_task(request):
    """
        使用delay，调用列表求和
    :param request:
    :return:
    """
    number_list = [1, 1, 1, 1, 6]
    result = xsum.delay(number_list)

    task_status = AsyncResult(result.task_id, app=result.app)
    return JsonResponse({'input_args': number_list, 'task_id': result.task_id, 'result': task_status.get()})
