# данная программа реализует перевод дробного числа из одной системы счисления в другую
# алгоритм сначала переводит имеющееся число в десятичную систему, а затем из десятичной в новую

# Перевод имеющегося числа в десятичное число
def not1_to_d(num, not1):
    n = 0
    number_d = 0
    if '.' in num:  # Разделение числа на две части: w_part - целая часть, f_part - дробная часть
        for i in num:
            if i == '.':
                break
            n += 1
        w_part = num[0:n]
        f_part = num[n+1:len(num)]
    else:
        w_part = num
        f_part = "0"

    m1 = 0
    for i in reversed(w_part):  # перевод целой части в 10-чную систему счисления
        if (ord(i) >= 97) and (ord(i) <= 102):
            a = ord(i) - 87
        else:
            a = int(i)
        number_d += a * (not1 ** m1)
        m1 += 1

    m2 = -1
    for i in f_part:  # перевод дробной части в 10-чную систему счисления
        if (ord(i) >= 97) and (ord(i) <= 102):
            a = ord(i) - 87
        else:
            a = int(i)
        number_d += a * (not1 ** m2)
        m2 -= 1

    return number_d


# Перевод промежуточного десятичного числа в необходимую систему счисления
def d_to_not2(num, not2):
    w_part = int(num)  # целая часть
    f_part = num % 1  # дробная часть
    res = ""
    if w_part == 0:  # если целая часть 0 - 0 будет целой частью и в новой системе счисления
        res += str(0)
    else:
        while w_part > 0:  # перевод челой части в новую систему счисления
            a = w_part % not2
            if a >= 10:
                res += chr(87 + a)
            else:
                res += str(a)
            w_part = w_part // not2

    res = res[::-1]
    res += '.'

    for i in range(10):  # точность вычисления дробной части (10 знаков после запятой в данном случае)
        # перевод дробной части в новую систему счисления
        f_part = f_part * not2
        b = int(f_part)
        if b >= 10:
            c = chr(87 + b)
        else:
            c = b
        res += str(c)
        f_part = f_part % 1

    return res


number = input("Введите данное число: ").lower()  # Число, которое имеем на входе
notation1 = int(input("Введите его основание: "))  # Система счисления имеющегося числа
notation2 = int(input("Введите основание результата: "))  # Новая система счисления
d_number = not1_to_d(number, notation1)  # Промежуточное десятичное число
result = d_to_not2(d_number, notation2)  # Итоговое число
print(result.upper())
