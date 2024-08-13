import random
from math import log,ceil
a = int(input("Ingrese el minimo del rango: "))
b = int(input("Ingrese el maximo del rango: "))

rand_value = round(random.uniform(a,b), ndigits=None)

n_ideal_at = ceil(log(b-a+1,2))

n_at = 1

guess_value = -1
while n_at <= n_ideal_at:
    guess_value = int(input("Adivine el numero: "))
    
    if guess_value > rand_value:
        print("You guessed  too  high!!")
    elif guess_value < rand_value:
        print("You guessed too low!!!")
    else:
        if n_at <= n_ideal_at:
            print(f"Congratulations , you did in {n_at} attempts")
        else:
            print("You got it, but you can do better :)")
        break
    n_at = n_at + 1
    