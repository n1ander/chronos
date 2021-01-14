import datetime
import requests
import timeit
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
        print(response.json()['uuid'])

def main():
    startTime = timeit.default_timer()
    with requests.Session() as session:
        for _ in range(100):
            fetch(session, url)
    print("\nCompleted Execution in: ", timeit.default_timer() - startTime)

main()