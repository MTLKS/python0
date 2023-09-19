import datetime

curr_time = datetime.datetime.now()
curr_timestamp = float(curr_time.timestamp())
curr_date = curr_time.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {curr_timestamp:,.4f} \
or {curr_timestamp:.2E} in scientific notation")
print(curr_date)
