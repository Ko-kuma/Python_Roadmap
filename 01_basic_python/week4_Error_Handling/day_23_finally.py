try:
    print("1. 엑셀 파일을 열었습니다.")
    result = 10 / 0 

except ZeroDivisionError:
    print("2. 에러 수습 중...")

finally:
    # 에러가 나든 안 나든, 이 코드는 끝까지 실행합니다.
    print("3. (필수) 엑셀 파일을 안전하게 저장하고 닫았습니다.")

print("4. 다음 작업 시작!")