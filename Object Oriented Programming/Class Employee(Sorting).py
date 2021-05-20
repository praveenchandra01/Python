class Employee:
    def __init__(self, x, y, z):
        self.name = x
        self.emid = y
        self.salary = z

    def Sal_sort(self, l):
        l.sort(key=lambda x: x.salary, reverse=True)
        l1 = []
        for i in range(3):
            l1.append((l[i].name, l[i].emid, l[i].salary))
        print("List of Employee sorted according to their Salary : :\n", l1)


l = []  # Executuon starts fom here
for i in range(3):
    n = input("Enter Employee Name :")
    a = int(input("Enter Employee id :"))
    b = int(input("Enter Employee Salary :"))
    l.append(Employee(n, a, b))
for i in l:
    print(i.name, i.emid, i.salary)

l.sort(key=lambda x: x.name)
l1 = []
for i in range(3):
    l1.append((l[i].name, l[i].emid, l[i].salary))
print("List of Employee sorted according to their Names :\n", l1)
E1 = Employee(n, a, b)
E1.Sal_sort(l)
input()
