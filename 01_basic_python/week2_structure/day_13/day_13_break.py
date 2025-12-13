while True : #무한히 반복 됩니다.
	text = input("입력하세요 : ")
	
	if text == "q": # q가 입력 되면
		print("탈출합니다!")
		break #브레이크
	
	print(f"나의 글 : {text}") 