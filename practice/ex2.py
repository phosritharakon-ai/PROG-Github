n = int(input())
data = input().split()

prime_count = 0
prime_sum = 0

for i in range(n):
    num = int(data[i])
    if num > 1:
        is_prime = True
        
        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1
            prime_sum += num
print(prime_count)
print(prime_sum)