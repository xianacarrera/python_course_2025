n = 127
iter = 1

while n > 4:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3*n + 1
    print(f"Iteración {iter}, n = {n}")
    iter += 1

print("Hemos llegado al bucle 4->2->1->4->2->1->...")