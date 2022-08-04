class A:
    def methodA(self):
        print("A class")
class B(A):
    def methodB(self):
        super().methodA()
        print("B class")
b = B()
b.methodB()