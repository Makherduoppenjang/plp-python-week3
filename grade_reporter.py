scores = [72, 45, 90, 61, 38]

# Initialize trackers for pass count, fail count, and total score sum
passed_count = 0
failed_count = 0
total_score = 0

# Loop through each score in the list
for score in scores:
    total_score += score  # Add to running total
    
    # Determine grade based on score conditions
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
    # Track passes and fails
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1
        
    print(f"Score: {score} - Grade: {grade}")

# Calculate average rounded to 1 decimal place
average_score = round(total_score / len(scores), 1)

print(f"Learners Passed: {passed_count}")
print(f"Learners Failed: {failed_count}")
print(f"Average Score: {average_score}")
