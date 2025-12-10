#day10_main_as.py
import day_10_my_tools as mt
print("---메인 프로그램 시작---")

#도구함에 있는 인사 함수 쓰기
#사용 법 : 파일명.함수명()
mt.say_hello("학습자")

#도구함에 있는 계산기 함수 쓰기
price = mt.calculate_price(50000)
print(f"10%할인가는{price}입니다")