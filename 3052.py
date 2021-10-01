n_list=[]
for i in range(10):
    n=int(input())
    n_list.append(n%42)
n_list=set(n_list) # set함수는 중복되지 않은 원소를 갖는 집합, 중복 삭제
print(len(n_list))