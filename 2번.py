index = input("문자열 : ")
def reverse(index):
    rev = ''
    for i in range(len(index) -1, -1, -1):
            rev += index[i]
    return rev

print("개별 문자열 출력 :", index)
print("역순 개별 문자 출력:", reverse(index))
