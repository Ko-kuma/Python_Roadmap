# Day1~7 보강학습

---

- 복습 체크리스트
    - Day1(Git 환경 설정 및 오류)
        - [x]  Git 기본 동작 (git add . , git commit, git push가 어떤 역할을 하는지 설명 가능한지?
        - [x]  Git 오류 non-fast-forward오류 발생 시, git pull --non-rebase명령을 사용할 수 있는가?
    - Day2(변수/자료형)
        - [x]  숫자형(int)과 문자열(str)의 차이점, type()으로 자료형을 확인 할 수 있는가?
    - Day3(조건문)
        - [x]  if, elif, else 구조와 들여쓰기의 중요성을 아는가? 90점 이상 A학점 판별 코드를 짤 수 있는가?
    - Day4(반복문)
        - [x]  for문과 while문의 차이점은? range(5)가 0부터 4까지 반복한다는 것을 이해하는가?
    - Day5/6(리스트)
        - [x]  리스트 [ ] 안에 여러 자료형을 담을 수 있는가? for item in list : 구문으로 리스트를 순회 할 수 있는가?

---

1. Day 1 복습 과 부족 부분 보강 및 상세 정리
    - 1일차 내용을 보려면 클릭
        1. Git 기본 동작의 이해 
            
            
            | Git | 의 분류 |
            | --- | --- |
            | 분류 | 설명 |
            | Working Directory | 실제 파일이 있는 곳(수정 중인 상태) |
            | Staging Area(인덱스) | 커밋 후보로 올려 놓는 임시 공간 |
            | Local Repository | 내가 가진 커밋(버전)들이 저장되는 곳 |
            | Remote Repository | GitHub, GitLab 같은 서버 저장소 |
            
            | 각 | 명령어의 역할 |
            | --- | --- |
            | git add. | 현재 디렉토리( . ) 아래에서 변경된 파일들을 
            Staging Area(스테이지)로 올립니다. |
            | git commit -m “메시지” | 스테이징 된 파일들을 
            하나의 커밋(버전)으로 기록합니다.
            ”현재까지의 상태를 스냅샷으로 저장”
            하는 작업입니다. |
            | git push origin main(또는 master) | 내 로컬 저장소의 커밋들을 
            원격 저장소의 해당 브랜치로 업로드 합니다.
            팀원이나 다른 컴퓨터에서
            이 커밋을 볼 수 있게 되는 단계입니다. |
        2. non-fast-forward 오류와 git pull 관련
            
            non -fast - forward에러는 보통 이런 상황에서 발생합니다.
            
            - 원격브랜치에 이미 새로운 커밋이 있는데 내 로컬 브랜치에는 그 커밋이 없을 때
                
                이 상태에서 git push를 하면 ”원격이 앞으로 더 나가 있는데, 그 상태에서 무시하고 덮어쓰게 되니 안된다(non-fast-forward)” 라고 막는것.
                
            
            해결 기본 원리
            
            1. 먼저 기본원리 원격 저장소의 변경을 내 로컬로 가져오고(=pull)
            2. 충돌이 나면 해결한 뒤
            3. 다시 git push
            
            일반적인 해결 명령
            
            ```bash
            git pull #기본은 merge 방식
            git pull --rebase #rebase 방식으로 깔끔한 히스토리 유지
            git push 
            ```
            
        3. 개념정리 
            - --no-rebase는 “rebase 말고 merge 방식으로 pull 하겠다”는 의미 입니다.
            - non-fast-forward 오류 해결의 핵심
                - “원격의 커밋을 먼저 내 로컬에 가져온다”는 점
                - 이걸 merge로 할 지(rebase 안 함) / rebase로 할 지(rebase 함)는 스타일 차이입니다.
        4. 결론 
            - git pull(기본), git pull --no-rebase, git pull --rebase 모두 non-fast-foward 상황에서 사용할 수 있습니다.
            - 다만, non-fast-forward면 반드시 --no-rebase를 써야한다는 건 아닙니다.
            - 가장 흔한 패턴은
            
            ```bash
            git pull --rebase #요즘 많이 사용하는 방식
            git push
            ```
            
        5. Ai 교차검증을 통한 부족한 부분에 대한 보강
            - 용어 정리
                - Branch 한 저장소 안에서 갈라져 나온 작업라인 / 작업 줄기
                - Merge는 단어의 뜻 대로 합친다, 융합한다는 의미 입니다.
                - Merge는 branch를 통합하는 것 입니다.
                - Rebase는 내 branch의 시작점을 다른 branch의 최신 상태로 옮기는 것
                - Rebase는 말 그대로 “기반(base)을 다시잡기(re-base)”
            - 초보자에게는 git pull --no-rebase(merge)가 훨씬 안전합니다.
            - 이유는 rebase는 타임머신을 타고 과거를 조작하는 것과 같아서 실수하면 작업 내역이 꼬일 수 있습니다.
            - 익숙해지기 전까지는 git pull을 했을 때 힌트가 뜨면 Merge(합치기) 방식을 선택하는 것이 정신건강에 좋습니다.

---

1. Day 2복습 과 부족 부분 보강 및 상세 정리
    - 
        1. 숫자형(int)와 문자열(str)의 차이
            1. int (정수형)
                - 10, -3, 0 과 같은 숫자
                - 수학 연산이 가능합니다 : +, -, *,/, %등
                    
                    ```python
                    a = 10
                    b = 3
                    print(a+b) #13
                    ```
                    
            2. str(문자열형)
            - “10”, “hello”, ‘안녕하세요’ 따옴표(” “, ‘ ‘)가 있어야 문자열이 됩니다.
            - 텍스트 데이터, 문자들의 집합
            - 숫자처럼 더하기를 하면 문자열 이어붙이기가 됩니다.
                
                ```python
                s1 = "10"
                s2 = "3"
                print(s1 + s2) # "103"
                ```
                
            
            💣주의사항
            
            int+str는 바로 더할 수 없고, 형변환이 필요합니다.
            
            ```python
            a = 10 #int
            b = "3" #str
            
            #print (a+b) ->이렇게 출력 시 TypeError발생
            
            print(a +int(b)) #13
            print(str(a)+b) #"103"
            ```
            
            c. type()자료형으로 확인
            
            ```python
            x = 10
            y = "helllo"
            
            print(type(x)) # <class 'int'>
            print(type(y)) # <class 'str'>
            ```
            
            코드를 짤 때 “이 값이 지금 숫자인지 문자열인지”헷갈릴 때 type()으로 확인하면 됩니다.
            
            d. Ai 교차검증을 통한 부족한 부분에 대한 보강
            
            - 변수와 출력 : f-string의 중요성
            - 실무에서는 +방법으로 문자열과 숫자를 더하기 보다는
                
                f-string방식을 사용하여 연결합니다.
                
                ```python
                score = 60
                #옛날 방식 
                print("제 점수는 " + str(score) + "점 입니다.") #제 점수는 60점 입니다
                #출력할 때 복잡함과 실수하기 쉽다는 단점이 있습니다.
                
                #f-string(실무)
                print(f"제 점수는{score}점 입니다")#제 점수는 60점 입니다.
                #문법적으로도 짧아져 가독성이 높아짐
                ```
                
                💫자료형 변환(str())을 신경 쓰지 않아도 되는 f-string을 손에 익히는 편이 좋음.
                

---

1. Day 3복습 과 부족 부분 보강 및 상세 정리
    - 
        1. 조건문(if / elif/ else)
            1. 기본 구조와 들여쓰기
                
                ```python
                if 조건1 :
                	#조건1이 참일 때 실행
                elif 조건2 : 
                	#조건1은 거짓, 조건2는 참일 때 실행
                else :
                	#위의 모든 조건이 거짓일 때 실행
                ```
                
                - : (콜론) 뒤에 오는 블록은 반드시 들여쓰기를 해야합니다.
                - 파이썬은 들여쓰기로 “어디까지가 if안의 코드인지”를 구분합니다.
            2. 90점 이상이면 A학점 판별 코드
                
                ```python
                #가장 단순한 방법
                score = int(input("점수를 입력하세요 : "))
                #input은 입출력 함수이며 아직 배우지 않았으나 입력에 관한 함수라는 걸 기억해 둘 것
                if score >=90 :
                	print("A학점입니다")
                else :
                	print("A학점이 아닙니다")
                ```
                
                ```python
                #상세하게 반영
                
                score = int(input("점수를 입력하세요 : "))
                
                if score >=90 :
                		grade = "A"	
                elif score >=80:
                		grade = "B"
                elif score >=70:
                		grade = "C"
                else :
                		grade = "재수강"
                
                print(f"당신의 학점은{grade}입니다")
                ```
                
                여기서도 들여쓰기를 잘못하면 바로 에러가 나는 걸 눈에 꼭 익혀두면 좋습니다.
                

---

1. Day 4 복습과 부족 부분 보강 및 상세 정리
    - 
        1. 반복문 for문과 while문의 차이
            1. for 문 
                - “정해진 횟수 만큼”혹은 “리스트/문자열의 각 요소에 대해” 반복할 때 사용.
                    
                    ```python
                    for i in range(5) :
                    	print(i)
                    ```
                    
            2. while 문
                - “조건이 참인 동안 계속 반복”할 때 사용
                - 반복 횟수가 미리 정해져 있지 않을 때 주로 사용
                    
                    ```python
                    i = 0
                    while i<5 :
                     print(i)
                     i += 1
                    ```
                    
            
            for와 while문의 결과는 둘 다 0,1,2,3,4 출력이지만 
            
            - for는 “얼마나 반복할지”를 먼저 결정하는 느낌
            - while은 “조건이 깨질 때까지 계속” 이라는 느낌
        2. range(5)의 의미
            
            ```python
            for i in range(5):
            	print(i)
            ```
            
            - range(5)는 0,1,2,3,4를 차례대로 내보내는 객체입니다.
            - 즉, “0이상 5 미만의 정수” 를 순서대로 반복하게 됩니다.
            - 필요하면 시작 값, 끝 값, 증가 값도 설정할 수 있습니다.
                
                ```python
                range(1,6) #1,2,3,4,5
                range(0,10,2)#0,2,4,6,8
                ```
                
        
        Ai교차 검증 결과 이상 없음 및 부족부분이 있을 시 나중에 책 및 강의로 보강 예정
        

---

1. Day 5/6 복습과 부족 부분 보강 및 상세 정리
    - 
        1. 리스트 안에 여러 자료형 담기
            1. 리스트 기본형태
                
                ```python
                my_list=[값1,값2,값3,...]
                ```
                
                파이썬 리스트는 여러 자료형을 섞어서 넣을 수 있습니다.
                
                ```python
                mixed_list = [10, "hello", 3.14, True]
                print(mixed_list[0]) #10
                print(mixed_list[1]) #"hello"
                ```
                
                인덱스는 0부터 시작(mixed_list[0] → 첫 번째 요소)
                
        2. for item in list : 로 리스트 순회
            
            ```python
            fruits = ['사과',"바나나",'포도']
            
            for fruit in fruits:
            	print(fruit)
            	#사과 
            	#바나나
            	#포도
            ```
            
            인덱스까지 같이 쓰고 싶다면 enumerate()도 자주 씁니다.
            
            enumerate()는 리스트, 튜플 같은 반복 가능한 것(iterable)을 돌 때,
            
            각 요소에 자동으로 번호(인덱스)를 붙여주는 파이썬의 내장 함수 입니다. 
            
            ```python
            for index, fruit in enumerate(fruits):
            	print(index,fruit)
            	#0 사과
            	#1 바나나
            	#2 포도
            ```
            
        3. Ai교차 검증을 통한 부족부분 정리 및 보강
            - 만약 리스트에 데이터가 3개 있는데 mixed_list[3](4번째 요소)을 부르면 어떻게 될까요
                
                IndexError : list index out of range가 발생하는데
                
                “범위를 벗어났다”는 뜻입니다. 리스트를 다룰 때 이 에러를 만나면 “ 아, 내가 개수를 잘못 셌구나(0부터 시작 안했거나, 없는 번호를 불렀구나)”라고 바로 알아채야 합니다.
                

---

1. 요약
    - 
        - Git 기본 명령어(add, commit, push)와 non-fast-forward 오류 해결법(git pull --rebase) 숙지
        - 변수와 자료형: 숫자형(int)과 문자열(str) 구분, type() 활용, f-string 실무 사용법
        - 조건문: if/elif/else 구조와 들여쓰기 규칙, 학점 판별 코드 작성
        - 반복문: for문(정해진 횟수)과 while문(조건 기반) 차이, range() 함수 이해
        - 리스트: 여러 자료형 저장, for item in list 순회, enumerate()로 인덱스 활용
        - 주요 에러: IndexError는 리스트 범위 초과 시 발생(0부터 시작하는 인덱스 주의)