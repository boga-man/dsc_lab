primes = [];

# python program to print the prime numbers between 1 to 1000 using for loop
for i in range(2,1000):
    isPrime = 1;
    for j in range(2,i):
        # if a number is divisible by any number between 2 and itself then it is not prime
        if(i%j==0):
            isPrime = 0;
            break
    # if the number is prime then it is appended to the list
    if(isPrime==1):
        primes.append(i);

print("Primes between 1 and 1000 are: ")
print(primes);