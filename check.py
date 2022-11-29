# a python function that takes a list and returns a new list with unique elements of the first list
# sample list[1,1,2,3,3,2,2,1,4,5,4,6,6,7,7,8,7,7,9]
def unique(numbers):
    no = []
    for a in numbers:
        if a not in no:
            no.append(a)
    return no 

print(unique([1,1,2,3,3,2,2,1,4,5,4,6,6,7,7,8,7,7,9]))


        
    

