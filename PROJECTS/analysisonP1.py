# finding pattern for win and lose
# for win: 1 or -2
# for lose: -1 or 2


import random
computer = random.choice([1, -1, 0])
youstr = input("enter your choice as s,w or g: ")
dict = {"s":1, "w":-1, "g":0}
you = dict[youstr]

reversedict = {1:"snake", -1:"water", 0:"gun"}
print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]} ")
if(computer == you):
    print("its a draw")
else:
#     if(computer==-1 and you==1): -2
#         print("you win :>")
#     elif(computer==-1 and you==0): -1
#         print("you lose :<")


#     elif(computer==1 and you==0): 1
#         print("you win :>")
#     elif(computer==1 and you==-1): 2
#         print("you lose :<")


#     elif(computer==0 and you==1): -1
#         print("you lose :<")
#     elif(computer==0 and you==-1): 1
#         print("you win :>")
#     else:
#         print("something went wrong")
    
#-------------RESULT-------------->

    if((computer-you)==1 or (computer-you) == -2):
        print("you win:>")
    else:
        print("you lose :>")


# ------------------HOW-------------->???????????????
# enter your choice as s,w or g: g
# you chose gun
# computer chose water
# you win :>                   done
