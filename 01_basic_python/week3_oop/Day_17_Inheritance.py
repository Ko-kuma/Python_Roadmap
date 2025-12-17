# [부모클래스]
class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
    
    def attack(self):
        print("주먹질!")

# [자식 클래스]
class Wizard(Character):
    pass  # "pass"는 "일단 내용 없음(넘어가)"이라는 뜻

gandalf = Wizard("간달프")

#정보 확인 (부모의 변수 사용)
print(f"이름: {gandalf.name}")  
print(f"체력: {gandalf.hp}")  

gandalf.attack()  