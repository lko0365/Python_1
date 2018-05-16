engkor_dict = {}
eng = input("영어 단어 :")
print("사전이 비어 있습니다.")
print("단어를 추가합니다.")
kor = input("한글 단어 :")
engkor_dict[eng] = kor
while True:
    eng = input("영어 단어 :")
    if(eng == ''):
        break
    else:
        if eng in engkor_dict:
            print("한글 단어 :",engkor_dict[eng])
            continue
        else:
            print(eng,"단어가 등록되어 있지 않습니다.")
            print("단어를 추가합니다.")
            kor = input("한글 단어 :")
            engkor_dict[eng] = kor
            continue
        break

print(engkor_dict)
