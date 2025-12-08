#나만의 '프로필 관리 프로그램', 8일차 배운 내용으로 간단한 프로필 관리 코드 작성

profile = {
    "name" : "kim",
    "goal" : "Becoming a Developer with Python",
    "d_day" : 80
}

profile["today_mood"] = "tired"

# 1. 자연스러운 자기소개 (key)
print(f"Hello! My name is {profile['name']}.")
print(f"My goal is {profile['goal']}.")

# 2. 전체 데이터 확인 (반복문으로)
print("\n--- All Data ---")
for key, value in profile.items():
    print(f"{key} : {value}")


'''
# for와 if 활용 
for key, value in profile.items():
    if key == "name":  # 이름표(key)가 'name'일 때만 이 문장 출력
        print(f"My name is {value}.")
    elif key == "goal": # 이름표가 'goal'일 때만 이 문장 출력
        print(f"My goal is to be a {value}.")
    # d_day는 조건에 없으니 출력 안 됨 (혹은 다르게 처리 가능)
'''