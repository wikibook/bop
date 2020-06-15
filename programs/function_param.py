def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# 리터럴 값을 직접 전달
print_max(3, 4)

x = 5
y = 7

# 변수를 인수로 전달
print_max(x, y)
