# 괄호를 반드시 써야 하는 것이 아니더라도
# 항상 괄호를 써서 튜플의 시작과 끝을
# 나타내는 방법을 권장합니다.
# 명시적인 것이 암묵적인 것보다 낫습니다.
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo    # parentheses not required but are a good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))
