import datetime

current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day

year,month,day = map(int, input("생일입력").split())
year,month,day

if current_month > month : #현재월 >생일월
    age= current_year - year
elif current_month < month: #현재월 <생일월
    age= current_year - year -1
else:                           #현재월 =생일월
    if current_day < day:            #현재일 <생일
        age= current_year - year -1
    else:                            #현재일 >=생일
        age = current_year - year

print("현재날짜 : %d-%d-%d" %(current_year,current_month,current_day))
print("출생날짜 : %d-%d-%d" %(year,month,day))

print( "사용자의 나이 : 만 %d세 입니다" %age)