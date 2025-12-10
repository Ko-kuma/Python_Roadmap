#day10_main.py
import day_10_my_tools
print("---메인 프로그램 시작---")

#도구함에 있는 인사 함수 쓰기
#사용 법 : 파일명.함수명()
day_10_my_tools.say_hello("학습자")

#도구함에 있는 계산기 함수 쓰기
price = day_10_my_tools.calculate_price(50000)
print(f"10%할인가는{price}입니다")