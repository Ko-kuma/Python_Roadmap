# 1️⃣ if문 문제

# 문제 1-1: 숫자 비교
#문제: 두 숫자를 입력받아 더 큰 숫자를 출력하세요.

a = 10
b = 20

if a > b:
    print(f"{a}가 더 큽니다.")
else:
    print(f"{b}가 더 큽니다.")

# 출력: 20가 더 큽니다.

# 문제 1-2: 홀수/짝수 판별
# 문제: 입력받은 숫자가 홀수인지 짝수인지 판별하세요.

num = 15

if num % 2 == 0:
    print(f"{num}은 짝수입니다.")
else:
    print(f"{num}은 홀수입니다.")

# 출력: 15은 홀수입니다.

#문제 1-3: 학점 계산
'''
문제: 점수를 입력받아 학점을 출력하세요.
- 90점 이상: A
- 80점 이상: B
- 70점 이상: C
- 그 외: F
'''
score = 85

if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
elif score >= 70:
    print("학점: C")
else:
    print("학점: F")

# 출력: 학점: B

# 문제 1-4: 나이 확인
# 문제: 나이를 입력받아 성인인지 미성년자인지 판별하세요. (18세 이상: 성인)

age = 20

if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# 출력: 성인입니다.

# 문제 1-5: 세 수 중 최댓값 찾기
#문제: 세 개의 숫자 중 가장 큰 수를 찾으세요.

a, b, c = 10, 25, 15

if a > b and a > c:
    max_num = a
elif b > a and b > c:
    max_num = b
else:
    max_num = c

print(f"최댓값: {max_num}")

# 출력: 최댓값: 25

# for문 문제

# 문제 2-1: 1부터 5까지 출력
# 문제: for문을 사용하여 1부터 5까지 출력하세요.

for i in range(1, 6):
    print(i)

# 출력:
# 1
# 2
# 3
# 4
# 5

# 문제 2-2: 구구단 (2단)
# 문제: 2단 구구단을 출력하세요.

for i in range(1, 10):
    print(f"2 × {i} = {2 * i}")

# 출력:
# 2 × 1 = 2
# 2 × 2 = 4
# 2 × 3 = 6
# ...
# 2 × 9 = 18


# 문제 2-3: 리스트 순회
# 문제: 주어진 리스트의 모든 요소를 출력하세요.

fruits = ["사과", "바나나", "포도", "딸기"]

for fruit in fruits:
    print(fruit)

# 출력:
# 사과
# 바나나
# 포도
# 딸기

# 문제 2-4: 합계 계산
# 문제: 1부터 10까지의 합계를 구하세요.

total = 0

for i in range(1, 11):
    total += i

print(f"합계: {total}")

# 출력: 합계: 55

# 문제 2-5: 구구단 전체 (이중 for문)
# 문제: 2단부터 9단까지의 구구단을 출력하세요.

for dan in range(2, 10):
    for num in range(1, 10):
        print(f"{dan} × {num} = {dan * num}", end="  ")
    print()  # 줄바꿈

# 문제 2-6: 개수 세기
# 문제: 리스트에서 3보다 큰 숫자의 개수를 세세요.

numbers = [1, 2, 3, 4, 5, 6, 7]
count = 0

for num in numbers:
    if num > 3:
        count += 1

print(f"3보다 큰 숫자의 개수: {count}")

# 출력: 3보다 큰 숫자의 개수: 4

## while문 문제

# 문제 3-1: 1부터 5까지 출력
# 문제: while문을 사용하여 1부터 5까지 출력하세요.

i = 1

while i <= 5:
    print(i)
    i += 1

# 출력:
# 1
# 2
# 3
# 4
# 5

# 문제 3-2: 숫자 맞추기
# 문제 : 정해진 숫자(예: 5)를 맞추는 게임. 입력받은 숫자가 정답과 같을 때까지 반복하세요.

answer = 5
guess = 0

while guess != answer:
    guess = int(input("숫자를 맞춰보세요 (1-10): "))
    if guess < answer:
        print("더 큰 숫자입니다.")
    elif guess > answer:
        print("더 작은 숫자입니다.")
    else:
        print("정답입니다!")

# 실행 예:
# 숫자를 맞춰보세요 (1-10): 3
# 더 큰 숫자입니다.
# 숫자를 맞춰보세요 (1-10): 7
# 더 작은 숫자입니다.
# 숫자를 맞춰보세요 (1-10): 5
# 정답입니다!

# 문제 3-3: 합계 계산
# 문제: 입력받은 숫자들의 합계를 구하세요. (음수 입력 시 종료)

total = 0

while True:
    num = int(input("숫자를 입력하세요 (음수 입력 시 종료): "))
    
    if num < 0:
        break
    
    total += num

print(f"합계: {total}")

# 실행 예:
# 숫자를 입력하세요 (음수 입력 시 종료): 10
# 숫자를 입력하세요 (음수 입력 시 종료): 20
# 숫자를 입력하세요 (음수 입력 시 종료): 30
# 숫자를 입력하세요 (음수 입력 시 종료): -1
# 합계: 60

# 문제 3-4: 팩토리얼 계산
# 문제: 입력받은 숫자의 팩토리얼을 계산하세요.

n = 5
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"{n}! = {factorial}")

# 출력: 5! = 120

# 문제 3-5: 구구단 (2단, while 사용)
# 문제: while문을 사용하여 2단 구구단을 출력하세요.

dan = 2
num = 1

while num <= 9:
    print(f"2 × {num} = {2 * num}")
    num += 1

# 출력:
# 2 × 1 = 2
# 2 × 2 = 4
# 2 × 3 = 6
# ...
# 2 × 9 = 18

# 문제 3-6: 별 출력 (while문 활용)
# 문제: 다음과 같은 패턴을 출력하세요.
'''
*
**
***
****
*****
'''

i = 1

while i <= 5:
    print("*" * i)
    i += 1

# 출력:
# *
# **
# ***
# ****
# *****

# 혼합 문제

# 문제 4-1: if와 for 함께 사용
# 문제: 1부터 20까지의 숫자 중 3의 배수를 출력하세요.

for i in range(1, 21):
    if i % 3 == 0:
        print(i, end=" ")

# 출력: 3 6 9 12 15 18

# 문제 4-2: if와 while 함께 사용
# 문제: 1부터 100까지 더한 후, 합계가 500을 넘으면 종료하세요.

total = 0
i = 1

while True:
    total += i
    
    if total > 500:
        print(f"{i}를 더했을 때 합계({total})가 500을 넘었습니다.")
        break
    
    i += 1

# 출력: 33를 더했을 때 합계(561)가 500을 넘었습니다.

# 문제 4-3: for, while, if 모두 사용
# 문제: 1부터 3단 구구단까지 출력하되, 결과가 10 이상인 것만 출력하세요.

for dan in range(1, 4):
    num = 1
    while num <= 9:
        result = dan * num
        if result >= 10:
            print(f"{dan} × {num} = {result}")
        num += 1

# 출력:
# 2 × 5 = 10
# 2 × 6 = 12
# 2 × 7 = 14
# 2 × 8 = 16
# 2 × 9 = 18
# 3 × 4 = 12
# 3 × 5 = 15
# ...