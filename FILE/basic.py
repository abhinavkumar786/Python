# f = open("greet.txt","r")
# a = f.read()
# # a = f.readline()
# # read only first line
# print(a)
# f.close()


# f = open("write.txt","w")
# f.write("it is my first writing part of file program")
# f.close()
# it will delete the recent data in the file
# also create another file


# st = "Hey Abhinav you are amazing"
# f = open("my.txt","w")
# f.write(st)
# f.close()

# DIFFERENCE---------------->>>>>>>>>>>>>
# readline and readlines



# f = open("greet.txt","r")
# a = f.readline()
# print(a,type(a))
# f.close()
# Hello! How's your day
#  <class 'str'>



# f = open("greet.txt","r")
# a = f.readlines()
# print(a,type(a))
# f.close()
# ["Hello! How's your day\n", 'What are your plans for today\n', 'Today the weather is cloudy and pleasant'] <class 'list'>

# why first in double quotes and rest in single


# f = open("greet.txt")
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# # line4 = f.readline()nothing came just an empty string
# line4 = f.readline()
# line5 = f.readline()
# print(line1,line2,line3,line5=="")
# f.close()
# type--> str
# Hello! How's your day
#  What are your plans for today
#  Today the weather is cloudy and pleasant True
# if line1 = f.readlines() then it will return all in the form of list



# the empty string that we get can be treated as the end of file which is useful in loop
# f = open("greet.txt","r")
# line = f.readline()
# while(line!=""):
#     print(line)
#     line = f.readline()



# f = open("write.txt","a")
# f.write("\nnow i have a great idea of file handling")
# f.close()



# stop manually closing the file
# WITH statement:

# with open("greet.txt") as f:
#     print(f.read())/

# Hello! How's your day
# What are your plans for today
# Today the weather is cloudy and pleasant


# write function takes the string 