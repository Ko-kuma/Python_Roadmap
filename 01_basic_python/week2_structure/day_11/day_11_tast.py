#day_11_tast : 데이터 전처리
dirty_comments = [
    "정말 좋은 제품이네요!! " ,
    "ㅋㅋ",
    "배송이 너무 늦어요",
    "정말 좋은 제품이네요!!",
    "굿",
    "강추 합니다"
]

print(f"정리 전 : {dirty_comments}")

#문자열 정리
cleaned_stap1 = [c.strip() for c in dirty_comments]

#중복제거 (set)
cleaned_stap2 = list(set(cleaned_stap1))

#필터링 
final_comments = [c for c in cleaned_stap2 if len(c) >=3]

print(f"정리 완료 : {final_comments}")