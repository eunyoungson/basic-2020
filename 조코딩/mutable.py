#Immutable (정수,실수,문자열,튜플)
a=1
def vartest(a):
    a =a+1
vartest(a)
print(a)

#mutable(리스트,딕셔너리,집합)
b = [1,2,3]
def vartest2(b):
    b = b.append(4)
vartest2(b)
print(b)

# [] 리스트, ( ) 튜플, { } 딕셔너리