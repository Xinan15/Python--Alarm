from datetime import datetime
from playsound import playsound

# input
alarm_time = input("Please enter time to alarm, for example: 09:50:00 am\n")
# hour
alarm_hour = alarm_time[0:2]
# minute
alarm_minute = alarm_time[3:5]
# second
alarm_seconds = alarm_time[6:8]
# am/pm
alarm_period = alarm_time[9:11].upper()
print("The alarm is set..")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    # time check
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    print("Get up!")
                    # alert
                    # playsound('audio.mp3')
                    break
