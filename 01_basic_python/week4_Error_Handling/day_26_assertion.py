def calculate_pay(hours, rate):
    # [조건] 일한 시간과 시급은 절대 음수일 수 없음
    # assert 조건, "조건이 틀렸을 때 나올 메시지"
    assert hours > 0, "일한 시간은 0보다 커야 합니다"
    assert rate > 0, "시급은 0보다 커야 합니다"
    
    return hours * rate

try:
    print(f"정상 정산: {calculate_pay(40, 15000)}원")
    
    # 실수로 일한 시간을 -5로 넣었다면?
    print(f"실수 정산: {calculate_pay(-5, 15000)}원")

except AssertionError as e:
    print(f"차단됨: {e}")

print("\n Assertion 덕분에 잘못된 계산이 진행되지 않고 멈췄습니다.")