
#Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]


for num in numbers:
    if num < 0:
 

        print (num)


negative_numbers = list(filter(lambda x: x<0, numbers ))

print (negative_numbers)
