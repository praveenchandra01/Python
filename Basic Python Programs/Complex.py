c=complex(input("Enter complex number="))
print("Complex number:",c,"Real part:",c.real,"Imagnary Part:",c.imag)
print("Greatest is",max(c.real,c.imag))
if c.real>c.imag :
    print("Greatest is ",c.real)
else :
    print("Greatest is ",c.imag)
input()
          
