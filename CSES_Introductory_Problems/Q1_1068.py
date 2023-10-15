''' Name :- Koushik Das
    Regd. No.:- 2341004117
    Qs. Link:-  https://cses.fi/problemset/task/1068 '''
# Taking input (1<=n<=10^6)
num = int(eval(input("Enter an integer: ")))
false = 0
#Checking validity of the input
if num < 1:
    print("Invalid Input")
    false += 1
else:
    while True:
        print(num, end=' ')
        if num ==1:
            break
        elif num % 2 == 0:  #checking for even integers
            num //= 2   
        else:  #if not even , then obviously odd
            num = 3 * num + 1

    if false == 0 and num!=1 : #if false is not incremented == no invalid input
        print(1)
