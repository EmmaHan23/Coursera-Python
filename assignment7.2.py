file_name = input("Enter file name: ")
count = 0
total = 0.0
with open(file_name, 'r') as file:
    for line in file:
        if line.startswith('X-DSPAM-Confidence:'):
            colon_pos = line.find(':')
            number_str = line[colon_pos+1:].strip()
            try:
                value = float(number_str)
                count += 1
                total += value
            except ValueError:
                continue
average = total / count if count > 0 else 0.0
print(f"Average spam confidence: {average:.16f}")