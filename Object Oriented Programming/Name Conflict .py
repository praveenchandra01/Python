class Base:
    x=10
    def __init__(self):
        self.x=20
class Derived(Base):
    def __init__(self):
        super().__init__()
obj=Derived()
print(obj.x,Derived.x)
