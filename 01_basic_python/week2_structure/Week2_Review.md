# Week2

---

최종적으로 학습을 보면 문법을 아는 데 순서(Flow)를 몰라서 스스로 문제를 풀이 할 때 코드가 꼬이는 경우가 많았습니다.

그래서 오늘은 Gemini 및 GPT의 도움을 받아 순서를 잡는 연습 ‘논리 수리’를 해보고 2주차 학습을 마칠 생각입니다.

---

- 
    1. 뒤죽 박죽 논리 맞추기
        1. 목표프로그램
            
            사용자가 숫자를 입력하면 10을 그 숫자로 나눕니다.(10 / 입력값)
            
            ```python
            '''
            [목표프로그램]
            1.사용자가 숫자를 입력하면 10을 그 숫자로 나눕니다.(10 / 입력값)
            2.계속 반복해야합니다.
            3.q를 누르면 꺼져야 합니다.
            4.0을 넣거나 한글을 넣으면 에러를 잡아야 합니다.
            '''
            '''
            1. 사용자가 숫자를 입력 : input
            2. 계속 반복의 경우 : while True
            3. q를 누르면 꺼짐 : if문 사용하여 조건 생성
            4. 0을 넣거나 한글을 넣으면 에러를 잡아야 함 : try-except
            '''
            ```
            
        2. 문제 : 해당 뒤섞인 코드를 제자리에 넣어보십시요.
            
            ```python
            try:
                num = int(text)
            while True:
                if text == 'q': break
            except:
                print("에러 발생! 숫자를 제대로 입력하세요.")
                print(10 / num)
                text = input("숫자를 입력하세요(종료:q): ")
            ```
            
        3. 정답
            
            ```python
            while True: 
                text = input("숫자를 입력하세요(종료:q): ") 
            
                if text == 'q': 
                    break
            
                try: 
                    num = int(text)     
                    print(10 / num)      
                    
                except:  
                    print("에러 발생! 숫자를 제대로 입력하세요.")
            			
            ```
            

---

1. 오류가 발생해도 종료되지 않는 단어장
    
    ```python
    '''
    [프로그램의 구조]
    1. 프로그램이 무한히 작동한다.
    	while True
    2. 사용자에게 메뉴를 보여 준다
    	[1] 단어 추가 [2] 단어장 보기(퀴즈) [3] 종료
    	print()
    3. 사용자가 선택한 번호에 따라 다른 행동을 한다.
    	if - elif - else
    	조건 1. 1번선택 -> 영어단어와 뜻을 입력받아 파일에 저장
    	(파일명과 'a' 추가 기능 사용)
    	조건 2. 2번 선택 -> 파일을 읽어와서 화면에 보여준다
    	(파일이 없을 시 에러가 날테니 try-exept 사용)
    	조건 3. 3번 선택 -> "안녕히 가세요"라는 단어와 반복문 종료
    	조건 4. 이상한 번호를 누르면 "없는 번호"라고 알려준다.
    '''  
    ```
    
    ```python
    while True : #조건이 참인 동안 계속 작동하게
        print(f"[1] 단어 추가, [2] 단어장 보기, [3]단어장 종료")
        num = input("원하시는 번호를 누르세요 :")
    
        if num == "1" :
            vocabulary = input("단어를 입력 하세요")
            with open("voca.txt", "a", encoding="utf-8") as v :
                v.write(f"{vocabulary}\n")
        
        elif num == "2" :
            try :
                with open("voca.txt", "r",encoding="utf-8") as re :
                    content = re.read()
                    print(content)
            except FileNotFoundError: # "파일이 없을 때만" 이 메시지를 띄움
                print("저장된 파일이 없습니다. 먼저 단어를 추가해주세요!")
            except Exception: # 그 외 알 수 없는 에러들
                print("알 수 없는 오류가 발생했습니다.")
        
        elif num == "3":
            print("안녕히 가세요")
            break
    
        else :
            print("존재하지 않는 목차입니다. 재실행하십시요")
    
    ```
    

---

1. 랜덤을 이용한 스무고개 만들기
    
    ```python
    import random
    
    # 1부터 50 사이의 랜덤 숫자 하나 뽑기
    secret_num = random.randint(1, 50)
    
    print("--- 1~50 사이의 숫자를 맞혀보세요! ---")
    
    while True:
        try:
            user_input = input("숫자 입력: ")
    
            guess = int(user_input) 
    
            if guess < secret_num:
                print("UP! (더 큰 숫자입니다)")
            
            elif guess > secret_num:
                print("DOWN! (더 작은 숫자입니다)")
                
            else:
                print(f"정답입니다! 숫자는 {secret_num}였습니다.")
                break
    
        except:
            print("에러! 한글이나 영어 말고 '숫자'만 입력하세요.")
    ```
    

---

Week2 학습(8~14일차) Ai 교차 정리(GPT, Gemini)

## **📅 학습 기간**

- 12월 2주차 (Day 8 ~ Day 14)

## **🎯 핵심 목표**

- 함수와 모듈의 이해
- 사용자 입력과 파일 저장(영구 보관)
- 예외 처리를 통한 방어적 프로그래밍 (Debugging Logic)
- 논리적 흐름 제어 (break, continue)

---

## **1. 사용자 입력 (Input)**

터미널(콘솔)을 통해 사용자와 소통하는 가장 기본적인 방법.

