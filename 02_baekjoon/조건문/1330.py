A, B = map(int, input().split())

if A > B :
    print(">")
elif A < B :
    print("<")
else :
    print("==")


#print(f">" if A > B else f"<" if A < B else f"==")