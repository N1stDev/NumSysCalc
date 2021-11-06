def not1_to_d(num, not1):
    n = 0
    number_d = 0
    if '.' in num:
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
    for i in reversed(w_part):
        if (ord(i) >= 97) and (ord(i) <= 102):
            a = ord(i) - 87
        else:
            a = int(i)
        number_d += a * (not1 ** m1)
        m1 += 1

    m2 = -1
    for i in f_part:
        if (ord(i) >= 97) and (ord(i) <= 102):
            a = ord(i) - 87
        else:
            a = int(i)
        number_d += a * (not1 ** m2)
        m2 -= 1

    return number_d


def d_to_not2(num, not2):
    w_part = int(num) 
    f_part = num % 1 
    res = ""
    if w_part == 0:  
        res += str(0)
    else:
        while w_part > 0: 
            a = w_part % not2
            if a >= 10:
                res += chr(87 + a)
            else:
                res += str(a)
            w_part = w_part // not2

    res = res[::-1]
    res += '.'

    for i in range(10): 
        
        f_part = f_part * not2
        b = int(f_part)
        if b >= 10:
            c = chr(87 + b)
        else:
            c = b
        res += str(c)
        f_part = f_part % 1

    return res


number = input("Введите данное число: ").lower()  
notation1 = int(input("Введите его основание: "))  
notation2 = int(input("Введите основание результата: "))  
d_number = not1_to_d(number, notation1)  
result = d_to_not2(d_number, notation2)  
print(result.upper())
