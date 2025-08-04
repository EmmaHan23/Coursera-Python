filename = input("Enter file name: ")
try:
    file = open(filename)
except FileNotFoundError:
    print("File cannot be opened:", filename)
    exit()
count = 0

for line in file:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        print(email)
        count += 1

print(f"There were {count} lines in the file with From as the first word")
file.close()