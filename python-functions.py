# Number 1
def sum_to(n):
  sum = 0
  for value in range(1, n+1):
    sum += value
  print(sum)

sum_to(10)


# Number 2
def largest(li):
  return max(li)

print(largest([1, 2, 3, 4, 0]))


# Number 3
def occurrences(str1, str2):
  return str1.count(str2)

print(occurrences('fleep floop', 'fe'))

# Number 4
def product(*args):
  result = 1
  for x in args:
    result *= x
  return result

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0