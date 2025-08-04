file_name = input("Enter file name: ").strip()
with open(file_name, 'r') as file:
    content = file.read()
print(content.upper())