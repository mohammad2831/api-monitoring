# celery_project/celery.py
import os
from celery import Celery

# محیط جنگو را تنظیم کنید تا Celery بتواند به تنظیمات پروژه دسترسی پیدا کند.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring_api.settings')

# یک اینستنس از Celery App ایجاد کنید.
# نام 'celery_project' نام پروژه جنگوی شماست.
app = Celery('monitoring_api')

# تنظیمات Celery را از فایل settings.py جنگو لود کنید.
# 'CELERY' یک namespace است که یعنی همه تنظیمات Celery باید با CELERY_ شروع شوند.
app.config_from_object('django.conf:settings', namespace='CELERY')

# وظایف (tasks) را به صورت خودکار از تمام فایل‌های tasks.py در اپلیکیشن‌های جنگو پیدا کنید.
app.autodiscover_tasks()

# یک وظیفه ساده برای تست (اختیاری، اما مفید برای دیباگ)
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')