number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # 이곳에서 새 블록을 시작
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # 이곳에서 새 블록을 종료
elif guess < number:
    # 또 다른 블록
    print('No, it is a little higher than that')
    # 블록 안에서 원하는 무엇이든 할 수 있습니다...
else:
    print('No, it is a little lower than that')
    # 여기에 도달했다면 분명 guessed > number일 것입니다

print('Done')
# if 문의 실행이 끝나면 이 마지막 문장이 항상 실행됩니다
