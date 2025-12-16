#Create a Moster class
class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def hit(self, damage):
        self.hp -= damage
        print(f"   ({self.name}이 {damage} 데미지를 입었습니다. 남은 체력: {self.hp})")

#Create a Character Class
class Character:
    def __init__(self, nickname, job):
        self.nickname = nickname
        self.job = job
        self.hp = 100
    
    # 상대방(target)의 hit 함수를 호출하는 것이 핵심
    def attack(self, target):
        print(f"⚔️ {self.nickname}이(가) {target.name}을(를) 공격합니다!")
        target.hit(10) # 10의 데미지 입힘

# --- 실행 확인 ---
hero = Character("아더왕", "전사")
mob = Monster("고블린", 50)

print(f"야생의 {mob.name}(체력:{mob.hp})이 나타났다!")
hero.attack(mob) # 공격 1방
hero.attack(mob) # 공격 2방