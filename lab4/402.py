def even_numbers_generator(n):

    for i in range(0, n + 1, 2):  
        yield i


n = int(input())


gen = even_numbers_generator(n)

print(",".join(str(x) for x in gen))
