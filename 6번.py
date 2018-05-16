engkor_dict = {}
eng = input("영어 입력: ")
kor = input("한글 입력: ")
while(eng !='' and kor !=''):
    engkor_dict[eng] = kor
    eng = input("영어 입력: ")
    kor = input("한글 입력: ")
print(engkor_dict)
