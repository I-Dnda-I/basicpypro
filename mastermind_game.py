import random



dict_op = {'h':2,'e':1}
size = int(input("Set the number of digits: "))
a, b = [10**(size-1), 10**(size)-1]

while 1:
    
    op = dict_op.get(input("Choose difficulty ('h' for hard mode or 'e' for izi mode): "),0)
    cont =1
    if op == 1:

        rand_num = round(random.uniform(a,b))
        guessed_num = ["+"]* size
        list_rand_num = list(str(rand_num))
        while 1:
            att_num = list(str(input(f"Guess the numer with {size} digits: ")))
            if att_num == list_rand_num:
                break
            for i in range(size):
                if att_num[i] == list_rand_num[i]:
                    guessed_num[i] = att_num[i]
            print(guessed_num)
            cont = cont + 1
        print(f"Grats, you guess the number with {cont} tries")

    elif op == 2:
        rand_num = round(random.uniform(a,b))
        guessed_num = ["+"]* len(rand_num)
        list_rand_num = list(str(rand_num))
        n_in_pos =0
        while 1:
            att_num = list(str(input(f"Guess the numer with {size} digits: ")))
            if att_num == list_rand_num:
                 break
            for i in range(size):
                if att_num[i] == list_rand_num[i]:
                    n_in_pos = n_in_pos +1
            print(f"There is {n_in_pos} digits in correct position ")
            cont = cont +1
        print(f"Grats, you guess the number with {cont} tries")
            
    else:
        print("You left.")
        break
    