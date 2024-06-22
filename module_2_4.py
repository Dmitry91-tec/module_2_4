numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
numbers.remove(1)                          #Убираем 1 из списка
for i in numbers:
    for j in numbers:
        if i % j == 0 and i >= j:
            is_prime = True
            while is_prime:
                if i / j != 1:
                    break                 #Число не простое
                else:
                    primes.append(i)      #Число простое
                    break
            break
not_primes = list(set(numbers)-set(primes))
print(primes)
print(not_primes)