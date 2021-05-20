def decor_result(result_function):#result_function = result
    def distinction(marks):
        for m in marks:
            if m>=75:
                print("Congrats !! you have got Distinction")
        else:
            result_function(marks)
    return distinction        


@decor_result
def result(marks):
    for m in marks:
        if m>=33:
             pass
        else:
               print("FAIL")
               break
    else:
        print("PASS")
            
result([50,70,70,99,80])
input()
