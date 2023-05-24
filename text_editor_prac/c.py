f = open("depth02_template_b.feb", 'r', encoding = "utf-8")
a = f.readlines() # 해당 위치에서 전체 내용 행렬로 리스트 부르기
print(a)
f1 = open("test_dummy.feb", 'w', encoding = "utf-8")
for i in a:
    data = i + '\n'
    f1.write(i)
f.close()
f1.close()