hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
if hours <= 40:
    gross_pay = hours * rate
else:
    overtime_hours = hours - 40
    gross_pay = (40 * rate) + (overtime_hours * rate * 1.5)
print(gross_pay)