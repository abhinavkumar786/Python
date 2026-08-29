# def square(n):
#     return n*n
# print(square(5))
# square=lambda x:x*x
# print(square(5))


# list=["abhinav","rajat","aditya"]
# join="::".join(list)
# print(join)

# a="{} is a good {}".format("abhinav","boy")
# print(a)
# # we can also change the position of the arguments
# a="{1} is a good {0}".format("abhinav","boy")
# print(a)


# MAP:<----------------------<<<<<<<<<<<<




# l = [1, 2, 3, 4, 5]            # 1) a list of numbers

# square = lambda x: x * x       # 2) a function that squares a number

# sqList = map(square, l)        # 3) map returns an iterator that will apply square to each item
# print(list(sqList))            # 4) convert to list to see the results
# # Output: [1, 4, 9, 16, 25]

# def square_with_loop(n):
#     result = 0
#     for _ in range(abs(n)):  # simulate repeated addition
#         result += abs(n)
#     return result

# l = [1, 2, 3, 4, 5]
# sqList = map(square_with_loop, l)
# print(list(sqList))
# Output: [1, 4, 9, 16, 25]

# IN ONE LINE:
# print(list(map(lambda x: x*2, [1, 2, 3])))
# Output: [2, 4, 6]


# L=[1,2,3,4]
# square=lambda x:x*x
# sqlist=map(square,L)
# print(list(sqlist))
# # map() returns a map object (iterator), not a list.
# print(list(map(lambda x:x*x,[5,6,7,8,9])))
# list(...) forces it to run through all items and store them in a list.



# l = [1, 2, 3, 4, 5]
# square = lambda x: x * x

# sqList = map(square, l)   # create the map object again
# print(list(sqList))       # consumes it and prints

# # If you want to print again:
# sqList = map(square, l)   # re-create it
# print(list(sqList))
# print(list(sqList))
# sqList is a map object (an iterable) returned by map().

# list(sqList) consumes that iterable — meaning it goes through each item one by one, calls the function you gave to map(), and stores all the results into a list.

# This is the moment when your map() function actually runs for each element.

# Without calling list() (or looping over sqList), the map() function won’t execute — it’s lazy.

# So yes:

# list(...) is there to consume the iterable and trigger the map function calls.

# Once consumed, the map object is empty, and running list(sqList) again will give [].

# l = [1, 2, 3, 4, 5]

# def square(x):
#     print(f"Squaring {x}")
#     return x * x

# sqList = map(square, l)  # map object created, still not executed

# print("Consuming map with a loop:")
# for result in sqList:    # Iterates over map, triggering function calls
#     print("Result:", result)



# FILTER<-----------<<<<<<<<<<<<<<<<<<<

# l=[1,2,3,4,5]
# def even(n):
#     if n%2==0:
#         return True
#     return False
# onlyeven=filter(even,l)
# print(list(onlyeven))

# COMBO<<<<<<<_--------------------

# square only the even numbers:

# l=[1,2,3,4,5]
# result = list(map(lambda x: x*x, filter(lambda x: x%2==0, l)))
# print(result)
# Output: [4, 16]
# these can be operated for list,tuples,sets,strings,genreators
# same for reduce

# l1=[1,2,3,4]
# l2=[5,6,7,8]
# sum=lambda a,b:a+b
# s=map(sum,l1,l2)
# print(list(s))#by loop for both the lists and then add and append it 

# REDUCE FUNCTION:
# from functools import reduce
# reduce(function, iterable[, initializer])initializer (optional) is the starting accumulator value.


# from functools import reduce
# l=[1,2,3,4]
# def sum(a,b):
#     return a+b
# print(reduce(sum,l))

# reduce(lambda a,b: a+b, [1,2,3], 10)
# steps: 10+1=11, 11+2=13, 13+3=16 -> result 16
