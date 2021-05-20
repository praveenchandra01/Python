
        
def addition(a, b):
        r = a+b
        print("{0}+{1}={2}".format(a, b, r))
        print()

def subtraction(a, b):
        r = a-b
        print("{0}-{1}={2}".format(a, b, r))
        print()


def multiplication(a, b):
        r = a*b
        print("{0}*{1}={2}".format(a, b, r))
        print()


def division(a, b):
        try:
            r = a/b
            print("{0}/{1}={2}".format(a, b, r))
        except ZeroDivisionError:
            print("Denominator Can't be Zero")
        print()  