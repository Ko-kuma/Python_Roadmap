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
