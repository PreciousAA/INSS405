grades = []
num_user = 3
for i in range(num_user):
    grade = float(input("Enter final grade for user" +  str(i+1) + ": "))
grades.append(grade)

mean_grade = sum(grades) / num_user

if mean_grade >=90:
    final_grade = "A"
elif mean_grade >=80:
    final_grade = "B"
elif mean_grade >=70:
    final_grade = "C"
elif mean_grade >=60:
    final_grade = "D"
else:
    final_grade = "F"

print ("The final letter grade based on mean score of", num_user, "user is", final_grade,".")







