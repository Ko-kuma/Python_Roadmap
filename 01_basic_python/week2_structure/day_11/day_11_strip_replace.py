#day11_strip_replace_split

raw_data = " 가격 : 10,000원(부가세 별도) \n"
print(f"원본 : '{raw_data}'")

#strip - 양쪽 공백과 줄바꿈 제거
step1 = raw_data.strip()
print(f"1단계(strip) : '{step1}'")

#replace - '가격 :', '원', ','같은 불순물 제거 -> 빈칸(' ')으로 변경
step2 = step1.replace("가격 : ", "").replace("원", "").replace(",","").replace("(부가세 별도)", "")
print(f"2단계(replace) : '{step2}'")

#마지막 공백을 한 번더 제거하고 정수로 변환
final_price =int(step2.strip())
print(f"최종결과 :{final_price}(자료형 :{type(final_price)})")