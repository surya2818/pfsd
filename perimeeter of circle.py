import math
class Calc:
    r=int(input())
    b=int(input())
    c=int(input())
    def peri(self):
        peri = math.pi * 2 * self.r
        print("perimeeter of circle",peri)
    def area(self):
        area=math.pi*self.r*self.r
        print("area of circle",area)
    def perirec(self):
        perirec=2*self.b*self.c
        print("perimeeter of rectangle",perirec)
    def arearec(self):
        arearec=self.b*self.c
        print("area of rectangle",arearec)
    def areatri(self):
        areatri=self.b*self.c*self.r
        print("area of triangle",areatri)
    def peritri(self):
        peritri=self.b+self.r+self.c
        print("perimeeter of triangle",peritri)
a=Calc()
a.peri()
a.area()
a.perirec()
a.arearec()
a.areatri()
a.peritri()
