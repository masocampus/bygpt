# 반복 구조 - 같은 일은 효율적으로!
# - 조건을 만족하는 동안 같은 스텝을 반복해서 처리함

# 예제)
# 01 - 당면을 산다
# 02 - 거스름돈이 1,200원보다 많으면 계속 붕어빵을 산다
# 03 - 거스름돈이 1,200원보다 적으면 집으로 되돌아 온다

# 흐름의 제어 - 반복문

# 반복문의 종류
# for - 몇 회 반복할 것인지 미리 알고 있을 때 사용. 예) 1 ~ 100의 토탈값 집계
# while - 몇 회 반복할 지 미리 알고 있지 못하는 경우에 주로 활용

# for 문 기본 형식
# 지정한 범위 만큼 반복
# 형식
# for 변수 in range(시작값, 끝값+1, 증가값) : 
#       실행문

# while 문 기본 형식
# 조건식이 참일 때 반복
# 형식
# while 조건식 : 
#       실행문

# pseudo code 
# 달걀이 깨지면 거짓 => 실행 중지함
# while 달걀이 안깨졌음
#   한 층 더 올라간다
#   달걀을 떨어뜨린다

# 반복문 for 문 연습
# Hello 김찬우를 10회 출력하기
for i in range(0, 10) : 
    print("Hello 김찬우")

# 1 ~ 100까지 더하면 어떤 값이 나올까? 
# tot_num = 0
# for i in range(1, 101) : 
#     tot_num = tot_num + i  
# print("1에서 100까지의 합은 : {}".format(tot_num))

# 주요 코드 해석연습
# tot_num = 0에서 tot_num을 0이라고 초기화를 설정한 이유
# 초기화를 진행하지 않았다면, 최초의 tot_num 변수 값은 공백(undefined)가 됨
# 공백 +1이라는 연산을 진행할 수 없기 때문에 초기값으로 반드시 tot_num =0을 지정해야 함
# 지정하지 않는 경우 "name 'tot_num' is not defined"라는 오류가 발생하게 됨

# 변수 이해를 돕기 위한 코딩 연습
# b = 1
# result = a + b # a에 할당된 값이 없기 때문에 무엇을 더해야 하는지 모르는 상황

# 500과 1000 사이의 홀수 합계 구하기
# tot_num = 0 
# for i in range(501, 1001, 2) :
#     tot_num = tot_num + i
# print("500과 1000 사이에 있는 홀수의 합계 : {:,}".format(tot_num))


