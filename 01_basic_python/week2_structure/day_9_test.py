#쇼핑몰에서 결제금액을 계산 10% 할인가로 계산
def calculate_price(original_price) :
    discount =original_price * 0.1 # 10%할인 금액
    final_price = original_price - discount
    return final_price

t_shirt = calculate_price(20000)
print(f"티셔츠의 최종가는 {int(t_shirt)}원 입니다.")