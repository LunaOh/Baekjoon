s = input().upper()
alp = list(set(s))
cnt_list = [s.count(i) for i in alp]
 
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(alp[cnt_list.index(max(cnt_list))])