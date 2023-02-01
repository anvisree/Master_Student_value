master=input("student")
a=master.replace('(',' ').replace(')',' ').split()    #a=["seven","times","five"]
print(a)

def number(input):
    if input == "zero":
        return 0
    elif input == "one":
        return 1
    elif input == "two":
        return 2
    elif input == "three":
        return 3
    elif input == "four":
        return 4
    elif input == "five":
        return 5
    elif input == "six":
        return 6
    elif input == "seven":
        return 7
    elif input =="eight":
        return 8
    elif input == "nine":
        return 9

def times(m,n):
    return m*n

def minus(m,n):
    return m-n

def plus(m,n):
    return m+n

def divided_by(m,n):
    return int(m//n)


def calculation(input,m,n):
    if input == "times":
        result = times(m,n)
        print(result)
    elif input == "minus":
        result = minus(m,n)
        print(result)
    elif input == "plus":
        result = plus(m,n)
        print(result)
    elif input == "divided_by":
        result = divided_by(m,n)
        print(result)

cal = calculation(a[1],number(a[0]),number(a[2]))

