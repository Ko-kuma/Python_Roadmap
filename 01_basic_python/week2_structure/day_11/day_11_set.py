#day_11_set

#중복링크가 들어 올 때
crawled_urls = ["www.naver.com", "www.google.com", "www.naver.com", "www.daum.net"]

print(f"중복 제거 전(4개) : {crawled_urls}")

#set으로 변환 하는 순간 중복이 자동 삭제되며 다시 list로 변환
unique_urls = list(set(crawled_urls))

print(f"중복 제거 후({len(unique_urls)}개) : {unique_urls}")