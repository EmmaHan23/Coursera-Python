filename = 'mbox-short.txt'
try:
    with open(filename) as file:
        sender_counts = {} 
        for line in file:
            if line.startswith('From '):
                words = line.split()
                if len(words) > 1: 
                    email = words[1]
                    sender_counts[email] = sender_counts.get(email, 0) + 1

except FileNotFoundError:
    print(f"File {filename} not found.")
    exit()

max_count = 0
max_sender = None

for sender, count in sender_counts.items():
    if count > max_count:
        max_count = count
        max_sender = sender

if max_sender:
    print(f"{max_sender} {max_count}")
else:
    print("No 'From ' lines found in the file.")