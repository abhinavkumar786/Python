# f = open("greet.txt")
# content = f.read()
# print(content)
# if("twinkle in content"):
#     print("the word twinkle is present in the content")
# else:
#     print("not present")



# import random
# def game():
#     score = random.randint(1,100)
#     print("you are playing a game...")
#     with open("hi-score.txt") as f:
#         hiscore = f.read()
#         if(hiscore!=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#     print(f"your score is {score}")
#     with open("hi-score.txt","w") as f:
#         if(score>hiscore):
#             f.write(str(score))
        
#         return score

# game()    





# import random

# def game():
#     score = random.randint(1, 100)
#     print("You are playing a game...")

#     # Read the existing high score
#     try:
#         with open("hi-score.txt", "r") as f:
#             hiscore = f.read()
#             hiscore = int(hiscore) if hiscore else 0
#     except FileNotFoundError:
#         hiscore = 0

#     print(f"Your score is {score}")

#     # Only update the file if the new score is higher
#     if score > hiscore:
#         with open("hi-score.txt", "w") as f:
#             f.write(str(score))

#     return score

# game()




def generatetables(n):
    





for i in range(2,21):
    generatetables(i)