# 4일차 반복문을 활용한 합계 계산

total = 0 

#i는 0부터 9까지 반복됩니다.(1부터 10까지 더하려면 range(1,11)을 사용)
for i in range(1,11):
    total = total + i # total에 i의 값을 누적

print(f"1부터 10까지의 합계 : {total}")
