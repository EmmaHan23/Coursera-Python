smallest = None
largest = None

while True:
    user_input = input("Enter an integer number: ")
    
    if user_input == 'done':
        break
        
    try:
        num = int(user_input)
    except:
        print("Invalid input")
        continue
        
    if smallest is None or num < smallest:
        smallest = num
        
    if largest is None or num > largest:
        largest = num

print("Maximum is", largest)
print("Minimum is", smallest)