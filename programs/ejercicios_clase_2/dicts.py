# Sin dict comprehension
squares = {}
for i in range(1, 101, 1):
    squares[i] = i*i

# Con dict comprehension
# squares = {x: x**2 for x in range(1,101, 1)}
total = 0
for sq in squares:
    total += sq
print(total)