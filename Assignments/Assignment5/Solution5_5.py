#5. Write a program to calculate the total score of all students 
student_score = {1: 44, 2: 45, 3: 55}
def sum_ofscore(student_score):
    sum=0
    for keys,value in student_score.items():
        sum+=value
    return sum

res=sum_ofscore(student_score)
print(res)