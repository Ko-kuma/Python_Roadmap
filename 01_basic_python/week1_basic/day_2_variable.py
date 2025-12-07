#변수 선언 및 할당
# 'name'이라는 상자에 'Ko-kuma'라는 문자열을 담습니다.
name = "Ko-kuma"

# 'age'라는 상자에 숫자 32를 담습니다.
age = 32

# 상자 안의 값을 출력(화면에 표시)합니다.
print(name)
print(age)    

#---------------------------------------------------
# 정수형 예시
a = 10 
b = 5

# 계산도 가능합니다.
result_add = a + b 
print(result_add) # 15 출력

#------------------------------------
#문자열 예시(작은 따옴표, 큰 따옴표 모두 사용 가능)
message = "파이썬 기초 문법 공부 1일차"
goal = '하루 1~2시간 꾸준히!'

print(message)

#문자열을 서로 붙일 수도 있습니다(연결)
full_message = message + " " + goal
print(full_message)

#--------------------------------------------
print(type(age))
print(type(name))
print(type(3.14))