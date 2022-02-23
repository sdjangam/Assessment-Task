a=123

rem1=a%10
a=a//10
rem2=a%10
a=a//10

rev=rem1*100+rem2*10+a
print(a)