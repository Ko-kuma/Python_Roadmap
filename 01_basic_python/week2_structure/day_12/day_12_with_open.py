#'w' 모드 : 쓰기(write)모드.(새로 만들기. 기존 내용은 싹 지워짐)
#'a' 모드 : 추가(Append)모드.(기존 내용 뒤에 이어 붙이기)
with open("파일명.txt","w",encoding="utf-8") as f :
	f.write("이 내용을 파일에 적어주세요.\n") #\n은 이스케이프 문자 줄바꿈