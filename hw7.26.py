def print_triangular_numbers(n):

    for i in range(1, n+1):
        print(i, "\t", int(i*(i+1)/2))

print_triangular_numbers(15)