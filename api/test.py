import requests
import time
from datetime import datetime
from celery import shared_task






@shared_task(bind=True)
def monitor_api_performance_adhoc(self, api_url: str, interval_seconds: int): # Renamed the task for clarity
    """
    This task is called by Celery Beat and monitors a URL once.
    It directly receives the URL and interval as arguments.
    """
    try:
        threshold = 1.0 # You can keep this constant for now

        print(f"--- Starting Ad-Hoc Monitoring for: {api_url} with interval: {interval_seconds} seconds ---")
        start_time = time.time()
        try:
            response = requests.get(api_url, timeout=5) # 5-second timeout for the request
            total_time = time.time() - start_time # Calculate total response time
            
            status_code = response.status_code
            is_success = True if 200 <= status_code < 300 else False
            error_message = None

            print(f"[{datetime.now()}] URL: {api_url}")
            print(f"  Total response time: {total_time:.3f}s")
            print(f"  Status: {response.status_code}")

            if total_time > threshold:
                print(f"  ⚠️  WARNING: Response time exceeds {threshold}s threshold!")

        except requests.exceptions.Timeout:
            total_time = time.time() - start_time
            status_code = None
            is_success = False
            error_message = "Request timed out."
            print(f"  ❌ REQUEST TIMEOUT for {api_url}!")
        except requests.exceptions.RequestException as e:
            total_time = time.time() - start_time
            status_code = None
            is_success = False
            error_message = str(e)
            print(f"  ❌ REQUEST FAILED for {api_url}: {e}")
        except Exception as e: # Catch any other unexpected errors
            total_time = time.time() - start_time
            status_code = None
            is_success = False
            error_message = f"Unexpected error in task: {e}"
            print(f"  ❌ UNEXPECTED ERROR for {api_url}: {e}")

        # At this stage, results are not stored in the database. They are only printed.
        # For database storage, you'll need your Django models.
        print(f"--- Ending Ad-Hoc Monitoring for: {api_url} ---")

    except Exception as e:
        # In a production environment, you would implement retry logic and error logging here.
        print(f"General error in monitor_api_performance_adhoc task: {e}")







"""
def monitor_api_performance(url: str, threshold: float = 1.0):
    Monitor API response time and alert if threshold exceeded
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        total_time = time.time() - start_time
        server_time = response.elapsed.total_seconds()

        print(f"[{datetime.now()}] {url}")
        print(f"  Server response: {server_time:.3f}s")
        print(f"  Total time: {total_time:.3f}s") 
        print(f"  Status: {response.status_code}")

        if server_time > threshold:
            print(f"  ⚠️  WARNING: Response time exceeds {threshold}s threshold")

    except requests.exceptions.Timeout:
        print(f"  ❌ REQUEST TIMEOUT")
    except requests.exceptions.RequestException as e:
        print(f"  ❌ REQUEST FAILED: {e}")





@shared_task
def send_request(api, interval_minutes):

    for i in range(5): 
        monitor_api_performance(api)
        time.sleep(2)
"""