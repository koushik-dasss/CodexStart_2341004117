n = int(input())
ctr =1
given_numbers = list(map(int, input().split()))
    
new_sum = sum(given_numbers)

total_sum = 0
for i in range(1,n+1):
    total_sum+=1

missing_number = total_sum - new_sum
print(missing_number)

