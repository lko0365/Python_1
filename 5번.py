items = {"라면" : 650, "우유" : 1100, "콜라" : 1200, "캔커피" : 500, "과자" : 700 }
sum = 0
while True:
    k = input("제품명 :")
    if k in items:
        sum += items[k]
        print(k, ":", items[k], ">", sum)
    else:
        break
print(k,"는 미등록 제품입니다.")
print("제품명: ")
print("총 금액: ",sum)
