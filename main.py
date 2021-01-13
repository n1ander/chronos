import datetime
from datetime import timedelta

minutes = 60
currentTime = datetime.datetime.utcnow()
beginTime = currentTime - timedelta(minutes = minutes)

def formatTime(x):
    return x.isoformat(timespec='milliseconds') + 'Z'

startTime = formatTime(currentTime)
endTime = formatTime(beginTime)

print(startTime)
print(endTime)
