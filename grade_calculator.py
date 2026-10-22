# ------Mini Project (Student Grade Calculator) using Python-------
#.Total Marks Calcuation
#.Percentage Calculation
#. Grade Calculation
 

# 1.-----Calculate Total Marks--------
def calculate_total (marks): 
    return sum(marks)
#2.----- Calculate Percentage-----
def calculate_percentage (total):
    return total/ 500 *100
#3.----- Calculate Grade-----
def calculate_grade(percentage):
    if percentage >= 90:
        return"A+"
    elif percentage >= 80:
      return "A"
    elif percentage >= 70:
      return "B"
    elif percentage >= 60:
       return "C"
    elif percentage >= 40:
       return"D"
    else:
       return "Fail"

#4.----- Take Student details and marks-----
name = input ("Enter student name: ")
marks = []
for i in range (1,6):
    mark = float(input(f"Enter marks for subject{i}: "))
    marks.append(mark)
total = calculate_total(marks)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)

#5.----- Display Final Result-----
print ("\n--- STUDENT NAME ---")
print ("Name:", name)
print ("Total marks:",total , "/500")
print("Percentage:", percentage, "%")
print ("Grade:", grade)

print("\n--- RESULT DECLARED---")
