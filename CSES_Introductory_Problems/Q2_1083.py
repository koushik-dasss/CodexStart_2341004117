n = int(input())
given_numbers =[]
ctr =1
while ctr<n:
    number = int(input())
    given_numbers.append(number)
    ctr+=1

new_sum =0
for i in given_numbers:
    new_sum+=i
total_sum = 0
for i in range(1,n+1):
    total_sum+=i
missing_number = total_sum - new_sum

print(missing_number)