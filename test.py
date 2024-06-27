def barg(x):
    if x%2 == 0 :
        barg(x-1)
    if x%3 == 0:
        barg(x-1)
    