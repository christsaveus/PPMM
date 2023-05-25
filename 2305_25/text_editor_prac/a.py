#To edit the <MeshDomains>
# 저장할 변수명 = open("파일 이름", "모드")
# 변수명.close();

# r 파일을 읽기 모드 
# w 파일을 쓰기 모드로 열기/파일생성
# a 파일에 내용 추가하기 / 파일 생성
# 텍스트 모드로 파일 열기
# 바이너리 모드로 파일 열기
# r+ 읽기 + 쓰기 모드, 덮어쓰기로 파일을 쓴다.
# w+ 읽기 + 쓰기 모드, 기존의 파일을 지우고 파일을 쓴다. 
# a+ 읽기 + 쓰기 모드, 기존의 파일 끝에서부터 파일을 쓴다. 파일 생성

# f = open("test.txt", 'w') # 파일 열기
# f.write("파이썬 월드1231")
# f.close()
# test.txt 파일이 생성됨

# with open("test2.txt", 'w') as f:
#     f.write('파이썬 월드\n')
#     # with를 쓴다면 close로 escape할 필요가 없음
#     f.write("파이썬 월드2")

"""
여러 개의 리스트를 한 줄에 쓰기
"""
# f = open("test.txt", 'w')
# f.writelines(["파이썬", "배우기"]) # test.txt 라는 파일에 "파이썬배우기"로 바뀜
# f.close()

# data = "에 오신 것을 환영합니다."
# f = open('test3.txt', 'a') # 파일에 내용 추가하기
# f.write(data)
# f.close()


"""
나한테는 이게 진짜 중요
"""

# n = 0
# f = open("test4.txt", 'w')
# while n < 10:
#     data = "%d 숫자\n"%n
#     f.write(data)
#     n = n + 1

# f.close()

# n = 0
# f = open("test5.txt", 'w')
# while n < 10:
#     if n == 9:
#         data = "%d 숫자"%n
#         f.write(data)
#         break
#     data = "%d 숫자\n"%n
#     f.write(data)
#     n = n + 1
# f.close()

# n = 1
# f = open("loop.txt", 'w')
# while n < 101:
#     data = "%d "%n
#     f.write(data)
#     n = n + 0.5
# f.close()


# n = 1
# f = open("loop.txt", 'w')
# while n < 101:
#     data = str(n) + " "
#     f.write(data)
#     n = n + 1
# f.close()


f = open('test.txt', 'w', encoding = 'utf-8') #밑에 \n\에서 두번째 left slash는 함수가 밑에 더 이어질 것임을 의미한다.
f.write("I have a dream, a song to sing\n\
To help me cope with anything\n\
If you see the wonder of a fairy tale\n\
You can take the future even\n\
if you fail I believe in angels\n\
Something good in everything")
f.close()