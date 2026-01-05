
numbers = [2,4,5,10,13,14,13,11,7,9,7]

def is_prime(n, i=2):
    if n < 2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

recursive_prime_number = {num for num in numbers if is_prime(num) }

print(recursive_prime_number)