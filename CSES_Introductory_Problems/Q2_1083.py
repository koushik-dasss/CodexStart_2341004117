n = int(input())
given_numbers =[]
ctr =1
while ctr<n:
    number = int(input())
    given_numbers.append(number)
    ctr+=1
    
sum =0
for i in given_numbers:
    sum+=i

expected_sum = n * (n + 1) // 2
missing_number = expected_sum - sum
print(missing_number)
