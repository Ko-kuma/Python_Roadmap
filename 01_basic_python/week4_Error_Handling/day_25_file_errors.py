import os

def read_my_file(filename):
    try:
        # 파일 읽기 시도
        with open(filename, "r", encoding="utf-8") as f:
            print(f"파일 내용: {f.read()}")

    except FileNotFoundError:
        # 파일이 아예 없을 때
        print(f"[에러] '{filename}' 파일이 폴더에 없습니다. 이름을 확인해주세요.")

    except PermissionError:
        # 파일은 있지만 권한이 없거나 다른 프로그램(엑셀 등)이 이미 열고 있을 때
        print(f"[에러] 파일은 있지만 읽을 권한이 없습니다. 혹시 다른 곳에서 열려있나요?")

    except Exception as e:
        # 위 상황 외에 우리가 예상치 못한 다른 모든 에러
        print(f"[기타 에러] 알 수 없는 문제가 발생했습니다: {e}")

# --- 테스트 ---
print("--- 파일 읽기 테스트 시작 ---")
read_my_file("nothing.txt")  # 없는 파일을 불러와서 FileNotFoundError 유도