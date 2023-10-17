''' Name :- Koushik Das
    Regd. No.:- 2341004117
    Qs. Link:-  https://cses.fi/problemset/task/1069 '''

DNA_Sequence = input()




r = 1
max_r = 1

for i in range(1, len(DNA_Sequence)):
    if DNA_Sequence[i] == DNA_Sequence[i - 1]:
        r += 1
    else:
        max_r = max(max_r,r)
        r=1
        


print(max(max_r, r))
