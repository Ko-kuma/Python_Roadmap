# day10_main.py
import random
import time

# 뽑고 싶은 목록(리스트)
menu_list = ["김치찌개", "돈까스", "짜장면", "초밥", "햄버거"]

print("me: 오늘 뭐 먹지? 고민 중...")
time.sleep(2) # 2초 동안 고민하는 척

# choice가 리스트 안에서 하나를 랜덤으로 뽑음
today_menu = random.choice(menu_list) 

print(f"me: 오늘의 추천 메뉴는 [{today_menu}] 입니다!")