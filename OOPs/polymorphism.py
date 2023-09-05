class A:
    def show(self):
        print('show in A')


class B(A):
    def show(self):
        super().show()
        print('show in B')


class C(B):
    def show(self):
        A.show(self)
        print('show in c')



c = C()
c.show()