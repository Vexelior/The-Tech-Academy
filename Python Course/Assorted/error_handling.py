


def getInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("n\Please provide the second numeric value: ")
    return var1,var2

def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e:
            print("{}: \n\nYou did not provide a numeric value!".format(e))
        except:
            ("\n\nOops, you provided an invalid input, program will close now!")
    print("{} + {} = {}".format(var1,var2,var3))


if __name__ == "__main__":
    compute()
