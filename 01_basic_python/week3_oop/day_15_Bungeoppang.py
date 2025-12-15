'''
class Bungeoppang :
	#__init__은 붕어빵이 처음 만들어 질 때(생성 될 때) 실행 되는 함수
	#self는 '나 자신(만들어진 붕어빵)'을 가리켜요
	def __init__(self, mat, price) :
		self.mat = mat #나 자신의 맛(속재료) 저장
		self.price = price #나 자신의 가격 저장
	
	#붕어빵의 자소서
	def say_hi(self) :
		print(f"{self.mat}붕어빵, 가격{price}입니다")
        
#팥 붕어빵 만들기(객체 생성)
red_bean = Bungeoppang("팥", 1000)

#슈크림 붕어빵 만들기(또 다른 객체 생성)
cream = Bungeoppang("슈크림", 1200)

red_bean.say_hi() #함수 호출
cream.say_hi()
'''

'''
class Bungeoppang :
	def __init__(self,mat, price) :
		self.mat = mat
		self.price = price * 0.9
		
	def new_mat(self) :
		print(f"신상품 {self.mat}, 가격 지금 10%할인{int(self.price)}")
		
pizza = Bungeoppang("피자맛", 1500)

pizza.new_mat()
'''

class Bungeoppang :
    def __init__(self, mat, price) :
        self.mat = mat
        self.price = price
        self.sales = 0  # <--- [추가] 태어날 땐 판매량 0
        
    def new_mat(self) :
        print(f"신상품 {self.mat}, 가격 {self.price}")

    # --- [미션] 아래 함수를 완성해서 채워 넣으세요 ---
    def sell(self):
        self.sales += 1  # 판매량 1 증가
        print(f"{self.mat} 붕어빵 판매 완료! (총 {self.sales}개 팔림)")
        
red_bean = Bungeoppang("팥", 1000)

red_bean.sell() # "팥 붕어빵 판매 완료! (총 1개 팔림)"
red_bean.sell() # "팥 붕어빵 판매 완료! (총 2개 팔림)"
red_bean.sell() # "팥 붕어빵 판매 완료! (총 3개 팔림)"