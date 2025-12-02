# 2일차 학습 실습 코드

# 1. 변수 선언 및 출력
nickname = "Pythoner Ko" #string
hours = 2.5 #float
print(f"나의 닉네임: {nickname}")
print(f"오늘의 목표 학습 시간: {hours}시간")

# 2. 계산 실습
base_salary = 100 #int
bonus = 20 #int
total_money = base_salary + bonus

# 3. 자료형 확인
print(type(nickname)) 
print(type(total_money)) 

# 4. 문자열과 숫자 결합 (에러 발생 확인)
# print("총 금액은 " + total_money + "입니다.") 
print(f"총금액은{total_money}입니다")
# 위 코드는 에러가 납니다. 문자열과 숫자는 바로 결합할 수 없습니다!