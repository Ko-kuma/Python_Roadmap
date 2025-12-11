#예시 게시글 내용
insta_post = "오늘도 파이썬 공부! #코딩 #Python #개발자 #오운완 힘들지만 재밌다 "

#공백기준 다어 쪼개기
words = insta_post.split()

#리스트 내포로 한줄로 해결,replace로 단어 변경
tags = [w.replace("#", ",") for w in words if "#" in w]

print(f"원본 게시글 : {insta_post}")
print(f"추출된 게시글 : {tags} ")
