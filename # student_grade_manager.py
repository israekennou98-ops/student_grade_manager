# student grade manager
# python project
students=[]
name1=input("enter first student name:")
name2=input("enter second student name:")
name3=input("enter third student name:")
students.append(name1)
students.append(name2)
students.append(name3)
print("students:",students)
def get_grade(number):
  grade=float(input("grade"+str(number)+"(0-20):"))
  while grade<0 or grade>20:
   print("invalid grade!")
   grade=float(input("grade"+str(number)+"(0-20):"))
  return grade
grades=[]
for i in range(3):
 print("enter grades for",students[i])
 grade1=get_grade(1)
 grade2=get_grade(2)
 grade3=get_grade(3)
   
 grades.append([grade1,grade2,grade3])
for i in range(len(students)):
  student_grades=grades[i]
  average=sum(student_grades)/len(student_grades)
  if average>=16:
    result="exellent"
  elif average>=14:
    result="very good"
  elif average>=10:
    result="passed"
  else:
    result="failled"
  print("students:",students[i],"|average:",round(average,2),"|result:",result)
total=0
for student_grades in grades:
  average=sum(student_grades)/len(student_grades)
  total=total+average
class_average=total/len(grades)
print("class average:",round(class_average,2))
averages=[]
for student_grades in grades:
  average=sum(student_grades)/len(student_grades)
  averages.append(average)
print("highest average:",round(max(averages),2))
print("lowest average:",round(min(averages),2))
passed_students=0
for student_grades in grades:
  average=sum(student_grades)/len(student_grades)
  if average>=10:
    passed_students=passed_students+1
print("number of passed students:",passed_students)
top_index =averages.index(max(averages))
print("top student:",students[top_index],"-",round(averages[top_index],2))
failed_students=0
for student_grades in grades:
  average=sum(student_grades)/len(student_grades)
  if average<10:
    failed_students=failed_students+1
print("number of failed students:",failed_students)
print("===========================================")
print("students grade manager - END")
print("===========================================")