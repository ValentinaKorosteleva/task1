def find_password(n):
    password=''
    numbers = list(range(1,21))

    for i in numbers:
        for j in numbers:
            if i < j:
                sumij= i + j
                if sumij % n == 0:
                    password += str (i) + str(j)

    return password
while True:
    try:
        n=int(input('введите целое число от 3 до 20:'))
        if 3 <= n <= 20:
            break
        else:
            print('некорректный ввод введите целое число от 3 до 20')
    except ValueError:
        print()

print(f'parol:  {find_password(n)}')