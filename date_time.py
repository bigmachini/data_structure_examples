
import datetime 

actual_date = input()
expected_date  = input()

d = actual_date.split(' ')
actual_date = datetime.datetime(int(d[2]), int(d[1]), int(d[0]))

d = expected_date.split(' ')
expected_date = datetime.datetime(int(d[2]), int(d[1]), int(d[0]))
if  actual_date - expected_date < 0:
    fine = 0
elif actual_date.year != expected_date.year:
    fine = 10000
elif actual_date.month != expected_date.month:
    fine = 500 * (actual_date.month - expected_date.month)
else:
    diff_date = actual_date - expected_date
    diff_date = diff_date.total_seconds() / (3600 * 24)
    fine = 15 * diff_date

print(int(fine))