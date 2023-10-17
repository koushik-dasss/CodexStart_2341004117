''' Name :- Koushik Das
    Regd. No.:- 2341004117
    Qs. Link:-  https://cses.fi/problemset/task/1069 '''
# Input of DNA Sequence
DNA_Sequence = input()  
r = 1 # Initialisation of varibale for normal repetition 
max_r = 1 # Initialisation of varibale for highest repetition 
for i in range(1, len(DNA_Sequence)): # iterating each character of the DNA Sequence 
    if DNA_Sequence[i] == DNA_Sequence[i - 1]:  # Character equal or not 
        r += 1
    else:
        max_r = max(max_r,r) 
        r=1
print(max(max_r, r)) # Output ( Longest repitition in the sequence )