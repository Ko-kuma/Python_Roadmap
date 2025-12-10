#day10_main_as.py
from day_10_my_tools import say_hello
print("---from 예제---")

#도구함에 있는 인사 함수 쓰기
say_hello("학습자")

#주의 : 편하기는 하지만 해당 파일에도 say_hello라는 함수가 존재 할 시 이름이 겹쳐 충돌 위험 이있습니다. 그래서 as가 더 안전성이 있습니다.