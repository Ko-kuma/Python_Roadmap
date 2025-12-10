import time 
import random 

print("robot : 웹 사이트 접속 중...")

#1초부터 5초 사이의 숫자 중 하나를 랜덤으로 뽑습니다.
#ranint(a,b) -> a부터 b 까지 정수 중 하나를 뽑음
rest_time = random.randint(1, 5)

print(f"robot :사람인 척 하기 위해{rest_time}동안 다른 행동을 합니다")

#위 에서 뽑은 랜덤한 시간만큼 쉽니다.
time.sleep(rest_time)
print("robot : 휴식 끝 데이터를 훔쳐왔습니다")