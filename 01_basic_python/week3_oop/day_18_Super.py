# [부모]
class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100   
        print("부모 클래스 기본 세팅 완료!")

# [자식]
class Wizard(Character):
    def __init__(self, name):
       
        super().__init__(name)  
        
       
        self.mp = 500
        print("자식 클래스 마나 세팅 완료!")

# --- 확인 ---
harry = Wizard("해리포터")
print(f"체력: {harry.hp}")  #상속 받은 것
print(f"마나: {harry.mp}")  #super