responses=["Welcome to smart calulator","My name is Edith","ThankYou!","Sorry, this is beyond my ability"]

def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def lcm(a,b) :
    for i in range(1,int(a*b)+1):
        if i%a==0 and i%b==0:
            return i

def hcf(a,b):
    y=int(min(a,b))
    for i in range(y,1,-1):
        if a%i==0 and b%i==0:
            return i
            break


def add(a,b):
    return a+b

def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def end():
    print(responses[2])
    input("Press enter to exit")
    exit()

def myname():
    print(responses[1])

def Sorry():
    print(responses[3])

operations={"LCM":lcm,"HCF":hcf,"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"MINUS":sub,"SUBTACTION":sub,"DIFFRENCE":sub,"SUBTRACT":sub,
            "PRODUCT":mul,"MULITPLICATION":mul,"MULTIPLY":mul,"DIVIDE":div,"DIVISION":div}
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end}

ex={"LCM":lcm,"HCF":hcf}
            
