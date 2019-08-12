from datetime import datetime

print(datetime.now())

date_time = datetime.now()

print("La fecha es: {}/{}/{} ".format(date_time.day, date_time.month, date_time.year))

print("La hora es: {}:{}:{} ".format(date_time.hour, date_time.minute, date_time.second))
