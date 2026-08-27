n = int(input('digite um numero'))
primo = True

if n < 2:
    print(f'o numero {n} não é primo')

else:
    
    for divisor in range(2, n):
        if n % divisor == 0:
            primo = False

    if primo:
        print(f'o numero {n} é primo')
    else:
        print(f'o numero {n} não é primo')
