from datetime import datetime

dt = datetime.now()
print(dt)

print(dt.weekday())

print(f"{dt.month}, {dt.weekday()}, {dt.day}, {dt.year}, {dt.time()}")