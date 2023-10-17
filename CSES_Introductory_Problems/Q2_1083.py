''' Name :- Koushik Das
    Regd. No.:- 2341004117
    Qs. Link:-  https://cses.fi/problemset/task/1068 '''



''' You are given all numbers between  1,2,…n
 except one. Your task is to find the missing number.

input = n 
        (n-1) numbers in one line
output = missing number '''         






# Input n (2≤n≤2*10^5))
n = int(input())
list_numbers=[]  # Empty list initialisation 
new_sum =0
ctr =1
while ctr<n:
    number = int(input())   
    list_numbers.append(number)   # (n-1) numbers appended in the list (including n and other numbers between n)
    ctr+=1
for i in list_numbers:
    new_sum+=i  # sum of (n-1) numbers

total_sum = 0
for i in range(1,n+1):
    total_sum+=i # sum of n numbers
missing_number = total_sum - new_sum   # output

print(missing_number)