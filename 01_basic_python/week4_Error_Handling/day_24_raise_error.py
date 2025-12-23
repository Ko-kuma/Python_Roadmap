
class LevelError(Exception): 
    pass

def set_level(level):
    if level > 100:
        # 억지로 에러를 발생시킴! (raise)
        raise LevelError("레벨은 100을 초과할 수 없습니다!")
    print(f"레벨이 {level}로 설정되었습니다.")

try:
    set_level(150) # 일부러 에러 상황 만들기
except LevelError as e:
    print(e) # 만든 에러 메시지 출력