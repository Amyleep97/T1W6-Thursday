# Prompt the user to enter a score
score = int(input("Enter the score (0-100):"))

# Determine the grade based on the score
if score >= 90 and score<= 100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >=  60:
    grade = "D"
else: 
    grade = "F"
    
print(f"The grade for score {score} is {grade}")