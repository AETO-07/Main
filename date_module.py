import datetime

date = datetime.datetime.now()
print(date)
print(date.year)
print(date.strftime("%Y-%m-%d"))
print(date.strftime("%d/%m/%Y"))
print(date.strftime("%d %B, %Y"))
print(date.strftime("%d %b, %Y"))