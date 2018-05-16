num = int(input(" 점수 : "))

if(100 >= num >= 90):
    print(num, ":", "A")
elif(89 >= num >=80):
    print(num, ":", "B")
elif(79 >= num >=70):
    print(num, ":", "C")
elif(69 >= num >=60):
    print(num, ":", "D")
elif(59 >= num >= 0): 
    print(num, ":", "F")
else:
    print("입력 가능한 점수 범위는 0~100 입니다")