- **핵심:** input()으로 받은 모든 값은 **문자열(String)**이다.
- 계산을 하려면 반드시 int()나 float()로 형변환을 해야 한다.
- **주의:** 형변환 시 숫자가 아닌 값이 들어오면 에러가 발생하므로 방어 코드가 필요하다.

```python
name = input("이름: ")       # "홍길동" (문자열 유지)
age = int(input("나이: "))   # "20" -> 20 (정수로 변환)
```

---

## **2. 파일 입출력 (File I/O)**

프로그램이 종료되어도 데이터가 사라지지 않게 하드디스크에 저장하는 기술.

- with 구문: 파일을 열고(open) 나서 자동으로 닫아주는(close) 안전장치.
- 모드(Mode)
    - 'w': 덮어쓰기 (Write - 기존 내용 삭제)
    - 'a': 이어쓰기 (Append - 기존 내용 뒤에 추가)
    - 'r': 읽기 (Read)
- **Tip:** 텍스트 저장 시 encoding="utf-8"을 명시해야 한글이 깨지지 않는다.

```python
# 파일 쓰기 (줄바꿈 \n 포함)
with open("memo.txt", "a", encoding="utf-8") as f:
    f.write("오늘의 공부 기록\n")

# 파일 읽기
try:
    with open("memo.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()  # 한 줄씩 리스트로 읽기
except FileNotFoundError:
    print("읽을 파일이 없습니다.")
```

---

## **3. 예외 처리 (Exception Handling)**

에러가 발생해도 프로그램이 죽지 않게 만드는 안전벨트.

- 전략 (EAFP): “일단 실행해보고(Try), 문제 생기면 수습하자(Except).”
- **주의:** 모든 에러를 무작정 잡기보다, 예상되는 에러를 구체적으로 잡는 것이 좋다.

```python
try:
    num = int(input("숫자 입력: "))
    print(10 / num)
except ValueError:
    print("숫자가 아닙니다! 정수를 입력하세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except Exception as e:
    print(f"알 수 없는 에러 발생: {e}")
```

---

## **4. 흐름 제어 (Control Flow)**

반복문을 내 마음대로 조종하는 법.

- break: 반복문을 즉시 종료 (종료 조건)
- continue: 아래 코드는 건너뛰고 반복문 처음으로 이동 (스킵 조건)

```python
while True:
    cmd = input("명령어(exit/skip): ")

    if cmd == "exit":
        print("프로그램 종료")
        break

    elif cmd == "skip":
        print("이번 턴은 건너뜁니다.")
        continue

    print("명령어 실행 중...")
```

---

## **5. 표준 라이브러리 활용 (Random)**

파이썬 설치 시 기본으로 제공되는 유용한 도구들 (import 필요).

- random.randint(a, b): a부터 b 사이의 랜덤 정수 뽑기
- random.shuffle(리스트): 리스트의 순서를 무작위로 섞기

```python
import random

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
pick = random.randint(1, 100)
```

---

## **💡 이번 주 프로젝트 (Projects)**

### **1) 📖 나만의 영단어장 (My Voca)**

- 기능: 단어 추가(저장), 단어장 보기(불러오기), 랜덤 퀴즈
- 배운 점
    - 사용자의 입력은 언제나 예상과 다를 수 있다 → 문자열 처리의 중요성
    - try-except와 if문으로 오작동을 방어해야 한다

### **2) ⬆️⬇️ Up & Down 숫자 맞히기 게임**

- 기능: 컴퓨터가 생각한 숫자를 맞힐 때까지 반복
- 배운 점
    - while True + break 조합으로 게임 루프(Game Loop)를 만들 수 있다
    - 내가 짠 코드가 상호작용하는 재미를 느낌

---

## **🚀 KPT 회고 (Keep, Problem, Try)**

### **Keep (잘한 점)**

- 1일 1커밋 실천 중
- 코드가 안 돌아갈 때 포기하지 않고 끝까지 파고들어 해결함
- 프로그래밍이 “재밌다”는 감정을 느낌

### **Problem (부족했던 점)**

- 코드 실행 순서(Logic Flow)가 가끔 헷갈려 뒤죽박죽이 됨
- random 같은 표준 라이브러리의 존재/사용법을 많이 모름
- 자료형(문자열 vs 숫자) 차이로 인한 버그 발생

### **Try (시도할 점)**

- 모르는 문법/기능은 구글링으로 능동적으로 찾아보기
- “왜 안 되지?”에서 멈추지 말고 “어떻게 더 좋게 만들지?”까지 고민하기
- 다음 주 OOP(객체지향)도 겁먹지 말고 부딪혀보기

---

## **📝notion  Week 2 핵심 요약**

- **사용자 입력 처리:** input()은 항상 문자열을 반환하므로 계산 시 형변환 필요
- **파일 입출력:** with open()으로 데이터를 영구 저장하고, 'w'(덮어쓰기), 'a'(이어쓰기), 'r'(읽기) 모드 활용
- **예외 처리:** try-except로 에러 발생 시에도 프로그램이 종료되지 않도록 방어 코드 작성
- **흐름 제어:** break로 반복문 종료, continue로 현재 반복 건너뛰기
- **표준 라이브러리:** random 모듈로 랜덤 정수 생성 및 리스트 섞기 구현
- **실전 프로젝트:** 영단어장과 Up&Down 게임을 통해 while True + break 패턴과 사용자 상호작용 학습
- **주요 개선점:** 코드 실행 순서(Logic Flow) 이해 부족으로 논리 구조 연습 필요
- **다음 목표:** 능동적 학습 태도 유지하며 3주차 객체지향 프로그래밍(OOP) 도전