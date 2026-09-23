count = 1
total = 0

# BUG: Missing colon at the end of the while loop statement and incorrect loop condition (count < 5 stops before reaching 5). Fixed by adding a colon and changing condition to count <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Type mismatch error caused by concatenating a string with an integer total. Fixed by casting total to a string using str(total).
print("Sum of 1 to 5 is: " + str(total))
