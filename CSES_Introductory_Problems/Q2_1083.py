n = int(input())
list_numbers=[]
new_sum =0
ctr =1
while ctr<n:
    number = int(input())
    list_numbers.append(number)
    ctr+=1
for i in list_numbers:
    new_sum+=i

total_sum = 0
for i in range(1,n+1):
    total_sum+=i
missing_number = total_sum - new_sum

print(missing_number)