#A simple generator function:

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

#The yield Keyword
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)
