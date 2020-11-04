#클래스 : 반복되는 변수와 메소드(함수)를 미리 정해놓은 틀(설계도)
class FourCal:
    pass
a = FourCal()
print(a)

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self,num):
        self.result += num
        return self.result
cal1 =Calculator()
cal2 =Calculator()

print(cal1.add(3))
print(cal2.add(4))

class FiveCal:
    def setdata(self, first,second) :
        self.first =first
        self.second =second
    def add(self):
        result = self.first + self.second
        return result

a = FiveCal()
a.setdata(4,2)
print(a.first)
print(a.second)
print(a.add())

class FiveCall:
    def __init__(self,first,second): #실행하면서 시작되는 것,설계도 같은것
        self.first = first
        self.second =second # 반드시 아래에 first,second의 변수가 나와야한다
    def setdata(self, first,second) :
        self.first =first
        self.second =second
    def add(self):
        result = self.first + self.second
        return result
class MoreFiveCal(FiveCall): #상속
    def pow(self) :
        result =self.first * self.second
        return result
#메소드 오버라이딩 :자식이 우선이다
    


a = FiveCall(2,3) # init 으로 설계했음으로, 여기 두개!
print(a.add())
b = MoreFiveCal(5,2)
print(b.add())
print(b.pow())

