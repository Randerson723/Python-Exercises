authors = ["Connor Milliken", "Victor aNisimov",
           "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]


def sortSur(authors):
    l2 = []
    for ele in authors:
        l2.append(ele.split())
    authors = []
    for ele in sorted(l2, key=lambda x: x[-1]):
        authors.append(' '.join(ele))

    return authors


print('\nAfter sorting:\n', sortSur(authors))


places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]

#F = C * 9/5 + 32

F_C = lambda x:x*(float(9)/(5)+32)

list(map(F_C, places))
