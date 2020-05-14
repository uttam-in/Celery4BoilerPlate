from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import datetime
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

# Create your views here.
class CeleryTasks(GenericAPIView):

    def post(self, request, **kwargs):
        response = {"payload": {}, "status": 200, "error": [], "message": "", "file_form": ""}
        requestdata = request.data
        # task_name = eval(kwargs['func_name'])
        # task_name.delay(2, 3, "Suhas")
        func_name_received = kwargs.pop('func_name', None)
        func_module = kwargs.pop('func_module', None)
        path = kwargs.pop('path', None)
        scheduler_type = requestdata['scheduler_type'] or None
        task_id = kwargs.pop('task_id', None)

        start_year = kwargs.pop('task_scheduling_start_date_year', None)
        start_month = kwargs.pop('task_scheduling_start_date_month', None)
        start_day = kwargs.pop('task_scheduling_start_date_day', None)
        start_hour = kwargs.pop('task_scheduling_start_date_hour', None)
        start_minute = kwargs.pop('task_scheduling_start_date_minute', None)

        end_year = kwargs.pop('task_scheduling_end_date_year', None)
        end_month = kwargs.pop('task_scheduling_end_date_month', None)
        end_day = kwargs.pop('task_scheduling_end_date_day', None)
        end_hour = kwargs.pop('task_scheduling_end_date_hour', None)
        end_minute = kwargs.pop('task_scheduling_end_date_minute', None)

        # cron

        cron_end_year = kwargs.pop('crontask_scheduling_end_date_year', None)
        cron_end_month = kwargs.pop('crontask_scheduling_end_date_month', None)
        cron_end_day = kwargs.pop('crontask_scheduling_end_date_day', None)
        cron_end_hour = kwargs.pop('crontask_scheduling_end_date_hour', None)
        cron_end_minute = kwargs.pop('crontask_scheduling_end_date_minute', None)

        cron_schedule_hour = kwargs.pop('cron_schedule_hour', None)
        cron_schedule_minute = kwargs.pop('cron_schedule_minute', None)

        retval = None
        print(scheduler_type)
        print(scheduler_type == 'IntervalSchedule')


        try:
            if scheduler_type == 'IntervalSchedule':
                print("IntervalSchedule")

                schedule, created = IntervalSchedule.objects.get_or_create(every = 30,period = IntervalSchedule.SECONDS,)
                PeriodicTask.objects.create(
                interval = schedule,
                name = requestdata['task_id'],
                args=json.dumps([10]),
                task = 'scheduler.tasks.customtask',)


            elif scheduler_type == 'CrontabSchedule':
                print("Cron")
        except Exception as e:
            print(e)

        return Response(response)