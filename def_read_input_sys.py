#문제 1-1: 간단한 함수 정의
#문제 : 두 수를 더하는 함수 `add(a, b)`를 만들어 호출해 보세요.

def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# 문제 1-2: 여러 인자를 받는 함수
# 문제: 세 수의 평균을 구하는 함수 `average(a, b, c)`를 만들어 호출하세요.

def average(a, b, c):
    return (a + b + c) / 3

avg = average(10, 20, 30)
print(avg)  # 출력: 20.0

# 문제 1-3: 기본값(default argument) 있는 함수
# 문제 : 인사말을 출력하는 함수를 만드세요. 이름을 받으면 "○○님 안녕하세요", 받지 않으면 "안녕하세요"를 출력합니다.

def greet(name="손님"):
    print(f"{name}님 안녕하세요")

greet()      
greet("지민")  


# 문제 1-4: 여러 값을 반환하는 함수
# 문제 : 두 수를 입력받아 합, 곱, 차를 모두 반환하는 함수를 만드세요.

def calculate(a, b):
    sum_val = a + b
    mul_val = a * b
    diff_val = a - b
    return sum_val, mul_val, diff_val

s, m, d = calculate(5, 3)
print(f"합: {s}, 곱: {m}, 차: {d}")  

# 문제 1-5: 리스트를 처리하는 함수
# 문제 : 리스트의 모든 원소를 더하는 함수 `sum_list(numbers)`를 만드세요.

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = sum_list([1, 2, 3, 4, 5])
print(result) 

result = sum([1, 2, 3, 4, 5])
print(result)

# 문제 2-1: input() 함수로 입력받기
# 문제 : 사용자로부터 이름을 입력받아 인사말을 출력하세요.

name = input("이름을 입력하세요: ")
print(f"안녕하세요, {name}님!")

# 문제 2-2: 숫자 입력받아 계산하기
# 문제 : 두 숫자를 입력받아 합을 구하세요.

a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))
print(f"합: {a + b}")

# 문제 2-3: 여러 입력을 한 줄에서 받기
# 문제 : "이름 나이"를 한 줄에 입력받아 출력하세요.

info = input("이름과 나이를 입력하세요 (예: 지민 15): ")
name, age = info.split()
print(f"이름: {name}, 나이: {age}")


# 문제 2-4: 조건에 따른 출력
# 문제 : 나이를 입력받아 "미성년자"인지 "성인"인지 판별하세요.

age = int(input("나이를 입력하세요: "))

if age >= 18:
    print("성인입니다")
else:
    print("미성년자입니다")


# 문제 3-1: sys.argv로 명령행 인자 받기
# 문제: 다음 코드를 저장하고 터미널에서 실행하세요.

# greeting.py
import sys

print("프로그램 이름:", sys.argv[0])
print("전체 인자:", sys.argv)
print("인자 개수:", len(sys.argv))
'''
터미널에서 실행:

python greeting.py hello world
'''

# 문제 3-2: sys.argv를 이용한 더하기 프로그램
# 문제 : 명령행에서 받은 숫자들을 모두 더하는 프로그램을 만드세요.

# add_args.py
import sys

if len(sys.argv) < 2:
    print("사용법: python add_args.py 숫자1 숫자2 ...")
else:
    total = 0
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print(f"합: {total}")

'''
터미널에서 실행:
python add_args.py 10 20 30
'''

# 문제 3-3: sys.exit()로 프로그램 종료
# 문제: 비밀번호를 확인하고 틀리면 프로그램을 종료하세요.

import sys

password = input("비밀번호를 입력하세요: ")

if password == "1234":
    print("접근 허용")
else:
    print("비밀번호가 틀렸습니다!")
    sys.exit()  # 프로그램 즉시 종료

print("이 메시지는 출력되지 않습니다")

# 문제 4-1: 파일에 글 쓰기 (write mode)
# 문제 : "hello.txt" 파일을 만들어 "Hello, Python!"을 저장하세요.

# 파일 쓰기
f = open("hello.txt", "w")
f.write("Hello, Python!")
f.close()

print("파일이 저장되었습니다")

# 문제 4-2: 파일 읽기 (read mode)
# 문제 : 위에서 저장한 "hello.txt"를 읽어 출력하세요.

# 파일 읽기
f = open("hello.txt", "r")
content = f.read()
f.close()

print(content)  # 출력: Hello, Python!

# 문제 4-3: 파일을 라인 단위로 읽기
# 문제: 여러 줄의 텍스트 파일을 읽어 각 줄을 출력하세요.

# 먼저 파일 생성
f = open("lines.txt", "w")
f.write("첫 번째 줄\n")
f.write("두 번째 줄\n")
f.write("세 번째 줄\n")
f.close()


#파일 읽기:
f = open("lines.txt", "r")
lines = f.readlines()  # 모든 줄을 리스트로 반환
f.close()

for i, line in enumerate(lines, 1):
    print(f"{i}. {line}", end="")  # 이미 \n 포함


# 문제 4-4: with 문을 이용한 안전한 파일 처리
# 문제: with 문을 사용해 파일을 읽고 쓰세요.

# 파일 쓰기
with open("data.txt", "w") as f:
    f.write("안녕하세요\n")
    f.write("파이썬입니다\n")

# 파일 읽기
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# 문제 4-5: 파일에 숫자 저장 및 계산
# 문제 : 사용자가 입력한 숫자들을 파일에 저장하고, 저장된 숫자들의 합을 구하세요.

# 숫자 저장
with open("numbers.txt", "w") as f:
    for i in range(3):
        num = int(input(f"{i+1}번째 숫자: "))
        f.write(str(num) + "\n")

# 숫자 읽고 합 계산
total = 0
with open("numbers.txt", "r") as f:
    for line in f:
        num = int(line.strip())  # \n 제거 후 정수 변환
        total += num

print(f"합: {total}")

# 문제 4-6: 파일에서 단어 검색
# 문제: 텍스트 파일에서 특정 단어가 몇 번 나타나는지 세세요.

# 파일 생성
with open("poem.txt", "w") as f:
    f.write("파이썬 파이썬 파이썬\n")
    f.write("프로그래밍은 재미있다\n")
    f.write("파이썬으로 배우자\n")

# 단어 검색
with open("poem.txt", "r") as f:
    content = f.read()
    count = content.count("파이썬")
    print(f"'파이썬'이 {count}번 나타났습니다")


# 🎯 연습 문제: 종합 프로젝트

## 문제: 간단한 학생 성적 관리 프로그램
'''
1. 학생 이름과 성적을 입력받기
2. 성적을 "scores.txt"에 저장
3. 파일에서 읽어 평균 계산
4. 함수를 사용해 학점 판정 (A: 90~, B: 80~, C: 70~, D: 60~, F: 0~59)
'''
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 성적 입력 및 저장
with open("scores.txt", "w") as f:
    name = input("학생 이름: ")
    score = int(input("성적: "))
    f.write(f"{name},{score}\n")

# 파일에서 읽고 분석
total = 0
count = 0
with open("scores.txt", "r") as f:
    for line in f:
        name, score = line.strip().split(",")
        score = int(score)
        grade = get_grade(score)
        print(f"{name}: {score}점 ({grade}학점)")
        total += score
        count += 1

average = total / count
print(f"평균: {average:.1f}점")