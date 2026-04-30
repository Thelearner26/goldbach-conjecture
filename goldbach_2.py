def prime_sieve(num):
    prime_num = [True] * (num + 1)

    prime_num[0] = False
    prime_num[1] = False

    for i in range (2 , int (num ** 0.5) + 1):
        if prime_num[i]:
            for j in range (2*i , num + 1 , i ):
                prime_num[j] = False

    primes = []
    for p in range(2 , num + 1):
        if prime_num[p]:
            primes.append(p)

    return(primes)


def goldbach_count(num):
    prime_list = prime_sieve(num)
    prime_set = set(prime_list)
    
    
    for even_num in range(4, num + 1, 2):
        count = 0
        
        for p in prime_list:
            if p > even_num // 2:
                break
            if (even_num - p) in prime_set:
                count += 1
        
        print(f"{even_num} → {count} representations")
    


number = int(input("Goldbach representation up till which number ?  "))

goldbach_count(number)
