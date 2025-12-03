#조건문을 배우기 전 논리, 비교 연산자 실습
print(10==10) #10과 10은 같다(같다)
print(5!=10) #5와 10은 값이 같지 않다(다르다)
print(20>5) #20은 5보다 크다
print(5<20) #5는 20보다 작다
print(20>=19) # 20은 19보다 크거나 같다
print(20<=20) # 20은 20보다 작거나 같다
print((10>5)and(5>1)) #10은 5보다 크다 그리고 5는 1보다 크다 (두 조건 다 맞아야 True)
print((10<5)or(10>5)) #10은 5보다 작다 또는 10은 5보다 크다 (한 개의 조건이라도 맞으면 True)
print(not(10>5)) #10은 5보다 크다 하지만, 논리연산자 not이여서 조건은 반대 (10은 5보다 작다)

#단일 조건(if)
money = 10000

#만약(if) 돈이 5000원 보다 많으면, 다음 코드를 실행 
if money > 5000:
	print("택시를 탈 수 있습니다")

#양자택일(if, else)
is_rainy = True

#비가 오면 우산을 챙긴다
if is_rainy:
	print("우산을 챙긴다.")#is_rainy가 True일 때 실행
else:
	print("그냥 나간다.")#is_rainy가 False일 때 실행


#다중 조건(if, else, elif)
score = 85

if score >=90:
	print("A학점")
elif score >=80:
	#위의 조건(90점 이상)이 거짓일 때, 이 조건(80점 이상)을 검사
	print("B학점")
else :
	#모든 조건이 거짓일 때 실행
	print("C학점")
