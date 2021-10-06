num = set(range(1,10001))
generated_num = set()
for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    generated_num.add(i) # add는 집합에 요소 추가

self_num=num-generated_num
for k in sorted(self_num): # sorted 함수로 정렬
    print(k)