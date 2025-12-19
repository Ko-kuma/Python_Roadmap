# 1. 부모 (기본 틀)
class Character:
    def attack(self):
        print("기본 공격!")

# 2. 자식들 (각자의 방식대로 오버라이딩)
class Warrior(Character):
    def attack(self): # 덮어쓰기
        print("전사가 대검을 휘두릅니다!")

class Wizard(Character):
    def attack(self): # 덮어쓰기
        print("마법사가 파이어볼을 날립니다!")

party = [Warrior(), Wizard(), Warrior()] # 전사 2명, 마법사 1명 파티 결성

print("--- 전원 공격 개시! ---")

# 반복문 하나로 끝냅니다. (누구인지 신경 안 씀)
for member in party:
    member.attack()