from datetime import datetime

data_str = "2023-04-24 09:03:32.744178"
dt = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S.%f")
get_year = lambda d: d.year
get_month = lambda d: d.month
get_day = lambda d: d.day
get_time = lambda d: d.time()

print(get_year(dt))
print(f"{get_month(dt):02d}")
print(f"{get_day(dt):02d}")
print(get_time(dt))