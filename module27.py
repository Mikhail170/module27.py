
def multiply(n):
    number_s = str(n)
    s0 = number_s[0]
    if len(number_s) > 1:
        s = number_s[1:len(number_s)]
        return int(s0)*multiply(int(s))
    else:
        if s0 == '0':
            return 1
        else:
            return int(s0)


result = multiply(10250)
print(result)
