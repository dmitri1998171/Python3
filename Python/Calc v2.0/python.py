
integ_int = []
integ_char = []

s = input('Enter a string: ')
l = len(s)


def integration_int(integ_int,s,l):
    
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            integ_int.append(int(s_int))
 
    print(integ_int)
    return integ_int


def integration_char(integ_char, s,l):
    
    i = 0
    while i < l:
        s_char = ''
        a = s[i]
        while not '0' <= a <= '9':
            s_char += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_char != '':
            integ_char.append(s_char)
 
    print(integ_char)
    return integ_char


def calculation(a,b,simbol):
    if(simbol == '^'): a = pow(a,b)
    if(simbol == '+'): a = a + b
    if(simbol == '-'): a = a - b
    print(a)


def grandIntegration(integ_int, integ_char,l):
    a = []
    b = []
    simbol = []
    i = 0

    len_int = len(integ_int)
    len_char = len(integ_char)

    a = integ_int[0]
    while i < len_int:
        float(integ_int[i])
        b = integ_int[i+1]
        simbol = integ_char[i]

        calculation(a,b,simbol)

        i += 1

        if(i==len_int-1): break



integration_int(integ_int, s, l)
integration_char(integ_char, s, l)
grandIntegration(integ_int, integ_char, l)

# 10^2+12^2+14-18324 











