'''
1. 파일 입출력을 하려면 무슨 모듈이 필요한가 : print와 input함수를 사용하기 때문에 import를 사용하여 모듈을 불러올 필요는 없음
2. 무한히 반복한다(while문을 사용하고 True를 써라 참인동안은 계속 하라는 것이니까)
3. 사용자 입력을 받는다(input)
4. 입력 받은 내용은 day12_memo.txt파일에 한줄씩 저장(with open 및 \n이스케이프 문자)
5. '폭탄' 이라고 입력하면 강제로 에러를 발생(이건, if문을 사용하면 될 거같은데 정확히 모르겠음)
6. 에러가 터져도 터지지 않고 "에러를 잡았습니다!"(try-except사용)
7. 'q' 입력하면 프로그램 종료(break문을 사용해라)
'''

while True : #무한 반복 실행
    boom = input("내용을 입력하십시요 :")#입력변수

    if boom == "q" :#종료 조건
        print("종료합니다")
        break#브레이크

    try :#예외처리
        if boom == "폭탄" : #에러 조건
            #강제 에러를 일으키는 명령어
            raise Exception("강제 폭발!")
        
        with open("day13_memo.txt", "a", encoding="utf-8") as f:
            f.write(f"입력내용: {boom}\n")
            
        print("해당 내용이 저장되었습니다.")
        
    except Exception as e: # [비상 대피소]
        # 폭탄이 터지면(raise되면) 저장 코드를 건너뛰고 바로 여기로 옵니다.
        print(f"에러가 발생했어요! ({e}) 하지만 프로그램은 죽지 않아요.")

    
