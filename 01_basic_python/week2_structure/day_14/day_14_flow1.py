while True: 
    text = input("숫자를 입력하세요(종료:q): ") 

    if text == 'q': 
        break

    try: 
        num = int(text)     
        print(10 / num)      
        
    except:  
        print("에러 발생! 숫자를 제대로 입력하세요.")