a=int(input())
b=int(input())
if b>9 and b<100:
    s=b%10+b//10
    if s>9 and s<100:
        print("Сумма цифр равна двузначному числу",s)
    else:
        print("Сумма цифр не равна двузначному числу",s)
else:
    print("Введите двузначное число")
if  s>a:
    print("Сумма цифр двузначного числа s>",a)
else:
    print("Сумма цифр двузначного числа s<",a)