def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "eight",
        9: "Nine",
        10: "Ten",
    }
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")
# Main program
if __name__ == "__main__":
    print("Enter your Switch case: ")
    argument=int(input())
    print (numbers_to_strings(argument))