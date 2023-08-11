def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("it's a prime number.")
    else:
        print("it's not a prime number.")

n = int(input("check this number: "))
prime_checker(n)
