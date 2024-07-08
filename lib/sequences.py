def print_fibonacci(n):
    if n <= 0:
        print([])
    elif n == 1:
        print([0])
    else:
        fibonacci_list = [0, 1]
        while len(fibonacci_list) < n:
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_number)
        print(fibonacci_list)
