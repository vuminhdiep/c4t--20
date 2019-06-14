
import datetime:

hAlarm = int(input("hour?"))
mAlarm = int(input("minute?"))

while True:
    h = datetime.datetime.now().hour
    m = datetime.datetime.now().minute
    if h == hAlarm and m == mAlarm:
        break
print("RingRingRing")