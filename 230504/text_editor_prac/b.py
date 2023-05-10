# f = open("test.txt", 'r', encoding='utf-8')
# a = f.read()
# print(a)
# f.close()


"""
test.txt 의 내용을 test_dummy.txt 로 복사하기
"""
f = open("test.txt", 'r', encoding = "utf-8")
a = f.readlines() # 해당 위치에서 전체 내용 행렬로 리스트 부르기
print(a)
f1 = open("test_dummy.txt", 'w', encoding = "utf-8")
for i in a:
    data = i + '\n'
    f1.write(i)
f.close()
f1.close()

# f = open("test.txt", 'r', encoding = "utf-8")
# i = 0
# while True:
#     line = f.readline() # line을 하면 개행문자를 함께 내보내지만
#     if not line:
#         break
#     print(line)
#     i = i + 1
#     print(i) # 단순히 변수만 출력할 때는 개행문자가 포함되지 않는다.
# f.close()


# f = open("test.txt", 'r', encoding = "utf-8")
# i = 0
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line.replace("\n", "")) # 이것도 왠지 쓸 거 같은데???
#     i = i + 1
# f.close()
# print(i)


"""
파일 안 글자의 통계정보 출력하기
"""

f = open("test.txt", 'r', encoding = "utf-8")
contents = f.read()
word_list = contents.split(" ")
line_list = contents.split("\n")

print("총 글자 수: ", len(contents)) # 공백포함
print("총 단어의 수: ", len(word_list))
print("총 줄의 수: ", len(line_list))

f = open("test2.txt", 'r', encoding = 'utf-8')
f_out = open("out_test.txt", 'w', encoding = 'utf-8')
count = 1
while True:
    line = f.readline()
    if not line: #공백이라면, c++ 에서는 void라면
        break
    if '태풍' in line:
        for i in range(line.count("태풍")): # for i in range(line.count("태풍")): 태풍이 있는 개수만큼
            line = line.replace("태풍", "{}) 햇빛".format(count).1)
            f_out.write(line)
            count += 1
        print(line)

f_out.close()
f.close()