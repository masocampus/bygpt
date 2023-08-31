# 게임 기본 구현하기

# A, B 두 사람이 주사위를 던져서 더 큰 수가 나오면 이기는 게임을 구현해보자

# 구현 프로세스 - Pseudo Code(수도 코드 - 의사 코드)
# 1. A가 주사위를 던진다
# 2. B가 주사위를 던진다
# 3. A, B가 던진 주사위 결과를 비교한다. 
#    --> Case 정리 : A가 이긴다, B가 이긴다, A/B가 비긴다

import random

user_a = int(input("1을 입력하면 A 주사위가 던져집니다 : "))
if user_a == 1 :
    dice_a = random.randrange(1, 7)
    print("A가 던진 주사위 숫자는 {} 입니다.".format(dice_a))

user_b = int(input("2를 입력하면 B 주사위가 던져집니다 : "))
if user_b == 2 : 
    dice_b = random.randrange(1, 7)
    print("B가 던전 주사위 숫자는 {} 입니다.".format(dice_b))

print("*****"*15)
print("A가 던진 주사위 숫자는 {}, B가 던진 주사위 숫자는 {} 입니다.".format(dice_a, dice_b))

# 승리 판단 코드 구현
if dice_a > dice_b : 
    print("A가 이겼습니다!")
elif dice_a < dice_b : 
    print("B가 이겼습니다!")
else : 
    print("A/B는 비겼습니다!")

