def numbers_to_strings(a,b,s):
    switcher = {
        add: print(a+b),
        sub: print(a-b),
        div: print(a/b),
        mul: print(a*b)
    }
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(s, "nothing")
# Main program
if __name__ == "__main__":
    print("Enter your numbers: ")
    a,b=int(input()).split()
    s=input()
    print (numbers_to_strings(a,b,s))