# 숫자 맞추기 게임 개발

# 기본 로직 구현 + 정답 힌트 제공 + 실행시마다 출력 내용 초기화 처리

import random
import os

chance = 5
count = 0

number = random.randint(1, 99)
os.system("cls")
print("1부터 99까지의 숫자를 {}번 안에 맞춰 보세요.".format(chance))

while count < chance : 
    count += 1
    user_input = int(input("숫자를 맞춰보세요 : "))

    if number == user_input : 
        break
    # 값을 맞추지 못한 경우에 대한 힌트 제공
    elif user_input < number : 
        print("{} 보다 큰 숫자입니다.".format(user_input))
    elif user_input > number :
        print("{} 보다 작은 숫자 입니다.".format(user_input))

if user_input == number : 
    print("정답 : {}이 맞습니다.".format(number))
else : 
    print("실패! 정답은 {} 입니다.".format(number))
