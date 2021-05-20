for i in range(1,5):
    for j in range(1,8):
        if  j<=3+i  and  j>=5-i:
            print('* ',end=' ')
        else:
            print("  ",end=' ')
    print()
input()
            
