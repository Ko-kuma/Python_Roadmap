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