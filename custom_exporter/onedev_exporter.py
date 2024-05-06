import requests
from prometheus_client import start_http_server, Gauge
import time


ONEDV_API_URL = "http://172.20.10.4:6610/~api/builds"


build_status_metric = Gauge('onedev_build_status', 'OneDev Build Status', ['project', 'branch'])

def fetch_and_export_build_data():
    try:
        response = requests.get(ONEDV_API_URL)
        response.raise_for_status()
        build_data = response.json()

        for build in build_data:
            project = build['project']
            branch = build['branch']
            status = build['status']

    
            build_status_metric.labels(project=project, branch=branch).set(status)

    except Exception as e:
        print(f"Error fetching build data from OneDev: {str(e)}")

if __name__ == '__main__':
    
    start_http_server(9101)

    while True:
        
        fetch_and_export_build_data()
        time.sleep(30)

