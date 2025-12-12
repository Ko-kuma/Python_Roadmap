print("--- 학습 기록 프로그램 ---")

# 목표 입력 (그냥 문자열이니까 에러 날 걱정이 없음)
goal = input("오늘의 학습 목표는?: ")

# 시간 입력 (여기가 위험 구간! 숫자로 바꿔야 계산)
try:
    time_input = input("목표 학습 시간(숫자만)을 입력하세요: ")
    study_time = int(time_input) # <-여기서 사용자가 "두시간"이라고 치면 에러 발생!
    
    print(f"✅ 입력 확인: 목표 '{goal}'을(를) {study_time}시간 동안 하시겠군요.")
    print(f"분으로 환산하면 총 {study_time * 60}분입니다.")

    # 파일 저장 (모든 게 정상일 때만 저장)
    with open("study_log.txt", "a", encoding="utf-8") as f:
        f.write(f"목표: {goal} | 시간: {study_time}시간\n")
    print("메모장에 저장되었습니다.")

except ValueError:
    # 숫자가 아닌 것을 입력했을 때 실행
    print("⚠ 에러 발생: 시간은 '숫자'로만 입력해야 합니다! (저장되지 않음)")

print("--- 프로그램 종료 ---")