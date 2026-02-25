n = int(input())
gen_exp = (i**2 for i in range(1, n + 1))
for val in gen_exp:
    print(val)