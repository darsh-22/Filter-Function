############################
##    This is method 1    ##
############################

def highest_even(lst):
    even_lst = []
    for i in lst:
        if i % 2 == 0:
            even_lst.append(i)
    return max(even_lst)

print(highest_even([1,2,3,4,5,6,7,8,9,10,11,12]))

############################
##    This is method 2    ##
############################


def only_even_lst(lst):
    return lst % 2 == 0         # after iterating through list returns true and false

# First filtering original list with only even and after filtering
# listing the even values in list and printing maximum number of list
print(max((list(filter(only_even_lst, [1,2,13,4,5,6,7,8,9,10,11,12])))))    