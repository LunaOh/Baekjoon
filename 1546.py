n=int(input())
score = list(map(int, input().split()))
m=max(score)
tot=0
for i in range(n):
    score[i]=score[i]/m*100
    tot+=score[i]
print(tot/n)