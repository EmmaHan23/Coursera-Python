# Prompt the user for a score
score = float(input("Enter score: "))

# Validate the score range
if score < 0.0 or score > 1.0:
    print("Error: Score must be between 0.0 and 1.0")
else:
    # Determine the grade based on the score
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')