## 함수 선언부

def add_func(n1,n2) :
    return n1 + n2

def sub_func(n1,n2) :
    return n1 - n2

def mul_func(n1,n2) :
    return n1 * n2




## 전역 변수부
num1,num2 = 100, 200
result = 0

##메인 코드부
result = add_func(num1,num2)
print(num1,'+',num2,'=',result)

result = sub_func(num1,num2)
print(num1,'-',num2,'=',result)

result = mul_func(num1,num2)
print(num1,'*',num2,'=',result)



