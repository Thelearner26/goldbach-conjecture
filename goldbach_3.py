import matplotlib.pyplot as plt

def prime_sieve(num):

    prime_num = [True] * (num + 1)
    
    prime_num[0] = False
    prime_num[1] = False
    
    for i in range(2, int(num**0.5) + 1):
        if prime_num[i]:
            for j in range(2*i, num + 1, i):
                prime_num[j] = False
    
    primes = []
    for p in range(2, num + 1):
        if prime_num[p]:
            primes.append(p)
    
    return primes


def goldbach_comet(num):

    prime_list = prime_sieve(num)
    prime_set = set(prime_list)

    even_numbers = []
    counts = []

    for even_num in range(4, num + 1, 2):
        
        count = 0

        for p in prime_list:
            if p > even_num // 2:
                break
            if (even_num - p) in prime_set:
                count += 1

        even_numbers.append(even_num)
        counts.append(count)

    return even_numbers, counts


def plot_comet(even_numbers, counts):

    fig, graph = plt.subplots(figsize=(12, 6))

    graph.scatter(even_numbers, counts , color='white' , s=1 , alpha=0.5)

    graph.set_facecolor('#001133')
    fig.patch.set_facecolor('#001133')

    graph.set_xlabel('Even Number', color='white')
    graph.set_ylabel('Number of Representations', color='white')
    graph.set_title('Goldbach Comet', color='white')

    graph.tick_params(colors='white')
    graph.grid(True, color='white', alpha=0.1)

    plt.show()


number = int(input("Goldbach Comet up till which number ?  "))

even_numbers, counts = goldbach_comet(number)

plot_comet(even_numbers, counts)