def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    prime_factors_list = []
    product_form = 1
    for i in range(2, n + 1):
        while is_prime(i) and n % i == 0:
            prime_factors_list.append(i)
            product_form *= i
            n //= i
        if n == 1:
            break
    return prime_factors_list, product_form

# Get user input
try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        raise ValueError("Please enter a positive integer.")
except ValueError as e:
    print(e)
    exit()

# Get and print prime factors
prime_factors_list, product_form = prime_factors(num)

if len(prime_factors_list) == 0:
    print(f"{num} has no prime factors.")
else:
    prime_factors_str = ' * '.join(map(str, prime_factors_list))
    print(f"The prime factors of {num} are: {prime_factors_str} ")
