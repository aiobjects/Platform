print("The basic calculator ")
def numbers_to_strings(a,b,s):
    switcher = {
        '+': a+b,
        '-': a-b,
        '/': a//b,
        '*': a*b
    }
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(s, "nothing")
# Main program
if __name__ == "__main__":
    print("Enter your numbers: ")
    a,b=map(int,input().split())
    s=input()
    print (numbers_to_strings(a,b,s))