places = [' ', 'Argentina', '  ', 'San Diego',
          '', '   ', '', 'Boston', 'New York']
#     = [Argentina, San Diego, Boston, New York]


new_places = list(filter(lambda x: x == 0), places)
print(new_places)

# .sort(key=)

authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

def sortSur(authors):
    l2 = []
    for ele in authors:
        l2.append(ele.split())
    authors = []
    for ele in sorted(l2, key=lambda x: x[-1]):
        authors.append(' '.join(ele))

    return authors

# HINT: YOU'LL NEED TO CONVERT EACH PERSON'S NAME (A STRING) INTO A LIST IN ORDER TO GRAB THE LAST NAME BY
# THE INDEX
places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]

result = map(lambda x: x* (9)/(5) + 32, places)
print(list(result))
# F = C * 9/5 + 32

# HINT: KEEP IN MIND PEMDAS. USE THE CELCIUS - FAHRENHEIT CONVERSION
# F = C * 9/5 + 32#


def recur_fibo(x):
    if x <= 1:
        return x
    
    else:
        return(recur_fibo(x-1) +recur_fibo(x-2))

xterms =int(input("How many terms?"))

if xterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Sequence:")
    for i in range(xterms):
        print(recur_fibo(i))
