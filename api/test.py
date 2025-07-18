import requests
import time
from datetime import datetime

def monitor_api_performance(url: str, threshold: float = 1.0):
    """Monitor API response time and alert if threshold exceeded"""
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

# Monitor an API endpoint

for i in range(5): 
    monitor_api_performance("https://docs.djangoproject.com/en/5.2/intro/tutorial01/")
    time.sleep(10)
