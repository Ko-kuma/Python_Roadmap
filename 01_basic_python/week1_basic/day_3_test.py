#3일차 학점 판별기

# 'score' 변수에 점수를 할당
score = 88

#조건문을 사용한 점수에 따른 학점 판별
if score >=90:
    #조건 1: 점수가 90점 이상이면
    grade = 'A힉점'
elif score >= 80:
    #조건 2: 90점 미만이지만, 80점 이상이면
    grade ='B학점'
elif score >= 70:
    #조건 3 : 80점 미만이지만 70점 이상이면
    grade = 'C학점'
else:
    #모든 조건에 해당하지 않으면 
    grade = 'F힉점'
print(f"점수는 {score}점이며, 최종 학점은 {grade}입니다")
