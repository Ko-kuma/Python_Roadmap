
#day_10_my_tools.py
#실행 코드는 없고 함수만 있는 도구함

def calculate_price(original_price) :
	#원레 가격을 넣으면 10% 할인된 정수 가격을 돌려주는 함수
	discount = original_price *0.1
	final_price = original_price - discount
	return int(final_price)

def say_hello(name):
	#이름을 넣으면 인사를 출력 하는 함수
	print(f"반갑습니다, {name}님! 오늘도 파이썬 정복 해봅시다")