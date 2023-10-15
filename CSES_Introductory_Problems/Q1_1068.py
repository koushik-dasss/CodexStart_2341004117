''' Name :- Koushik Das
    Regd. No.:- 2341004117
    Qs. Link:-  https://cses.fi/problemset/task/1068 '''

''' Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if 
n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for 
n=3 is as follows:
3→10→5→16→8→4→2→1 '''

# Taking input (1<=n<=10^6)
num = int(input("Enter  integer: "))
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
