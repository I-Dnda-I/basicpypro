import requests
import random

url = 'https://www.mit.edu/~ecprice/wordlist.10000'

response = requests.get(url)

if response.status_code == 200:
    palabras = response.text.splitlines()
    palabras_tupla = tuple(palabras)
else:
    print(f'Error al descargar el archivo: {response.status_code}')

name = input("Hi, whats your name?: ")
print(f"Good luck, {name}!")

magic_word = random.choice(palabras)

word_alike = ["-" ]* len(magic_word)
attempts = 12


while attempts > 0:
    print("".join(word_alike))
    letter = input("Guess a character: ").lower()
    
    if letter in magic_word:
        for i, value in enumerate(magic_word, start=0):
            if letter == magic_word[i]:
                word_alike[i] = letter
            
            if list(magic_word) == word_alike:
                break
    attempts = attempts - 1
    
    if list(magic_word) == word_alike:
        print("\nWell done, you win!!!")
        break
    print(f"\n{attempts} tries left")
    
else:
    print("\nYou lose!!!")
    print(f"The magic word was {magic_word}")
        
    