
#while문
count = 0
while count < 5 : # 조건 : count가 5보다 작은 동안 
	print(f"현재 숫자는{count}입니다.")
	count = count+1 #또는 count+= (count를 1씩 증가)

print("반복 종료")
#결과 : 0~4까지 출력 후 종료


#range(5) : 0부터 5미만(0,1,2,3,4)의 숫자 시퀀스 생성
for i in range(5) : 
	print(f"for문 반복 횟수 : {i}")
	
for year in range(2023, 2026): # 2023,2024,2025
	print(f"{year}년도 목표를 확인 합니다.")
