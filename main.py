import datetime
import requests
import timeit
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta

minutes = 60
currentTime = datetime.datetime.utcnow()
beginTime = currentTime - timedelta(minutes = minutes)

def formatTime(x):
    return x.isoformat(timespec='milliseconds') + 'Z'

startTime = formatTime(currentTime)
endTime = formatTime(beginTime)

#cast and print to console
#print(str(startTime))
#print(str(endTime))


url = "https://httpbin.org/uuid"

def fetch(session, url):
    with session.get(url) as response:
        print(response.json())

def main():
    startTime = timeit.default_timer()
    with ThreadPoolExecutor(max_workers=10) as e:
        with requests.Session() as session:
            e.map(fetch, [session] * 100, [url] * 100)
            e.shutdown(wait=True)
    print("\nCompleted Execution in: ", timeit.default_timer() - startTime)

main()