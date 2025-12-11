#day_11_List_Comprehension
nums =[1,2,3,4,5]

#[상황] 모든 숫자를 10배로 만들고 싶다.

#기존 방식 : append() 사용
result_a = []
for n in nums:
	result_a.append(n * 10)
print(f"기존 방식 : {result_a}")

#내포 방식 : List Comprehension
result_b = [n * 10 for n in nums]
print(f"내포 방식 : {result_b}")