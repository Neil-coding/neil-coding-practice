

# # make a function that gets the smallest number


# x = [5,3,7,3,3,3,3,3,3,3,3,3,3,2,35]

# def get_smaller(numbers: list):
#     smallest = numbers[0]
#     for current in numbers:
#         if current < smallest:
#             smallest = current
#     return smallest



# print(get_smaller([2,-35]))
    

# print(get_smaller([100, 200]))





# ada challenege
# start with an empty list
# add 1000 zeros to it
 

Manynumbers = [0]

# # hint
# # no functions necessary (so no def)
# # you'll want a for loop
# # and use .append()
# Manynumbers .append(0) # adds 0 to the list, 1 time
# Manynumbers .append(0) # adds 0 to the list again! now there are two 0s

# # to get length of a list
# len(Manynumbers)

# to loop as many times as you want
# for x in range(1000): 
#     Manynumbers .append(0)
     

# print(Manynumbers)

# new challenge
ls = [1,2,4,2,8,4,3,9,10]

# go through this list, and remove anything that is out of order.
# like the way you add stuff is .append, the way you remove is list.remove()
# " go through this list" pretty much always means use a for loop

last = ls[0]
for current in ls[1: ]:
    # current being bigger than last is actually sorted
    # we want to find UNSORTED numbers.
    # so you can switch the > to a < 
    if current < last:
        ls .remove(current)
    last = current


print (ls)








