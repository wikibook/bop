poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# 쓰기('w'riting) 모드로 엽니다
f = open('poem.txt', 'w')
# 텍스트를 파일에 씁니다
f.write(poem)
# 파일을 닫습니다
f.close()

# 모드를 지정하지 않으면 기본적으로
# 읽기('r'ead) 모드로 가정합니다
f = open('poem.txt')
while True:
    line = f.readline()
    # 길이가 0이면 EOF을 나타냅니다
    if len(line) == 0:
        break
    # 파일에서 읽어오고 있으므로
    # `line`의 각 줄 끝에는 
    # 개행 문자가 있습니다
    print(line, end='')
# 파일을 닫습니다
f.close()
