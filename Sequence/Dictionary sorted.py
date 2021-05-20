d={int(input("Enter key :")):(input("Enter Value :")) for x in range(0,5)}
'''d={3:'e',2:'a',1:'c',7:'b',5:'d'}'''
print(sorted(d))  #by kyes(only)
print(sorted(d.values()))#by values(only)
print(sorted(d.items()))#by default keys
print(sorted(d.items(),key=lambda x:x[1]))#by values
input()
