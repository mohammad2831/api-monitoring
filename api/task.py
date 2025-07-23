#task file
# myapp/tasks.py
from celery import shared_task
import time

@shared_task
def send_welcome_email(user_email):
    """
    این یک وظیفه Celery است که شبیه‌سازی ارسال ایمیل را انجام می‌دهد.
    عملیات زمان‌بر در اینجا انجام می‌شود.
    """
    print(f"شروع ارسال ایمیل خوش‌آمدگویی به: {user_email}...")
    time.sleep(5) # شبیه‌سازی تأخیر 5 ثانیه‌ای (مثلاً برای ارسال واقعی ایمیل)
    print(f"ایمیل خوش‌آمدگویی به {user_email} ارسال شد!")
    return f"Email to {user_email} sent successfully."