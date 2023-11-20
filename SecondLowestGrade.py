n=int(input('Number of students: '))
studentinfo=[]
grade=[]
compare=0
winners=[]
for information in range(n):
    student_name=input('')
    grades=float(input(''))
    grade.append(grades)
    studentinfo.append([student_name, grades])

grade=list(set(grade))
grade.sort()
compare=grade[1]
#[nil,3.5],[kookok,3.3],[kjjoj,3.9]
for i in range(len(studentinfo)):
    if compare in studentinfo[i]:
        winners.append(studentinfo[i][0])
winners.sort()        
print(winners)
        
#Print the name(s) of any student(s) having the second 
# lowest grade in. If there are multiple students, order
#  their names alphabetically and print each one on a new line.
#input
#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39

#output
#berry
#harry


    