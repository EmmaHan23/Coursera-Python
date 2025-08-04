filename = 'mbox-short.txt'
hour_counts = {}

try:
    with open(filename) as file:
        for line in file:
            if line.startswith('From '):
                time = line.split()[5] 
                hour = time.split(':')[0] 
                hour_counts[hour] = hour_counts.get(hour, 0) + 1

except FileNotFoundError:
    print(f"File {filename} not found.")
    exit()

for hour in sorted(hour_counts):
    print(f"{hour} {hour_counts[hour]}")