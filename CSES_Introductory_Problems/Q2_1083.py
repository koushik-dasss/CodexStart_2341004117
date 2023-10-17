n = int(input())
for _ in range(n+1):
	new=int(input())
	s=list(map(int,input().split()))
new_sum =0
for i in s:
    new_sum+=i
total_sum = 0
for i in range(1,n+1):
    total_sum+=i
missing_number = total_sum - new_sum

print(missing_number)