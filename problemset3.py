# a=input("enter your name: ")
# print("Good afternoon")
# print(f"Good Afternoon {a}")


# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# print(letter.replace("<|Name|>","Abhinav").replace("<|Date|>","18 May,2025"))


# name="Abhinav is a good  boy"
# print(name.find("  "))
# if it returns -1 that means there is no double space
#if not found=-1 and if found=index


# print(name.replace("  "," "))
#original string will remain as it is, the replace one is a new one 
#strings are immutable which means you cannot change them by running
#functions on them


# letter = "Dear Harry,\n\t this python course is nice.\nThanks!"
# print(letter)


# what does .find ,.replace called ?



# ✅ Reason why .isalpha() is important:
# It ensures that spaces, numbers, and symbols are not counted as consonants.


# Count vowels and consonants in a string------>

# FIRST METHOD:
# s=input()
# v_count=0
# c_count=0
# for x in s:
#     if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
#         v_count+=1
#     else:
#         c_count+=1
# print("vowel counts:",v_count,"consonant count:",c_count)




# SECOND METHOD:(OPTIMISED)
# def counts(string):
#     string = string.lower()
#     v_count=0
#     c_count=0

#     for x in string:
#         if x.isalpha():
#             if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
#                 v_count+=1
#             else:
#                 c_count+=1
#     return v_count,c_count
            

# string = input("enter a string:")
# vowels,consonants=counts(string)
# print("vowel count:",vowels,"consonant count:",consonants)


# THIRD METHOD:(OPTIMISED)
# def counts(string):
#     string=string.lower()
#     v_count=0
#     c_count=0
#     vowels="aeiou"
#     for x in string:
#         if x.isalpha():
#             if x in vowels:
#                 v_count+=1
#             else:
#                 c_count+=1
#     return v_count,c_count

# string=input()
# vowels,consonants=counts(string)
# print("vowels:",vowels,"consonants:",consonants)


# Reverse a string without using reverse():



#String → List → Reverse → Join → New String
# ''.join(lst)
# '' → this is the separator (empty string means no space between characters).
# .join(lst) → combines all elements of the list into one string.
# s="abhinav"   #n Python, variable names are just references (pointers) to objects.
# s="kumar"     #The old string object still exists in memory, but since nothing refers to it anymore, Python will garbage collect it later.
# print(s)
# s = "HELLO"
# print(s.lower())  # "hello"
# print(s)          # "HELLO" (original remains unchanged)

# string=input()
# l=[]
# z=len(string)
# for x in string:
#     l.append(x)
# for y in range(z//2):
#     a=l[y]
#     l[y]=l[z-y-1]
#     l[z-y-1]=a
# string="".join(l)
# print(string)



# Count frequency of each character in string:
# string=input()
# visited=set()
# count=1
# z=len(string)
# for x in range(0,z):
#     count=1
#     a=string[x]
#     if a.isalpha() and a not in visited:
#         for y in range(x+1,z):
#             if a==string[y]:
#                 count+=1
#             else:
#                 continue
#         print(f"frequency of {string[x]} is:",count)
#         visited.add(a)



# SECOND METHOD:--------->O(n)
# string = input()
# freq = {}

# for char in string:
#     if char.isalpha():  # Only count alphabets
#         freq[char] = freq.get(char, 0) + 1

# for char, count in freq.items():
#     print(f"frequency of {char} is: {count}")






# count words in the sentence:
# s="will power is the greatest power"
# count=0
# for x in s:
#     if x.isalpha():
#         count+=1
# print(f"total words in the sentence:{count}")


# C TO F:   F=(9C)/5+32
# c=int(input())
# f=(9*c)//5+32
# print(f"{f}F")


# Replace all vowels with '*':

# new_string = old_string.replace(old, new, count), count (optional) → number of occurrences to replace (default: all)


# def strings(s):
#     string=s.lower()
#     vowels="aeiou"
#     for x in string:
#         if x.isalpha():
#             if x in vowels:
#                 string=string.replace(x,"*")
#             else:
#                 continue
#     return string

# s=input()
# print(strings(s))


# 










# Check if two strings are anagrams: and pangram:<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------------------------------------(2)
# s1=input()
# s2=input()



