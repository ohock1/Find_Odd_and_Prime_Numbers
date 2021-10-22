from math import *

bound_low = int(input("Input a lower bound integer: "))

bound_high = int(input("Input a higher bound integer: "))

even = 0
odd_count = 0
prime_count = 0 

prime = []
odd = []

the_range = range(bound_low,bound_high+1)

for i in the_range:
    if i % 2 == 0:
        even = even + 1
        odd_count = (bound_high - bound_low) - even
    else:
        odd.append(i)
        
        
for i in the_range:
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime.append(i)
            prime_count = prime_count + 1
            
       

print("You have ",odd_count," number of odd numbers in the range.")
print(odd)
print("You have ",prime_count," number of prime numbers in the range.")
print(prime)
