engkor_dict = {}
eng = input("���� �ܾ� :")
print("������ ��� �ֽ��ϴ�.")
print("�ܾ �߰��մϴ�.")
kor = input("�ѱ� �ܾ� :")
engkor_dict[eng] = kor
while True:
    eng = input("���� �ܾ� :")
    if(eng == ''):
        break
    else:
        if eng in engkor_dict:
            print("�ѱ� �ܾ� :",engkor_dict[eng])
            continue
        else:
            print(eng,"�ܾ ��ϵǾ� ���� �ʽ��ϴ�.")
            print("�ܾ �߰��մϴ�.")
            kor = input("�ѱ� �ܾ� :")
            engkor_dict[eng] = kor
            continue
        break

print(engkor_dict)
