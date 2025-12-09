'''
#함수의 정의(매개변수x, 자판기 설치)
def open_vending_machine():
	print("자판기 문이 열렸습니다!")
	print("무엇을 도와드릴까요?")

#함수 호출(버튼 누르기)
print("---프로그램 시작---")
open_vending_machine()
print("---프로그램 종료---")

#함수 정의(매개변수, 투입구가 있는 자판기)
def order_drink(drink_name):
	print(f"자판기 : {drink_name}을 선택하셨군요!")
	print(f"자판기 : 여기 시원한 {drink_name}이 나왔습니다")

#함수 호출(데이터를 넣어서 버튼 누르기)
order_drink("콜라") #콜라라는 데이터 전송
print("---")
order_drink("사이다") #사이다라는 데이터 전송
'''

#print만 사용하는 자판기(말만하는 자판기, 실제행동x)
def fake_vending_machine(money):
	result=money - 500
	print(f"가짜 자판기 : 거스름돈 {result}원 여기 보여줄게! (주지않음)")

#return을 사용하는 자판기(돈을 돌려주는 자판기, 실제행동)
def real_vending_machine(money):
	result = money - 500
	return result #계산된 result 값을 밖으로 던져줌
	
print("---실험 시작---")
#가짜자판기 실험
my_pocket1 = fake_vending_machine(1000)
print(f"내 주머니(가짜) 상황 : {my_pocket1}")
#결과값은 None(없음)이라고 나올 것입니다. 받은게 없기 때문에....

print("---")

#진짜 자판기
my_pocket2 = real_vending_machine(1000)
print(f"내 주머니(진짜) 상황 : {my_pocket2}원이 들어왓다")
