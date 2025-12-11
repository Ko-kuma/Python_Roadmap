#초간단 계산기

#def정의
def add(x,y) :
	return x+y

#람다식 정의
add_lambda = lambda x,y : x+y

print(f"일반 함수 결과 : {add(10, 20)}")
print(f"람다 함수 결과 : {add_lambda(10,20)}")