def total(a=5, *numbers, **phonebook):
    print('a', a)
    
    # 튜플의 모든 항목을 순회합니다
    for single_item in numbers:
        print('single_item', single_item)
        
    # 딕셔너리의 모든 항목을 순회합니다
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

total(10,1,2,3,Jack=1123,John=2231,Inge=1560)
