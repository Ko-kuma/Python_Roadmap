# 부모
class Character:
    def attack(self):
        print("주먹질")

# 자식
class Wizard(Character):
    # 부모한테 attack이 있지만, 내가 다시 만듦 (덮어쓰기!)
    def attack(self):
        print("마법 공격! 파이어볼!")

# --- 확인 ---
gandalf = Wizard()
gandalf.attack()