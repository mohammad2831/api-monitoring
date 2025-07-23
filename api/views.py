from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ApiViewSerializer
from rest_framework.response import Response
from .test import monitor_api_performance_adhoc
import requests
import time
from datetime import datetime
from django.db import transaction
from django_celery_beat.models import IntervalSchedule, PeriodicTask
import json
from .models import ApiTarget
class ApiView(APIView):
    def post(self,request):
        data = ApiViewSerializer(data = request.data)
        if data.is_valid():
            api_url  = data.validated_data.get('api')
            interval_minutes = data.validated_data.get('interval_minutes')
            start_test = data.validated_data.get('start_test')
            finish_test = data.validated_data.get('finish_test')
            print(api_url)
            print(interval_minutes)
            print(start_test)
            print(finish_test)

            try:
                with transaction.atomic():
                    schedule, created = IntervalSchedule.objects.get_or_create(
                        every = interval_minutes,
                        period = IntervalSchedule.MINUTES,
                    )

                    task = PeriodicTask.objects.create(
                    interval=schedule,
                    name=f"Monitor: {api_url}",
                    task="monitors.tasks.task_monitor",
                    kwargs=json.dumps(
                        {
                            "monitor_id": instance.id,
                        }
                    ),
                )
                instance.task = task
                api_target = ApiTarget.objects.create(
                    
                ) 
            except:
                pass


            monitor_api_performance_adhoc.delay(api_url, interval_minutes)
            
            return Response({api_url, interval_minutes})

        else:
            return Response({"error": "problem in user status table"}, status=408)
        

    def test():
        pass
"""


"""
"""
# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .task import send_welcome_email # وارد کردن وظیفه Celery

def register_user(request):
    if request.method == 'POST':
        user_email = request.POST.get('email', 'test@example.com') # فرض کنید ایمیل از فرم می آید

        # به جای اجرای مستقیم، وظیفه را به Celery می‌فرستیم
        # .delay() یک shortcut برای .apply_async() است
        send_welcome_email.delay(user_email) 

        return HttpResponse(f"کاربر ثبت نام شد. ایمیل خوش‌آمدگویی به {user_email} در حال ارسال است (در پس‌زمینه).")

    # یک فرم ساده برای تست
    return render(request, 'myapp/register_form.html')



"""














"""            def monitor_api_performance(url: str, threshold: float = 1.0):
                try:
                    start_time = time.time()
                    response = requests.get(url, timeout=5)
                    total_time = time.time() - start_time
                    server_time = response.elapsed.total_seconds()

                    print(f"[{datetime.now()}] {url}")
                    print(f"  Server response: {server_time:.3f}s")
                    print(f"  Total time: {total_time:.3f}s") 
                    print(f"  Status: {response.status_code}")

                    if server_time > 0.1:
                        print(f"  ⚠️  WARNING: Response time exceeds {0.1}s threshold")

                except requests.exceptions.Timeout:
                    print(f"  ❌ REQUEST TIMEOUT")
                except requests.exceptions.RequestException as e:
                    print(f"  ❌ REQUEST FAILED: {e}")

            for i in range(interval_minutes):
                monitor_api_performance(api_url)

   """   
