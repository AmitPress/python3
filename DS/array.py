# in python arrays are called list

                                                # CRUD for list

# Create a list --

    #constructor
# l = list([1,2,3,4,5])  # takes a arg of list or set
# print(l[0])

    # literal
# l = [1,2,3,4,5]
# print(l[3])

    #type conversion

    # i) set to list
# s = {1,2,3,4,5} # is a set
# l = list(s)
# print(l[0])


    # ii) dict to list
# d = {"hi":1, "hello":2} # is a dict
# l = list(d)
# print(l[-1]) # it will just give the keys of the dictionary


    # iii) map to list
# m = {1:2,4:5} # is a map
# l = list(m)
# print(l[1]) # it will just give the keys of the dictionary


    # iv) map values to list
# m = {1:45,2:49,3:90}
# l = m.values()
# print(l[1])

    # v) map keys to list
# m = {1:45, 2:46, 3: 47}
# l = m.keys()
# print(l[1])

# so by default if we convert map to list using list() it will make an array of keys as of m.keys()


# Reading list --

    # using a loop
# l = [1,2,3,4,5,6,7]
# for intg in l:  # intg is an individual data of the list
#     print(intg) # will add extra next line

    # using a loop with enum
# l = [1,2,3,4,5,6,7]
# for i, intg in enumerate(l): # enumerate method will separate the indices from the data
#     print(str(i)+"->"+str(intg))

    # reverse a list
# l = [1,2,3,4,5,6,7,8]
# l.reverse() # this will reverse the list
# for x in l:
#     print(x)

    # sort and print list
# l = [4,2,6,8,1,3]

# l.sort()    #just use this sort method

# for x in l:
#     print(x)

    # what if u need to sort in desc order??

# l =[2,6,1,7,9,10]
# l.sort()
# l.reverse()
# for x in l:
#     print(x)

    # fetching an element's index
# l = [2,1,3,4,7,9]
# print(l.index(1)) # read it like index of 1

# Updating a list---

    #inserting a number in the first position (prepending)
# l = [3,4,1,2,7]
# l.insert(0,8)
# print(l)
    #inserting a number in the last position (appending)
# l = [3,4,1,2,7]
# l.insert(len(l),8)
# print(l)

    #or use append()
# l = [3,4,1,2,7]
# l.append(8)
# print(l)



