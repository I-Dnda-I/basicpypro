import random

list_n = []
dictio = {"s":1, "p":0}
current = 0
turn = dictio[input("Quieres empezar primero o segundo? ('p' si es primero o 's' si es segundo) ")]

mach_turn = 'w' if not turn else 'l' 
while 1:
    if turn :
        if current == 20:
            print("You win!!!")
            break
        if(mach_turn == 'l'):
            cant_rand_num = round(random.uniform(1,3))
            
        else:
            cant_rand_num = 4 - (current) % 4
            
        while cant_rand_num > 0:
            list_n.append(current + 1)
            current = current + 1
            cant_rand_num = cant_rand_num - 1 
            turn = 0
    else:
        if current == 20:
            print("You lose!!!")
            break
        values = list(map(int,input(f"Ingrese 1 - 3 numeros consecutivos empezando con {current + 1}: ").split()))
        size = len(values)
        list_n.extend(values)
        
        current = current+ size
    
        turn = 1
    print(list_n)