# 숫자 맞추기 게임 구현 - 2번째 시도

# 구현 방식 = 기본 로직 구현 + 정답 힌트 제공

import random

chance = 5
count = 0

randNumber = random.randint(1, 99)
print("1부터 99까지의 숫자를 5번 안에 맞춰 보세요.")

while count < chance : 
    #count = count +1
    count += 1
    user_input = int(input("숫자는 몇 일까요? "))

    if randNumber == user_input:
        break
    # 숫자를 맞추지 못한 경우에는 힌트를 제공하는 로직을 추가
    elif user_input < randNumber: 
        print("{} 보다 큰 숫자입니다.".format(user_input))
    elif user_input > randNumber: 
        print("{} 보다 작은 숫자 입니다.".format(user_input))

if user_input == randNumber:
    print("정답 : {} 이 맞습니다.".format(randNumber))
else : 
    print("실패, 정답은 {} 입니다.".format(randNumber))