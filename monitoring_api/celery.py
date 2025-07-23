# celery_project/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring_api.settings')


app = Celery('monitoring_api')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')




# Celery Beat Configuration
CELERY_BEAT_SCHEDULE = {
    'monitor-one-com-every-5-seconds': {
        'task': 'myapp.tasks.monitor_api_performance_adhoc',
        'schedule': 5.0, # 5.0 ثانیه (می‌تواند عدد صحیح یا float باشد)
        'args': ('https://celery.school/the-worker-and-the-pool', 5), # آرگومان‌های تسک: (api_url, interval_seconds)
        'options': {'expires': 300} # اختیاری: تسک بعد از 300 ثانیه (5 دقیقه) اگر اجرا نشد منقضی شود
    },
    'monitor-three-com-every-10-seconds': {
        'task': 'api.test.monitor_api_performance_adhoc',
        'schedule': 10.0,
        'args': ('https://celery.school/celery-worker-pools', 10),
    },
    'monitor-nine-com-every-15-seconds': {
        'task': 'api.test.monitor_api_performance_adhoc',
        'schedule': 15.0,
        'args': ('https://www.cpanel.ir/%D9%87%D8%A7%D8%B3%D8%AA-%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86-%D9%84%DB%8C%D9%86%D9%88%DA%A9%D8%B3-%D8%AF%D8%A7%D8%A6%D9%85%DB%8C/', 15),
    },
    # می‌توانید هر تعداد URL دیگر را اینجا اضافه کنید
}

