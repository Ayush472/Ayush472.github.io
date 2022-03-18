def add(*a):
    print(sum(a))
add(111,222,333,444,555)
add(11,22,33,44)
add(1,2,3)


def even(*a):
    t=0
    for x in a:
        if x%2==0:
            t=t+x
    print(t)

even(1,2,3,4,5)