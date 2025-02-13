from datetime import datetime

# The timestamp Date
timestamp_ms = 1736852281335
pd = datetime.utcfromtimestamp(timestamp_ms / 1000).strftime('%Y-%m-%d')

print(pd)


# The Latest Date
ld = datetime.now().strftime('%Y-%m-%d')
print(ld)

if(ld == pd):
    print('Dates Are Same')
else:
    print('Dates Are Different')

dt = datetime(2025, 1, 15, 12, 38, 1)

# Convert datetime to timestamp in seconds, then multiply by 1000 to get milliseconds
timestamp_ms = int(dt.timestamp() * 1000)

print(timestamp_ms)