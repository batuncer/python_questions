# Write a function that checks prime numbers. If a number is prime, it returns “Wow!  # is prime”,
# otherwise it returns “Alas!  # is not prime”.
# Sample Input 1: 29
# Sample Output: Wow! 29 is prime
# Sample Input 2: 12
# Sample Output: Alas! 12 is not prime

def prime_numbers (number):

    if number < 2:
        return f"Alas! {number} is not prime"
    for i in range (2, number):
        if number % i == 0:
            return f"Alas! {number} is not prime"
    return f"Wow! {number} is prime"


print(prime_numbers(29))
print(prime_numbers(12))