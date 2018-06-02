#----------------------------------------------
#Name: Grades
#Purpose: To calculate grade and letter grade based on averages
#Author: Alex Park
#Date: 10/1/17
#----------------------------------------------
"""
Input as many grades as prompted, then select end and the
GPA based on a 100 point scale will be printed along
with its assigned letter grade and all the grades, below.
The lowest grade will be dropped if there are 4 or more
grades inputted into the list. Floats are accepted.
"""
grades=[]
MIN_GRADE_TO_DROP = 4
while(True):
    value = input("Please enter grade:")
    if(value =='end'): #check for ending
        break
    else:
        value = float(value)
        if(value>100 or value<0):#check for invalid grades
            print('Invalid Grade')
        else:
            grades.append(value)

size = len(grades) #save the size in a variable
if(size>=MIN_GRADE_TO_DROP):
    grades.remove(min(grades))# drop the lowest grade
    size -= 1

gpa = round(sum(grades)/size,1)#calculate GPA and round it

print('Course Average:',gpa)
#check for grade and its letter using if statements
letter = ''
if(gpa>=0 and gpa<60):
    letter = 'F'
elif(gpa>=60 and gpa<70):
    letter = 'D'
elif(gpa>=70 and gpa<80):
    letter = 'C'
elif(gpa>=80 and gpa<90):
    letter = 'B'
else:
    letter = 'A'
print('Letter Grade:',letter)
print('Based on grades:')
for element in grades:#print each element in the grade list
    print(element)



