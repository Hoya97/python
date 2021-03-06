#정수형(integer) 정수를 뜻하는 자료형
a = 123
a = -547
a = 0

#실수형(Floating-point) 소숫점이 포함된 숫자
a = 1.23
a = -3.14

#컴퓨터식 지수 표현 방식 파이썬에선 4.24e10 혹 4.24E10 으로 표현 4.24e10은 4.24*10^10
#4.24E-10는 4.24*10^-10    (e와E 둘중 어느것을 사용해도 무방)
a = 4.24E10
a = 4.24e-10

#8진수(Octal) 숫자가 0o 또는 0O(숫자0 + 알파벳 소문자 o또는 대문자 O)로 시작해야됨
a = 0o177

#16진수(Hexadecimal) 0x로 시작
a = 0x8ff
b = 0xABC



#복소수 J또는 j사용
a = 1+2j
b = 3-4J

#복소수.real은 복소수의 실수부분을 리턴함
q = 1+2j
print(q.real)
#1.0

print("-"*50)#구분선

#복소수.imag는 복소수의 허수 부분을 리턴
w = 1+2J
print(w.imag)
#2.0

print("-"*50)#구분선

#복소수.conjugate()는 복소수의 켤레복소수를 리턴
e = 1+2j
print(e.conjugate())
#(1-2j)

print("-"*50)#구분선

#abs(복소수)는 복소수의 절댓값을 리턴(1+2j의 절댓값은 √1²+2²)
r = 1+2j
print(abs(r)) #2.23606797749979

print("-"*50)#구분선

#사칙연산
t = 3
u = 4
print(t+u) #7
print(t*u) #12
print(t/u) #0.75

print("-"*50)#구분선

#x의 y제곱을 나타내는 **연산자 x**y처럼 사용되었을 때 x의 y제곱(𝑥^𝑦) 값을 리턴
x = 3
y = 4
print(x ** y) #81 #3^4

print("-"*50)#구분선

#나눗셈 후 소수점 아랫자리를 버리는 //연산자
print(7/4) #1.75
print(7//4) #1 #1.75의 소수점 부분이 제거되 1이 나옴
