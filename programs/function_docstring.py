def print_max(x, y):
    '''두 숫자 중 최댓값을 출력합니다.

    두 숫자는 정수여야 합니다.'''
    # 가능할 경우 정수로 변환
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
