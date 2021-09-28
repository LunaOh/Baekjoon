n_list=[]
for i in range(9):
    n_list.append(int(input())) # append 함수를 사용해서 array의 맨 끝에 요소로 추가
print(max(n_list))
print(n_list.index(max(n_list))+1)