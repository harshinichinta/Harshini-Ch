# Program to convert distance in feet to inches, yards, and miles
# Input from user
feet = float(input("Enter the distance in feet: "))
# Conversion calculations
inches = feet * 12
yards = feet / 3
miles = feet / 5280
# Display results
print("Distance in feet :", feet)
print("Distance in inches :", inches)
print("Distance in yards :", yards)
print("Distance in miles :", miles)
