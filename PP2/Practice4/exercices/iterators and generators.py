# 1 Create a generator that generates the squares of numbers up to some number N.

def square_generatot(n):
    for i in range(1, 1+n):
        yield i**2
a=int(input())
squares=square_generatot(a)
for result in squares:
    print(result)
# 2
def even_generator(n):
    for i in range(0, n+1):
        if i%2==0:
            yield str(i)
n=int(input())
gen=even_generator(n)
result=",".join(gen)
print(result)
# 3
def my_generator(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield str(i)
n=int(input())
gen=my_generator(n)
result=" ".join(gen)
print(result)
# 4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
a, b=map(int, input().split())
gen=squares(a, b)
for res in gen:
    print(res)
# 5
def mygen(n):
    for i in range(n, -1, -1):
        yield i
n=int(input())  
gen=mygen(n)
for result in gen:
    print(result)



