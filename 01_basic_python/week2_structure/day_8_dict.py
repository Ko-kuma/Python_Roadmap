'''
#딕셔너리 만들기(Key(고유식별자):Value(값) 쌍으로 이루어짐)
#형식은 {key : value, ....} 조금 더 쉽게 {이름표 : 값, 이름표2 : 값, ...}
my_info={
    "name" : "kim",
    "job" : "office worker",
    "age" : 30
}

#딕셔너리 데이터 꺼내기(이름표 부르기)
print(my_info["name"])
print(my_info["job"])

#딕셔너리 데이터 추가하기
my_info["hobby"] = "코딩"
print(my_info)

#딕셔너리 데이터 수정하기
my_info["name"] = "Mr"

#딕셔너리 데이터 삭제하기
del my_info["age"]
print(my_info)
'''
#for 문과 함께 사용하는 딕셔너리
menu = {
	"아메리카노" : 3000,
	"라떼" : 4000,
	"쿠키" : 2000
	}
print("---메뉴판---")
#key(메뉴명)와 value(가격)을 한 번에 꺼내기
for key, value in menu.items():
	print(f"{key}의 가격은 {value}원 입니다.")