import datetime
from datetime import timedelta

x = datetime.datetime.utcnow()
print(x)

minutes_to_sub = 5
x_new = x - timedelta(minutes = minutes_to_sub)
print(x_new)

#format time
#x = datetime.datetime.utcnow().isoformat(timespec='milliseconds')