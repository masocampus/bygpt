# 자료구조란 무엇인가? 

# 자료구조 - 프로그램에서 데이터를 체계적으로 담는 그릇
# 데이터를 묶음으로 들고 다니기 위한 그릇

# 자료구조(Data Structure) = 데이터 묶음으로 처리하는 그릇

# 예1) 락액락_레인보우_컵 = [물, 콜라, 오렌지주스] - 리스트(List)

# 예2) 리빙앳홈_식판 = {"좌하":"밥", "우하":"바나나", "좌상":"샐러드"
#                       "중상":"방울토마토", "우상":"김치"} - 딕셔너리(Dictionary)
# 딕셔너리 : key:value 쌍으로 이루어진 데이터 구조

# 사용 형식
# 변수명 = 자료구조 데이터
# 변수 활용방법과 동일함

# 리스트 - List 연습하기

# 변수 사용하기 - 리스트 자료구조의 필요성 이해
a = 10
b = 20
c = 30
d = 40

print(a, b, c, d)

# 리스트 사용하기
aa = [10, 20, 30, 40]
print(aa, type(aa))

bb = [10, 'a', True]
print(bb, type(bb))

# 리스트 안의 특정 항목(item) 가져오기
cc = [10, 20, 30, 40]
print(cc[0], cc[1], cc[2], cc[3])

# 사과, 배, 포도, 딸기가 담긴 과일 리스트를 만들어보자
fruit = ['사과', '배', '포도', '딸기']
print(fruit)

# 딕셔너리(Dictionary)
# 순서가 없는 여러 개의 Key-Value 집합, Key는 Unique
# {"key1":value1, "key2":value2, ...}

# 딕셔너리(Dictionary)
# 사전과 같이 key & value 쌍을 모아놓은 자료 구조.
# key 기준으로 검색이 가능함
# {"key1":value1, "key2":value2, ...}
# 타 언어의 Map과 동일

# Dictionary 정의하기 및 검색하기

student = {"학번":1000, "이름":"마소캠퍼스", "전공":"데이터사이언스"}
print(student)

# key로 검색하기
print(student["학번"])
