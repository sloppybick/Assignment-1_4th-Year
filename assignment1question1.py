z=open("grade.txt")
def exam(inc1,inc2,attrendance,final):
    average=(inc1+inc2)/2
    avg_attendance=average+attrendance
    if final<0 or final>70:
        return "please enter a number below 70"
    else:
       marks=avg_attendance+final
    if marks>=80:
        return 4.00,'A+'
    elif marks>=75:
        return 3.75,'A'
    elif marks>=70:
        return 3.50,'A-'
    elif marks>=65:
        return 3.25,'B+'
    elif marks>=60:
        return 3.00,'B'
    elif marks>=55:
        return 2.75,'B-'
    elif marks>=50:
        return 2.50,'C+'
    elif marks>=45:
        return 2.25,'C'
    elif marks>=40:
        return 2.00,'D'
    else:
        return 0.00,'F'
    
student_data=[]    
for line in z:
    data=line.split()
    roll=int(data[0])
    inc1=float(data[1])
    inc2=float(data[2])
    attendance=int(data[3])
    final=float(data[4])
    gradepoint,letter_grade=exam(inc1,inc2,attendance,final)
    student_data.append([roll,gradepoint,letter_grade])

print(f"{'Roll':<12}{'Gradepoint':<20}{'Lettter_grade':<20}")

for data in student_data:
        roll,gradepoint,letter_grade=data
        print(f"{roll:<12}{gradepoint:<20}{letter_grade:<20}")   
        