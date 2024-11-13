grade_list=[]
passed_list=[]
for num in range(5):
    x=int(input("Enter Grade: "))
    if x <=100 and x >=40:
        grade_list.append(x)
        if x >=75:
            passed_list.append(x)
    else:
        print("invalid garde(grade must be 40-100)")
        break
if len(grade_list)==5: 
    totalgrades=grade_list[0]+grade_list[1]+grade_list[2]+grade_list[3]+grade_list[4]
    average=totalgrades/5
    passpoint=len(passed_list)/5
    passaverage=passpoint*100
    print(f"Number of students that passed: {len(passed_list)}")
    print(f"Percentage of students passed: {(passaverage)}%")
    print(f"Average Grade: {(average)}")
    print(f"Grades list: {(grade_list)}")